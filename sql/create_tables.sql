
DROP TABLE IF EXISTS fact_flight_position;
DROP TABLE IF EXISTS dim_aircraft;

CREATE TABLE dim_aircraft (
    aircraft_icao VARCHAR(10) PRIMARY KEY,
    callsign VARCHAR(20),
    origin_country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE fact_flight_position (
    id SERIAL PRIMARY KEY,

    aircraft_icao VARCHAR(10) NOT NULL,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    velocity DOUBLE PRECISION,
    altitude DOUBLE PRECISION,

    event_time TIMESTAMP NOT NULL,

    -- Natural key to prevent duplicates
    CONSTRAINT uq_fact_flight UNIQUE (aircraft_icao, event_time),

    -- Referential integrity
    CONSTRAINT fk_fact_aircraft
        FOREIGN KEY (aircraft_icao)
        REFERENCES dim_aircraft (aircraft_icao)
        ON DELETE CASCADE
);
