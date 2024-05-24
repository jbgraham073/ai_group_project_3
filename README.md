# ai_group_project_3
AI Bootcamp | Group Project 3

Our innovative product analyzes the current sentiment of popular song lyrics and offers a unique feature to rewrite the lyrics to match a sentiment of the user's choice. By leveraging advanced natural language processing and sentiment analysis, users can transform any song to reflect their desired mood, creating a personalized and dynamic musical experience.

## Problem Statement

Many music enthusiasts enjoy songs but wish the lyrics better matched their current mood or desired emotional state. However, manually rewriting lyrics to reflect a different sentiment is time-consuming and requires creative skill, leaving many listeners unable to fully personalize their musical experiences.

## 🔑 Key Features

1. Sentiment Analysis: Utilizes advanced natural language processing to accurately assess the current sentiment of popular song lyrics, providing a detailed emotional profile.
2. Sentiment Customization: Allows users to select their desired sentiment (e.g., happy, sad, energetic, calm) and automatically rewrites the song lyrics to reflect this chosen mood.
3. User-Friendly Interface: Offers an intuitive and interactive platform where users can easily input song lyrics, select their preferred sentiment, and receive personalized, sentiment-adjusted lyrics in real-time.

## Process 

* Milestone 1 - Ideate & select project
* Milestone 2 - Identify Data sources
* Milestone 3 - Clean data
* Milestone 4 - Identify/Build and train/Test models necessary for sentiment analysis of songs
    * BERT
    * VADER
* Milestone 5 - Rewrite lyrics for selected song to be a different sentiment than what it currently is
    * ChatGPT API rewrites lyrics for new sentiment 
* Milestone 6 - Build interface for User to input song for sentiment analysis and to request lyrics be rewritten
* Milestone 7 - Presentation

### 💰 Success Criteria

Sentiment Accuracy:

* Metric: Accuracy of sentiment analysis and user satisfaction with rewritten lyrics.
* Measurement: Evaluate the accuracy of sentiment analysis algorithms by comparing predicted sentiments with user-reported sentiments and analyzing feedback on the accuracy of the rewritten lyrics.

UI is functional 

* Metric: UI is functional & intuitive to use 
* Measurement: User intuitively knows how to operate system and system functions as expected 

## BERT Modeling 
[...yada yada using the MuSE dataset from Kaggle...yada yada]

### MuSE: The Musical Sentiment Dataset (found on [Kaggle](https://www.kaggle.com/datasets/cakiki/muse-the-musical-sentiment-dataset))

The process of producing this dataset is described in the paper [Toward a Musical Sentiment (MuSe) Dataset for Affective Distant Hearing](https://www.academia.edu/75793892/Toward_a_Musical_Sentiment_MuSe_Dataset_for_Affective_Distant_Hearing), which was presented at the CHR 2020 workshop on Computational Humanities Research.
In summary, to create this dataset, the authors carried out a multi-stage process to create a comprehensive register of songs mapped to the dimensions of valence, arousal, and dominance. They began by collecting mood labels from Allmusic.com as seed terms, then gathered user-generated tags from Last.fm for songs associated with those moods. Through filtering, they identified which tags corresponded to affective concepts using WordNet-Affect. The remaining mood tags were then mapped to valence, arousal, and dominance scores using ratings from Warriner et al's crowdsourced lexicon. Additional metadata like artist, genre, and Spotify audio features were appended by cross-referencing with the Spotify API. The resulting dataset contained around 90,000 songs characterized by mood tags dimensionally mapped to the VAD space, along with supplemental metadata facilitating further analysis of relationships between emotions, genres, and acoustic qualities.

## Initializing VADER: Valence Aware Dictionary and sEntiment Reasoner 
Vader sentiment analysis is used to capture the overall sentiment in bodies of text. It looks at words and phrases to determine if they're expressing positive, negative, compound, or neutral sentiment. Businesses use Vader sentiment analysis to understand how customers feel about their products or services to gauge customer satisfaction, identify issues, and improve their offerings. VADER excels at capturing nuances of slang, emojis, and even grammatical errors, therefore it's well suited to perform sentiment analysis on song lyrics. 
For Moodify Lyrix: 
Stage 1: Identify the sentiment of user chosen song lyrics
Stage 2: Enable the user to change the sentiment to match their mood using the Gradio interface, then perform a VADER sentiment analysis to the result. 


## Gradio Integration
[...yada]

## User Guidelines 
[...add guidelines]

[link to deck]


