import json
import sys
import collections
#import pprint

#tweet_file = open("output_all.txt")

def find_top_ten(tweet_file):
    hashtags_dict = {}
    for line in tweet_file.readlines():
        json_line = json.loads(line, encoding='utf-8')
        if "delete" in json_line.keys():
            continue
        if not json_line['entities']['hashtags'] == []:
            for hashtag in json_line['entities']['hashtags']:
                if hashtag['text'].encode('utf-8').strip() not in hashtags_dict.keys():
                    hashtags_dict[hashtag['text'].encode('utf-8').strip()] = 1
                else:
                    hashtags_dict[hashtag['text'].encode('utf-8').strip()] += 1
    for top_ten in collections.Counter(hashtags_dict).most_common(10):
        print top_ten[0], top_ten[1]

















def main():
    tweet_file = open(sys.argv[1])
    find_top_ten(tweet_file)


if __name__ == "__main__":
    main()