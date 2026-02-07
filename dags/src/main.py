from src.extract import fetch_opensky_data
from src.transform import transform_opensky_data
from src.load import upsert_dim_aircraft, insert_fact_flight_position

def main():
    raw_df = fetch_opensky_data()
    dim_aircraft, fact_flight_position = transform_opensky_data(raw_df)

    upsert_dim_aircraft(dim_aircraft)
    insert_fact_flight_position(fact_flight_position)
    print('Data saved Successfully')

if __name__ == '__main__':
    main()
