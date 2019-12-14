# PCBS-Old_Press_Article_Classification
In this project, word2vec is used to classify press articles from a newspaper according to their subjects

The aim of this project is to analyse on old press articles. The database is the newspaper "Le Matin". This newspaper was published in Normandy since the 80s. This newspaper was recently digitized so jason files are available with the titles of articles and their contents. 

At the moment, it is easy to make a research with a date but there is no tool for a research with a subject. In fact, it could be interesting to see evolution of a subject across years or to have all informations about a particular event.

In this project, a part of the database will be used to try to classify articles according to their subjects. In a frist part, articles will be clean in order to correct mistakes added during the digitization. In a second part, the database will be analyse to know how much and which subjects we will be looking for. In a last part, word2vect will be used to classify articles according to the subjects found. 

To implement this project, python3 will be used. To execute the code, nltk, gensim and sklear need to be installed with the following command in a terminal :
### pip -U install nltk
### pip -U install gensim
### pip -U install scikit-learn

As "Le Matin" is a daily newspaper, one year of copies are enought to complete this project. Thus, the databse can be dowloaded from the zip file 1884.zip (the first year of publication was selected). Then, unzip the folder to use it.

In these files, there are lot of mistakes due to the digitization. So unwanted characters can be removed with the program "cleaning.py". If the user wants to directly use cleaned files, they are available in the folder "cleaned_files". 

The program analyzing the newspaper is "w2v.py". The data to analyze are chosen inside the file and the results are the articles classified in different clusters according to their subjects.

Finally, the program "model.py" creates new files with several days to improve the classification's results.
