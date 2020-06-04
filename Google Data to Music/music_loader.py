import mido
import time
from tonal import Tonal, mapping
import pandas as pd

def generate_a_music_response(data_object): 

    interim_container = {}

    target_variables = ['retail_and_recreation_percent_change_from_baseline', 'grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline', 'transit_stations_percent_change_from_baseline', 'workplaces_percent_change_from_baseline', 'residential_percent_change_from_baseline']

    for target in target_variables: 

        try:
            interim_container[target] = int(data_object[target] * data_object[target] / 100)
        except ValueError: 
            interim_container[target] = 0

    print (f"Original data: {data_object}")
    print (f"Sound data: {interim_container}")

    return interim_container

def send_to_player(_mode, _value): 

    output.send(mido.Message(_mode,note=mapping(value, mid_range),velocity=50,channel=1))

if __name__ == "__main__":

    output = mido.open_output()
    tonal = Tonal()
    mid_range = tonal.create_sorted_midi("MelodicMinor", "F")

    _data = pd.read_csv(r"..\Data Exploration\data\raw_google_data\bucharest_data.csv")

    try:
        _data["date_converted"] = pd.to_datetime(_data["date"], format = "%d/%m/%Y")
    except ValueError: 
        _data["date_converted"] = pd.to_datetime(_data["date"])

    _data = _data.sort_values(by = "date_converted")
    data_array = _data.to_dict('records')

    for data_object in data_array: 

        music_response = generate_a_music_response(data_object)

        for key, value in music_response.items():
            
            send_to_player(_mode = "note_on", _value = value)
            time.sleep(0.08)

    for data_object in data_array: 

        music_response = generate_a_music_response(data_object)

        for key, value in music_response.items():

            send_to_player(_mode = "note_off", _value = value)
            time.sleep(0.01)
