import requests
import pandas as pd

def fetch_opensky_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()['states']

    columns = [
        "icao24",
        "callsign",
        "origin_country",
        "time_position",
        "last_contact",
        "longitude",
        "latitude",
        "baro_altitude",
        "on_ground",
        "velocity",
        "true_track",
        "vertical_rate",
        "sensors",
        "geo_altitude",
        "squawk",
        "spi",
        "position_source"
    ]

    df = pd.DataFrame(data, columns= columns)
    return df