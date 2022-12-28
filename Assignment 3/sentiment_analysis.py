def tweet_format(line):  # formatter for tweets file
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    tweet = line.strip().split()  # to make sure there is no trailing space as well as a default space
    for i in range(0, 2):  # loop that formats only the coordinates of tweets
        tweet[i] = tweet[i].strip("[,]")  # removes the punctuation
    tweet[0] = float(tweet[0])
    tweet[1] = float(tweet[1])  # gets rid of the brackets and ","
    for i in range(2, len(tweet)):  # loop that formats after coordinates
        tweet[i] = tweet[i].strip(punctuation).lower()  # making everything lowercase
    return tweet


def key_value_format(line):  # formatter for keywords file
    key_word_value = line.strip().split(",")  # to make sure there is no trailing space as well as a separator at ","
    return key_word_value


def score_calculator(tweet, key_word_value):
    score = 0
    keyword_discovered = 0
    for i in range(5, len(tweet)):  # Loop that excludes everything before tweets
        if tweet[i] in key_word_value and tweet[i].isalpha():  # Check to see if the word is in keywords but also not a number
            keywordindex = key_word_value.index(tweet[i])  # finds the index of the keyword from list
            score += int(key_word_value[keywordindex + 1])  # the value is the next index after where keyword is indexed
            keyword_discovered += 1
    if score == 0:
        return 0
    else:
        return score / keyword_discovered


def region_set(tweet):  # Setting the region for the tweets

    p1 = [49.189787, -67.444574]  # Index 0 = lat, 1 = long
    p3 = [49.189787, -87.518395]
    p5 = [49.189787, -101.998892]
    p7 = [49.189787, -115.236428]
    p9 = [49.189787, -125.242264]
    p2 = [24.660845, -67.444574]
    p4 = [24.660845, -87.518395]
    p6 = [24.660845, -101.998892]
    p8 = [24.660845, -115.236428]
    p10 = [24.660845, -125.242264]

    region = ""
    # Check if the tweet is in a timezone
    if 49.189787 >= tweet[0] >= 24.660845 and -67.444574 >= tweet[1] >= -125.242264:
        if p1[1] >= tweet[1] > p3[1]:  # this checks if the longitudinal value is in [p1,p3]
            region = "Eastern"
        elif p3[1] >= tweet[1] > p5[1]:  # this checks if the longitudinal value is in [p3,p5]
            region = "Central"
        elif p5[1] >= tweet[1] > p7[1]:  # this checks if the longitudinal value is in [p5,p7]
            region = "Mountain"
        elif p7[1] >= tweet[1] >= p9[1]:  # this checks if the longitudinal value is in [p7,p9]
            region = "Pacific"
    return region


def compute_tweets(tweets_file, keywords_file):
    # counts how many keywords per region
    eastern_keyword = 0
    central_keyword = 0
    mountain_keyword = 0
    pacific_keyword = 0
    # counts how many tweets per region
    eastern_tweets = 0
    central_tweets = 0
    mountain_tweets = 0
    pacific_tweets = 0
    # counts score per region
    eastern_score = 0
    central_score = 0
    mountain_score = 0
    pacific_score = 0
    key_word_value = []
    try:
        tweets = open(tweets_file, "r", encoding="utf-8")  # no.5 of the functional specification requirement
        keywords = open(keywords_file, "r", encoding="utf-8")
        for line in keywords:  # Reading the keyword file
            for index in key_value_format(line):
                key_word_value.append(index)
        for line in tweets:  # reading the tweet file
            tweet = tweet_format(line)
            region = region_set(tweet)
            if region == "Eastern":  # where all the counting happens for each region
                eastern_tweets += 1
                if score_calculator(tweet, key_word_value) != 0:
                    eastern_keyword += 1
                    eastern_score += score_calculator(tweet, key_word_value)
            elif region == "Central":
                central_tweets += 1
                if score_calculator(tweet, key_word_value) != 0:
                    central_keyword += 1
                    central_score += score_calculator(tweet, key_word_value)
            elif region == "Mountain":
                mountain_tweets += 1
                if score_calculator(tweet, key_word_value) != 0:
                    mountain_keyword += 1
                    mountain_score += score_calculator(tweet, key_word_value)
            elif region == "Pacific":
                pacific_tweets += 1
                if score_calculator(tweet, key_word_value) != 0:
                    pacific_keyword += 1
                    pacific_score += score_calculator(tweet, key_word_value)
        if eastern_keyword != 0:
            eastern_score /= eastern_keyword
        if central_keyword != 0:
            central_score /= central_keyword
        if mountain_keyword != 0:
            mountain_score /= mountain_keyword
        if pacific_keyword != 0:
            pacific_score /= pacific_keyword
        result_list = [(eastern_score, eastern_keyword, eastern_tweets),
                       (central_score, central_keyword, central_tweets),
                       (mountain_score, mountain_keyword, mountain_tweets),
                       (pacific_score, pacific_keyword, pacific_tweets)]
        tweets.close()
        keywords.close()
        return result_list
    except FileNotFoundError:
        print("File not found")
        return [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
