# PCBS-Old_Press_Article_Classification
In this project, word2vec is used to classify press articles from a newspaper according to their subjects

The aim of this project is to analyse old press articles. The database is the newspaper "Le Matin". This newspaper was published in Normandy since the 80s. It was recently digitized so jason files are available with the titles of articles and their contents. 

At the moment, it is easy to make a research with a date but there is no tool for a research with a subject. In fact, it could be interesting to see evolution of a subject across years or to have all informations about a particular event.

In this project, a part of the database will be used to try to classify articles according to their subjects. In a frist part, articles will be cleaned in order to correct mistakes added during the digitization. In a second part, the database will be analysed to know how much and which subjects we will be looking for. In a last part, word2vect will be used to classify articles according to the subjects found. 

To implement this project, python3 will be used. To execute the code, nltk, gensim and sklear need to be installed with the following command in a terminal :
### pip -U install nltk
### pip -U install gensim
### pip -U install scikit-learn
If there is a problem, the documentation can be checked here :

https://www.nltk.org/install.html

https://pypi.org/project/gensim/

https://scikit-learn.org/stable/install.html

As "Le Matin" is a daily newspaper (available here : https://gallica.bnf.fr/ark:/12148/cb328123058/date), one year of copies are enought to complete this project. Thus, the databse can be dowloaded from the zip file 1884.zip (the first year of publication was selected). Then, the folder need to be unziped to use it.

In these files, there are lot of mistakes due to the digitization. So unwanted characters can be removed with the program "cleaning.py". If the user wants to directly use cleaned files, they are available in the folder "cleaned_files". 

One of the major part of this project consists in analyzing the database in order to clean it, as it was mentionned above, and to find the themes that we will be looking for. In fact, after reading more than one hundred articles, twenty two main themes were identified : 
- news
- elections
- advertisements
- literature
- religion
- justice
- economy
- strikes
- politics
- satire
- divorces
- medicine
- stock exchange
- art
- meteorology
- war
- death notices
- sports
- education
- classifieds
- society column
- maritime column

It means that articles will be separated into 22 clusters relative to the 22 themes. Empty clusters are allowed beaucause it is not an obligation to have all themes into the sample of data used for each trial. 

The program "model.py" creates new files with several days to improve the classification's results. In fact, it could be interesting to have sample bigger than only one day. 

## Results

## Personal aspects of the project
Before this project, I already program few other ones but it was the first time I used word2vec.
