# PCBS-Old_Press_Article_Classification
In this project, word2vec is used to classify press articles from a newspaper according to their subjects.

The aim of this project is to analyse old press articles. The database is the newspaper "Le Matin". This newspaper was published in Normandy since the 80s. It was recently digitized so jason files are available with the titles of articles and their contents. 

At the moment, it is easy to make a research with a date but there is no tool for a research with a subject. In fact, it could be interesting to see evolution of a subject across years or to have all informations about a particular event.

In this project, a part of the database will be used to try to classify articles according to their subjects. In a frist part, articles will be cleaned in order to correct mistakes added during the digitization. In a second part, the database will be analysed to know how much and which subjects we will be looking for. In a last part, word2vec will be used to classify articles according to the subjects found. 

Word2vec transforms words into vectors and projects them into a vector space. This projection allows words that have a common sense to be brought together by a statistical distance. This method is based on two-layer artificial neural networks trained to reconstruct the linguistic context of words. This method is carried out in two stages. The first step is to read the text and transform it in a vector. In a second step, the context of the world is taken into account, that is to say the 5 to 10 words around and then the value is added to the vector representing the word. Thus, dimensions can be identified where the vectors which have a close statistical distance are grouped, that is to say used in a same context.

To implement this project, python3 will be used. To execute the code, nltk, gensim and sklear need to be installed with the following command in a terminal :

```
pip -U install nltk
pip -U install gensim
pip -U install scikit-learn
```

If there is a problem, the documentation can be checked here :

https://www.nltk.org/install.html
https://pypi.org/project/gensim/
https://scikit-learn.org/stable/install.html

As "Le Matin" is a daily newspaper (available here : https://gallica.bnf.fr/ark:/12148/cb328123058/date), one year of copies are enought to complete this project. Thus, the databse can be dowloaded from the zip file 1884.zip (the first year of publication was selected). Then, the folder needs to be unziped to use it.

In these files, there are lot of mistakes due to the digitization. So the major part of unwanted characters can be removed with the program "cleaning.py". If the user wants to directly use cleaned files, they are available in the folder "cleaned_files". When we will be analysing the results at the end of the project, we will have to keep in mind that there still are mistakes in the files so it can affect the results.

One of the major part of this project consists in analyzing the database in order to clean it, as it was mentionned above, and to find the themes that we will be looking for. In fact, after reading around two hundred articles, twenty two main themes were identified : 
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

The program "w2v.py" analyzes the data, that is to say the articles used as input, and draws a map. This map represents the articles in differents colors. Each color corresponds to a different theme. The numbers in the colored circle enables to identify the articles. We want to have stable results, that is to say the same articles grouped together at each trial. The color is not important because it can change, the important point is that is the numbers 5, 11, 15 and 23 are grouped together, they have to be grouped together at each trial, no matter the color. 

## Results
We made different tests before finding the optimal parameters. During the first tests, the group were most of the time different at each trial so the results were not interesting. We modified the number of iterations and the window to 10. The results were quite similar from one trial to another. In order to improve the results, we tried to increase the size of the input data. With two days, we had good results : the shape of the projection was the same at each trial and the groups were more similar.
![Example of results for a two days classification](https://github.com/marionsch/PCBS-Old_Press_Article_Classification/blob/master/Example_Results.png)

## Future prospects
To finalize this project, it could be interesting to develop an other tool to display the results. In fact, more data improve the results but we can't visualize them clearly with the tool used here. 
An other point is the identification of each cluster. At the moment, we separate the articles into different clusters corresponding to the themes but we did not associate a cluster with a theme. To do that, some trails seem to appear. For example, we can identify some keywords for each theme and calculate the frequency of these words in the articles inside a cluster. 

## Personal aspects of the project
Before this project, I already programed few other ones but it was the first time I used word2vec. I also understood that it is really important to prepare the data used for a project. In fact, I spent lot of time reading articles to classify them and cleaning articles to use them even if it is not the aim of the project. 
