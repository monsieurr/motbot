import os
import tweepy
from os.path import join, dirname
from dotenv import load_dotenv
import random
import words as wd
import color as clr

# Global variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
# API Authentication


def connect_to_twitter_simple():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY,
                               CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")


# Functions to send a tweet automatically given the arguments


def send_tweet(api, topic):
    twitter_text = "My message " + topic
    api.update_status(status="{}".format(twitter_text))  # send a tweet
    print("TWEET SENT")


def send_tweet_with_media(api, topic, media):
    twitter_text = "test"
    media = api.media_upload("test.png")


    print("screen to be uploaded : " + str(media))
    print("The size of the file is : " + str(media.size) + " bytes")

    print(type(media))
    media_id = media.media_id_string
    api.update_status(topic, media_ids=[media_id])

    # printing the information
    #api.update_status(topic, media_ids=[medias_id[0], medias_id[1], medias_id[2], medias_id[3]])


def select_image():
    choice = "test.png"  # change dir name to whatever
    print(choice)
    return choice



def remove_image(choice):
    try:
        os.remove(choice)
        print("file has been removed")
        return True
    except:
        print("Error while trying to remove the current image")


# Main functions
if __name__ == "__main__":
    randomnb = random.randint(0, 1000)
    api = connect_to_twitter_simple()
    select_random_function = random.randint(0, 2)


    random_color = clr.generate_random_color()
    quote = wd.select_quote("quotes.txt")
    quote = wd.capitalize_first_letter(quote)
    
    topic = quote+" [#"+str(randomnb)+"]"

    clr.generate_simple_art("test.png", random_color, quote)
    media = select_image()

    try:
        send_tweet_with_media(api, topic, media)
        #remove_image(media)
        #send_tweet(api, topic)
        print("DONE")
    except tweepy.TweepError as e:
        print("ERROR WHILE SENDING THE TWEET : " + str(e))
