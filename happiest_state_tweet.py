### Mines twitter data obtained from the twitter API for sentiment.
# State geo boundry boxes are obtained from the sourced in function: find_state_boxes
# Assigns overall sentiment score to tweet based on tab-delimited sentiment rating dictionary with [word    rating] passed
#  in. e.g. [abandon	-2]
# Geocodes, place coordinates, and location info entered are mined (in that order) to obtain U.S state location of tweet.
# Tweets and ratings for each state are then aggregated and averaged, and the highest state/rating is printed to stdout.
# A dictionary is also returned containing total ratings and count of tweets that went into that total.
###

import sys
import json
import re
from find_state_boxes import find_all_state_boxes

#sent_file = open("AFINN-111.txt")
#tweet_file = open("output_all.txt")

  # Hard code this for this assignment. find_state_boxes sourced in and commented out.
#state_boxes = {'Mississippi': {'Abbrev': 'MS', 'Geo_box': [-91.6550140380859, -88.0980072021484, 30.1477890014648, 34.9960556030273]}, 'Oklahoma': {'Abbrev': 'OK', 'Geo_box': [-103.002571105957, -94.4312133789062, 33.6191940307617, 37.0021362304688]}, 'Wyoming': {'Abbrev': 'WY', 'Geo_box': [-111.05689239502, -104.052154541016, 40.9948768615723, 45.0034217834473]}, 'Minnesota': {'Abbrev': 'MN', 'Geo_box': [-97.2392654418945, -89.4833831787109, 43.4994277954102, 49.3844909667969]}, 'Illinois': {'Abbrev': 'IL', 'Geo_box': [-91.513053894043, -87.0199203491211, 36.9701309204102, 42.5083045959473]}, 'Georgia': {'Abbrev': 'GA', 'Geo_box': [-85.6051712036133, -80.7514266967773, 30.3557567596436, 35.0008316040039]}, 'Arkansas': {'Abbrev': 'AR', 'Geo_box': [-94.6178131103516, -89.6422424316406, 33.0041046142578, 36.4996032714844]}, 'New Mexico': {'Abbrev': 'NM', 'Geo_box': [-109.050178527832, -103.000862121582, 31.3323001861572, 37.0001411437988]}, 'Ohio': {'Abbrev': 'OH', 'Geo_box': [-84.8203430175781, -80.5189895629883, 38.4031982421875, 42.3232383728027]}, 'Indiana': {'Abbrev': 'IN', 'Geo_box': [-88.0997085571289, -84.7845764160156, 37.7717399597168, 41.7613716125488]}, 'Maryland': {'Abbrev': 'MD', 'Geo_box': [-79.4871978759766, -75.0395584106445, 37.8856391906738, 39.7229347229004]}, 'Louisiana': {'Abbrev': 'LA', 'Geo_box': [-94.0431518554688, -88.817008972168, 28.9210300445557, 33.019458770752]}, 'Idaho': {'Abbrev': 'ID', 'Geo_box': [-117.243034362793, -111.043563842773, 41.9880561828613, 49.000846862793]}, 'Arizona': {'Abbrev': 'AZ', 'Geo_box': [-114.818359375, -109.045196533203, 31.3321762084961, 37.0042610168457]}, 'Iowa': {'Abbrev': 'IA', 'Geo_box': [-96.6397171020508, -90.1400604248047, 40.3755989074707, 43.5011367797852]}, 'Michigan': {'Abbrev': 'MI', 'Geo_box': [-90.4186248779297, -82.122802734375, 41.6960868835449, 48.3060646057129]}, 'Kansas': {'Abbrev': 'KS', 'Geo_box': [-102.0517578125, -94.5882034301758, 36.9930801391602, 40.0030975341797]}, 'Utah': {'Abbrev': 'UT', 'Geo_box': [-114.053932189941, -109.041069030762, 36.9979667663574, 42.0013885498047]}, 'Virginia': {'Abbrev': 'VA', 'Geo_box': [-83.6754150390625, -75.2312240600586, 36.5407867431641, 39.4660148620605]}, 'Oregon': {'Abbrev': 'OR', 'Geo_box': [-124.703544616699, -116.463500976562, 41.9917907714844, 46.2991027832031]}, 'Connecticut': {'Abbrev': 'CT', 'Geo_box': [-73.7277755737305, -71.7869873046875, 40.9667053222656, 42.0505905151367]}, 'Montana': {'Abbrev': 'MT', 'Geo_box': [-116.050003051758, -104.039558410645, 44.3582191467285, 49.0011100769043]}, 'California': {'Abbrev': 'CA', 'Geo_box': [-124.482009887695, -114.13077545166, 32.5295219421387, 42.0095024108887]}, 'Massachusetts': {'Abbrev': 'MA', 'Geo_box': [-73.5081481933594, -69.8615341186523, 41.1863288879395, 42.8867149353027]}, 'West Virginia': {'Abbrev': 'WV', 'Geo_box': [-82.6447448730469, -77.7190246582031, 37.2014808654785, 40.638801574707]}, 'South Carolina': {'Abbrev': 'SC', 'Geo_box': [-83.35400390625, -78.4992980957031, 32.0333099365234, 35.2155418395996]}, 'New Hampshire': {'Abbrev': 'NH', 'Geo_box': [-72.55712890625, -70.534065246582, 42.6970405578613, 45.3057823181152]}, 'Vermont': {'Abbrev': 'VT', 'Geo_box': [-73.437744140625, -71.4653549194336, 42.7269325256348, 45.0166664123535]}, 'Delaware': {'Abbrev': 'DE', 'Geo_box': [-75.7890472412109, -74.9846343994141, 38.4511260986328, 39.8394355773926]}, 'North Dakota': {'Abbrev': 'ND', 'Geo_box': [-104.049270629883, -96.5543899536133, 45.9350357055664, 49.0004920959473]}, 'Pennsylvania': {'Abbrev': 'PA', 'Geo_box': [-80.5210876464844, -74.6894989013672, 39.7197647094727, 42.5146903991699]}, 'Florida': {'Abbrev': 'FL', 'Geo_box': [-87.6349029541016, -79.9743041992188, 24.3963069915771, 31.0009689331055]}, 'Alaska': {'Abbrev': 'AK', 'Geo_box': [-180.0, 180.0, 51.0228691101074, 71.6048278808594]}, 'Kentucky': {'Abbrev': 'KY', 'Geo_box': [-89.5715103149414, -81.9645385742188, 36.4967155456543, 39.1474609375]}, 'Hawaii': {'Abbrev': 'HI', 'Geo_box': [-178.443603515625, -154.755783081055, 18.8654594421387, 28.5172691345215]}, 'Nebraska': {'Abbrev': 'NE', 'Geo_box': [-104.053520202637, -95.3080520629883, 39.9999961853027, 43.0017013549805]}, 'Missouri': {'Abbrev': 'MO', 'Geo_box': [-95.7741470336914, -89.0988388061523, 35.9956817626953, 40.6136360168457]}, 'Wisconsin': {'Abbrev': 'WI', 'Geo_box': [-92.8881149291992, -86.2495422363281, 42.491943359375, 47.3025016784668]}, 'Alabama': {'Abbrev': 'AL', 'Geo_box': [-88.4731369018555, -84.8882446289062, 30.1375217437744, 35.0080299377441]}, 'New York': {'Abbrev': 'NY', 'Geo_box': [-79.7625122070312, -71.8527069091797, 40.4773979187012, 45.0158615112305]}, 'South Dakota': {'Abbrev': 'SD', 'Geo_box': [-104.05770111084, -96.4363327026367, 42.4798889160156, 45.9454536437988]}, 'Colorado': {'Abbrev': 'CO', 'Geo_box': [-109.060256958008, -102.041580200195, 36.9924240112305, 41.0023612976074]}, 'New Jersey': {'Abbrev': 'NJ', 'Geo_box': [-75.5633926391602, -73.8850555419922, 38.7887535095215, 41.3574256896973]}, 'Washington': {'Abbrev': 'WA', 'Geo_box': [-124.836097717285, -116.917427062988, 45.5437202453613, 49.00244140625]}, 'North Carolina': {'Abbrev': 'NC', 'Geo_box': [-84.3218765258789, -75.4001159667969, 33.7528762817383, 36.5880393981934]}, 'Tennessee': {'Abbrev': 'TN', 'Geo_box': [-90.310302734375, -81.6468963623047, 34.9829788208008, 36.6781196594238]}, 'District of Columbia': {'Abbrev': 'DC', 'Geo_box': [None, None, None, None]}, 'Texas': {'Abbrev': 'TX', 'Geo_box': [-106.645652770996, -93.5078201293945, 25.8370609283447, 36.5007057189941]}, 'Nevada': {'Abbrev': 'NV', 'Geo_box': [-120.005729675293, -114.039642333984, 35.0018730163574, 42.0022087097168]}, 'Maine': {'Abbrev': 'ME', 'Geo_box': [-71.0841751098633, -66.9250717163086, 42.9561233520508, 47.4598426818848]}, 'Rhode Island': {'Abbrev': 'RI', 'Geo_box': [-71.9070053100586, -71.1204681396484, 41.055534362793, 42.018856048584]}}

