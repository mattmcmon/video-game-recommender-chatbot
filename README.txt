Matt McMonagle - Chatbot Final Project

Goal:
    To create a functional chatbot that recommends PC games on Steam (application) based on a title. 
    The chatbot will offer suggestions if the same game is provided (up to 5 times),
    If the same game is provided more than 5 times, the chatbot will ask the user to rephrase the question. 
    The chatbot will also respond to gratitude and greetings.

Design:
    The base of my chatbot was built around the article from Towards Data Science: https://towardsdatascience.com/using-cosine-similarity-to-build-a-movie-recommendation-system-ae7f20842599 
    I repurposed my project to recommend video games, rather than movies. Variables were renamed to be more descriptive and I added comments for easier readability.
    I found a very extensive CSV file from Kaggle.com that includes over 27,000 steam games.
    I also added functionality for the chatbot to provide alternative answers when the same game was provided by the user. 
    Responses to "thank you's" were also added and the program will exit when the user types "bye."

Limitations and Future Work:
    Because I had no prior experience with Machine Learning, the majority of my time was spent trying to understand the library and figuring out how to improve
    the base code. For future work, I would like to find/create a file that contains a synopsis of each game's story to give even more finely honed recommendations to the user.
    Also, adding functionality to allow the user to choose how they want to search (by genre, publisher, developer, etc) would be a useful feature to implement.

Usage:
    Install all the python libraries prior to running the chatbot program. To do this, navigate to the folder containing the steam.csv, games.py, requirements.txt,
    README.txt, and cahtbot_demo.mp4. Then, type the command below:

        pip install -r requirements.txt
    
    To run the program, type the line below into the terminal. Make sure that games.py, steam.csv, requirements.txt, and chatbot.mp4 are all in the same directory.
        
        python games.py

    This will launch the chatbot and then you can provide a game title and Steambot will recommend other titles to try.

    *NOTE: Because the CSV file contains over 27,000 games, it may take about 30 seconds to load the file.

Demo:

	See chatbot.mp4 file in the matt_mcmonagle_finalproj.zip folder for a video demo that walks through running the program, a brief overview of the code, and where the data
	was sourced from
    