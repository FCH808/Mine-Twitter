### Pulls bounding box data for each of the 50 states in json format from the open street maps api.
#   Return a dictionary containing [Full State Name: [Abbrev: State Abbreviation],
#                                                    [Geo_box: geo-location bounding box coordinates]]  for each state.
###


import json
import urllib
from find_states import find_all_states


def find_all_state_boxes():
    all_states_dict = {}
    state_info = find_all_states()

    for state in state_info.keys():
        state_dict = {}
        json_load = json.load(urllib.urlopen("http://nominatim.openstreetmap.org/search?state=" + state + "%5C&country=USA%5C&format=jsonv2"), encoding='utf-8')
        try:
            raw_box = json_load[0]["boundingbox"]
            state_dict["Abbrev"] = state_info[state]
            state_dict["Geo_box"] = [float(raw_box[2]), float(raw_box[3]), float(raw_box[0]), float(raw_box[1])]
        except IndexError as err:
            state_dict["Abbrev"] = state_info[state]
            state_dict["Geo_box"] = [None, None, None, None]
            #print "ERROR:", err
            #print "STATE:", state
            #print json_load
            pass
        all_states_dict[state] = state_dict
    return all_states_dict

#print find_state_boxes()
