import os
from sqlalchemy import create_engine, text

# --------------------------
# Use environment variables
# --------------------------
DB_URI = os.getenv(
    "POSTGRES_URI",
    "postgresql+psycopg2://airflow:airflow@postgres:5432/opensky"
)

engine = create_engine(DB_URI)

# --------------------------
# Dimension Table Upsert
# --------------------------
def upsert_dim_aircraft(df):
    if df.empty:
        return

    sql = text("""
        INSERT INTO dim_aircraft (aircraft_icao, callsign, origin_country)
        VALUES (:aircraft_icao, :callsign, :origin_country)
        ON CONFLICT (aircraft_icao) DO UPDATE
        SET
            callsign = EXCLUDED.callsign,
            origin_country = EXCLUDED.origin_country;
    """)

    # Replace NaN with None
    df = df.where(df.notnull(), None)

    with engine.begin() as conn:
        conn.execute(sql, df.to_dict(orient="records"))


# --------------------------
# Fact Table Insert
# --------------------------
def insert_fact_flight_position(df):
    if df.empty:
        return

    # Rename columns to match the table
    df = df.rename(columns={
        'last_contact': 'event_time',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'altitude': 'altitude',
        'velocity': 'velocity',
        'aircraft_icao': 'aircraft_icao'
    })

    # Replace NaN with None
    df = df.where(df.notnull(), None)

    sql = text("""
        INSERT INTO fact_flight_position (
            aircraft_icao, latitude, longitude, velocity, altitude, event_time
        )
        VALUES (
            :aircraft_icao, :latitude, :longitude, :velocity, :altitude, :event_time
        )
        ON CONFLICT (aircraft_icao, event_time) DO NOTHING;
    """)

    with engine.begin() as conn:
        conn.execute(sql, df.to_dict(orient="records"))
