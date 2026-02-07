import pandas as pd

def transform_opensky_data(df):
   
    df = df.dropna(subset=["icao24", "longitude", "latitude", "last_contact"])

    dim_aircraft = (
        df[['icao24', 'callsign', 'origin_country']]
        .drop_duplicates()
        .rename(columns={'icao24': 'aircraft_icao'})
    )

    fact_flight_position = (
        df[["icao24", "latitude", "longitude",
            "velocity", "baro_altitude", "last_contact"]]
        .rename(columns={
            'icao24': 'aircraft_icao',
            'baro_altitude': 'altitude',
            'last_contact': 'event_time'
        })
    )

  
    fact_flight_position["event_time"] = pd.to_datetime(
        fact_flight_position["event_time"], unit='s'
    )

   
    fact_flight_position = fact_flight_position.where(pd.notnull(fact_flight_position), None)

   
    return dim_aircraft, fact_flight_position