state_boxes = find_all_state_boxes()

states = []
for state in state_boxes:
    states.append(state_boxes[state]['Abbrev'])

def make_sent_dict(text_file):
    scores = {}

    for line in text_file:

        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def score_tweet(tweet, sent_dict):
    score = 0
    for sent_entry in sent_dict.items():
        try:
            if sent_entry[0].lower() in tweet['text'].lower().encode('utf-8'):
                score += sent_entry[1]
        except KeyError as err:
            break
    return score


def find_happy(sent_text, tweets_txt):
    sent_dict = make_sent_dict(sent_text)


    # Only search the end of the word for state abbreviations since there are a lot of false positives like 'de' in spanish location.
    regex = re.compile(r'\b(' + '|'.join(states) + r')$\b', re.IGNORECASE)

    coord = 0
    place = 0
    user_location = 0
    geo = 0
    delete = 0
    total = 0

    # Git lazy =( Adhoc add.
    happiness = {}

    def add_happiness(dict, state_abbrev, current_score):
        if state_abbrev in dict.keys():
            dict[state_abbrev][0] += 1
            dict[state_abbrev][1] += 1
        else:
            dict[state_abbrev] = [current_score, 1]
        return dict

    for line in tweets_txt.readlines():
        temp_json_line = json.loads(line)

        current_score = score_tweet(temp_json_line, sent_dict)

        if "delete" in temp_json_line.keys():
            delete += 1
            continue
        if "geo" in temp_json_line.keys() and temp_json_line["geo"] is not None:
            geo += 1
            for state in state_boxes:
                long = temp_json_line["geo"]["coordinates"][1]
                lat = temp_json_line["geo"]["coordinates"][0]
                if state_boxes[state]["Geo_box"][0] <= long <= state_boxes[state]["Geo_box"][1] and state_boxes[state]["Geo_box"][2] <= lat <= state_boxes[state]["Geo_box"][3]:
                    happiness = add_happiness(happiness, state_boxes[state]["Abbrev"], current_score)
                    break

        elif "coordinates " in temp_json_line.keys()and temp_json_line["coordinates"] is not None:
            coord += 1

        elif "place" in temp_json_line.keys() and temp_json_line["place"] is not None:
            place += 1
            long = 0
            lat = 0
            for i in temp_json_line["place"]["bounding_box"]["coordinates"][0]:
                long += i[0]
                lat += i[1]
            long = long/4
            lat = lat/4
            for state2 in state_boxes:
                if state_boxes[state2]["Geo_box"][0] <= long <= state_boxes[state2]["Geo_box"][1] and state_boxes[state2]["Geo_box"][2] <= lat <= state_boxes[state2]["Geo_box"][3]:
                    happiness = add_happiness(happiness, state_boxes[state2]["Abbrev"], current_score)
                    continue
        elif "user" in temp_json_line.keys():

            if not temp_json_line["user"]["location"] == "":
                user_location += 1
                loc = regex.findall(temp_json_line["user"]["location"].encode('utf-8').strip())
                if len(loc) > 0:
                    happiness = add_happiness(happiness, loc[0].upper(), current_score)
        total += 1

    # print "Place:", place
    # print "Coordinates:", coord
    # print "User Location:", user_location
    # print "Deleted:", delete
    # print "Total Records:", total
    # print "Geo:", geo
    current_highest = -1000000000000
    current_state = None
    for each in happiness.items():
        if each[1][0]/float(each[1][1]) > current_highest:
            current_highest = each[1][0]/float(each[1][1])
            current_state = each[0]
    print current_state
    print current_highest
    return happiness

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    find_happy(sent_file, tweet_file)

if __name__ == '__main__':
    main()
