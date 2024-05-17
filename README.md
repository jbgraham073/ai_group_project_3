# ai_group_project_3
AI Bootcamp | Group Project 3

MuSE: The Musical Sentiment Dataset (found on [Kaggle](https://www.kaggle.com/datasets/cakiki/muse-the-musical-sentiment-dataset)
The process of producting this dataset is described in the paper [Toward a Musical Sentiment (MuSe) Dataset for Affective Distant Hearing](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://ceur-ws.org/Vol-2723/short26.pdf), which was presented at the CHR 2020 workshop on Computational Humanities Research.

In summary, the authors of this dataset carried out a multi-stage process to create a comprehensive dataset of songs mapped to the dimensions of valence, arousal, and dominance. It began by collecting mood labels from Allmusic.com as seed terms, then expanded by gathering user-generated tags from Last.fm for songs associated with those moods. Through filtering, they identified which tags corresponded to affective concepts using WordNet-Affect. The remaining mood tags were then mapped to valence, arousal, and dominance scores using ratings from Warriner et al's crowdsourced lexicon. Additional metadata like artist, genre, and Spotify audio features were appended by cross-referencing with the Spotify API. The resulting dataset contains around 90,000 songs characterized by mood tags dimensionally mapped to the VAD space, along with supplemental metadata facilitating further analysis of relationships between emotions, genres, and acoustic qualities.
