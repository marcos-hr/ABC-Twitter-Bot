import tweepy
import time
import unidecode
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("spanish")

consumer_key = 'eV1jyPZ8jWMmtOil9paHnsV0Q'
consumer_secret = 'CWh7fRm7eDOOd3lMaKucN0vgCTOUk7tZvptRppmH59ZcLkn2hd'

access_token = '1036225992979824641-KHhGeOmHWkNbaXWD2oOkBivExNZU0t'
access_token_secret = 'l8a8QrjCINZGuFfH6qK58sv7pGQpCooIqLSr48sbOYT4G'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print (user.name + " | " + str(user.id))

def main():
    print("inicio")


    count = 1
    with open('most-common-spanish-words.txt') as f:
        file = f.readlines()

    for i in range(len(file)):
        file[i] = unidecode.unidecode(file[i].strip().split("|", 1)[0])

    file = list(set(file))
    file = sorted(file, key=str.lower)

    last_root = ""
    count = 1
    for i in range(len(file)):

        if last_root != stemmer.stem(file[i]):
            print (file[i])
            f=open("nuevo.txt", "a+")
            f.write(file[i] + "\n")
            count += 1

        last_root = stemmer.stem(file[i])

main()

EL AUTOFOLLOWER