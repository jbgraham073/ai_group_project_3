# ai_group_project_3
AI Bootcamp | Group Project 3

## Overview
This project provides a Gradio app where users can input a song's lyrics, understand its existing sentiment, and change the lyrics to match a new desired sentiment. The project includes multiple components such as data generation, model training, and a user-friendly interface built with Gradio. We used tools for analyzing and modifying the sentiment of song lyrics using advanced machine learning models, BERT and VADER. 

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

### MuSE: The Musical Sentiment Dataset (found on [Kaggle](https://www.kaggle.com/datasets/cakiki/muse-the-musical-sentiment-dataset))

The process of producing this dataset is described in the paper [Toward a Musical Sentiment (MuSe) Dataset for Affective Distant Hearing](https://www.academia.edu/75793892/Toward_a_Musical_Sentiment_MuSe_Dataset_for_Affective_Distant_Hearing), which was presented at the CHR 2020 workshop on Computational Humanities Research.
In summary, to create this dataset, the authors carried out a multi-stage process to create a comprehensive register of songs mapped to the dimensions of valence, arousal, and dominance. They began by collecting mood labels from Allmusic.com as seed terms, then gathered user-generated tags from Last.fm for songs associated with those moods. Through filtering, they identified which tags corresponded to affective concepts using WordNet-Affect. The remaining mood tags were then mapped to valence, arousal, and dominance scores using ratings from Warriner et al's crowdsourced lexicon. Additional metadata like artist, genre, and Spotify audio features were appended by cross-referencing with the Spotify API. The resulting dataset contained around 90,000 songs characterized by mood tags dimensionally mapped to the VAD space, along with supplemental metadata facilitating further analysis of relationships between emotions, genres, and acoustic qualities.

## Features
- **Sentiment Analysis**: Analyze the sentiment of song lyrics using BERT and VADER models.
- **Lyrics Modification**: Modify the sentiment of existing song lyrics to match a new mood.
- **User Interface**: Gradio app for easy interaction with the models.
  
## Files and Notebooks
### Python Scripts
- **vader.py**: Script for sentiment analysis using the VADER model.
- **lyrics_genius.py**: Script for fetching song lyrics using the Genius API.
- **gpt_sent_shift.py**: Script for shifting the sentiment of song lyrics using the GPT model.

### Notebooks
- **dataset_generation.ipynb**: Jupyter notebook for generating datasets of song lyrics and their sentiments.
- **model_inference.ipynb**: Notebook for running inference on song lyrics using trained models.
- **GPT_API.ipynb**: Notebook for interacting with the GPT API for sentiment modification.
- **bert_FINE_tune.ipynb**: Notebook for fine-tuning the BERT model on a custom dataset.
- **vader.ipynb**: Notebook for sentiment analysis using the VADER model.
- **gradio_playground.ipynb**: Notebook for developing and testing the Gradio user interface.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sentiment-song-lyrics-modifier.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    
## Usage
1. Run the data generation notebook to prepare your dataset.
2. Fine-tune the BERT model using the provided notebook.
3. Use the sentiment analysis and modification scripts to analyze and modify song lyrics.
4. Launch the Gradio app to interact with the models through a user-friendly interface.

## APIs
We executed APIs for: 
1. lyricsgenius.com
2. ChatGPT

## Issues: 
We were not able to upload the actual models to github due to their size (1.6gb) even as a zip file. 

## Acknowledgements
Special thanks to Matt Hergott, our awesome instructor. 




