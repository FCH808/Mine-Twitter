Mine-Twitter
============

###Mines twitter data obtained from the twitter API for crude estimate overall sentiment.

Mines twitter data obtained from the twitter API for sentiment.

State geo boundry boxes are obtained from the sourced in function: find_state_boxes

Assigns overall sentiment score to tweet based on tab-delimited sentiment rating dictionary with [word    rating] passed in. e.g. [abandon	-2]

Geocodes, place coordinates, and location info entered are mined (in that order) to obtain U.S state location of tweet.

Tweets and ratings for each state are then aggregated and averaged, and the highest state/rating is printed to stdout.

A dictionary is also returned containing total ratings and count of tweets that went into that total.

