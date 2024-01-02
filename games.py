'''Creates a chatbot using NLTK that will ask the user for video game preference
and suggest recommended titles to try. Meet Steambot!'''

# import libraries needed for chatbot
import random
import string
import warnings
import pandas as pd
# convert a collection of text documents to a vector of token counts
from sklearn.feature_extraction.text import CountVectorizer
# this function finds similarity between user words and words in corpus
from sklearn.metrics.pairwise import cosine_similarity
# error handling, filters warning messages
warnings.filterwarnings('ignore')

# opens corpus file
file = pd.read_csv("steam.csv")
#converts title names to lowercase for easy comparison to user input
file['title'] = file['title'].str.lower()
# features used for comparison in the csv file
features = ['categories', 'publisher', 'genres', 'developer']

# replaces rows in data that contain NaN values with an empty string
for feature in features:
    file[feature] = file[feature].fillna('')

def combined_features(row):
    '''combines features we wish to use for comparison into a single string'''
    return row['categories'] + " " + row['publisher'] + " " + row['genres'] + " " + row['publisher']

def get_game_index(title):
    '''gets index value for title from file variable'''
    return file[file.title == title]['index'].values[0]-1


def get_title(index):
    '''gets the game title based on index value'''
    return("Steambot: Based on the game you provided, I recommend trying " +
            f"\"{file[file.index == index]['title'].values[0]}.\"\n"
            f"Steambot: The game is published by {file[file.index == index]['publisher'].values[0]}"
            f" and developed by {file[file.index == index]['publisher'].values[0]}.\n"
            f"Steambot: Fans of the \"{file[file.index == index]['genres'].values[0]}\" " +
            "genre typically enjoy this game.")

def greeting(sentence):
    '''Looks for a common greeting within user input and outputs a greeting in return.'''
    for word in sentence.translate(remove_punctuation).split():
        if word.lower() in GREETINGS:
            #returns random greeting from pool of greetings
            bot_greeting = random.choice(GREETINGS)
        return bot_greeting

def search_count(user_game):
    '''counts the number of times the user has searched'''
    if user_game not in prev_user_input:
        prev_user_input[user_input] = 0
    elif user_input in prev_user_input:
        prev_user_input[user_input] += 1
    return prev_user_input[user_input]

# creates a variable to store punctuation
remove_punctuation = dict((ord(punct), None) for punct in string.punctuation)
# variable to store common greetings
GREETINGS = ('hey', 'hi', 'howdy', 'hello', 'what\'s up', 'sup', 'yo')
# variable to store thank you responses from user
THANKS = ("thank you", "thanks", "thx", "thnx")
# variable to store thank you phrases
THANKS_RESPONSE = ("You're welcome!", "My pleasure!", "Happy to help!", "No problem!")

# adds all of the features from combined_features function to a column in the file variable
file['combined_features'] = file.apply(combined_features, axis = 1)

vectorizer = CountVectorizer()
count_vector = vectorizer.fit_transform(file['combined_features'])

# informs user that program is running - csv is large and takes ~30sec to load
print('Loading database... Please wait. Loading may take around 30 seconds.')

# computes similarity between games in the database
similarity_idx = cosine_similarity(count_vector)

# chatbot introduces itsself and welcomes user
print('Steambot: My name is Steambot. I can help recommend games to play on PC ' +
      'through Steam. \nSteambot: You can provide a game that you enjoy and I will recommend a ' +
      'title that is similar.\nSteambot: If you want to exit, type "bye"!')

#creates a variable to store the last user input and the count
prev_user_input = {}

# creates a boolean variable to keep the chat loop going until 'bye' is typed by user
CHAT = True
while CHAT is True:
    # asks user for a game to suggest other titles that the user may enjoy
    user_input = input(">>")
    # converts user input into lowercase
    user_input = user_input.lower()
    # checks if user wishes to exit program
    if 'bye' not in user_input:
        # prints thank you statement if user thanks Steambot
        if user_input.translate(remove_punctuation) in THANKS:
            print("Steambot: " + random.choice(THANKS_RESPONSE))
        else:
            try:
                # gets the game index of game input by user
                game_index = get_game_index(user_input.lower())
                # gets index of similar games
                similar_games = list(enumerate(similarity_idx[game_index]))
                # sorts similar games (by index) in descending order
                sorted_similar_games = sorted(similar_games, key=lambda x:x[1], reverse=True)
                num_searches = search_count(user_input)
                # displays most relevant results (first result in sorted list is input title)
                if num_searches < 5:
                    print(get_title(sorted_similar_games[num_searches+1][0]))
                # after searching same title 5 times, Steambot recommends user provide a new title
                else:
                    print("Steambot: Sorry you don't like my recommendations! "
                          "Try providing another title.")
            # catches index error if input isn't found on the corpus file
            except IndexError:
                print("Steambot: I couldn't find the title you mentioned. "
                      "Please check the spelling.\n" +
                      "Steambot: If spelling is correct, I may not have this title in my database.")
            except KeyboardInterrupt:
                CHAT = False
    #exits loop and program when user types 'bye'
    else:
        CHAT = False
        print("Steambot: Goodbye and have a great day!")
