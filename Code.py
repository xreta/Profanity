import string

def calculate_profanity(tweet, racial_slurs):
    return sum(1 for word in tweet.split() if word in racial_slurs)

def main():
    with open("tweets.txt") as file:
        tweets = file.readlines()

    racial_slurs = ["nigger", "fag", "kike", "spic", "wetback", "chink", "gook", "jap"]
    remove_punctuation = str.maketrans("", "", string.punctuation)

    for tweet in tweets:
        tweet = tweet.strip().translate(remove_punctuation).lower()
        profanity_degree = calculate_profanity(tweet, racial_slurs)
        print(f"The profanity degree for tweet '{tweet}' is: {profanity_degree}")

if __name__ == "__main__":
    main()
