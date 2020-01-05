# Marion Schaeffer
# Cogmaster 1
# sch-marion@hotmail.com
# Janvier 2020

import nltk
from gensim.models import Word2Vec
from nltk.cluster import KMeansClusterer 
import numpy as np 
from sklearn import cluster
from sklearn import metrics

# ----------DECOUPE--ARTICLE-----------------------------------

def nettoie_titre(titre):
    """Fonction qui nettoie un titre
    
    Tous les caracteres autres qu'une majuscule, 
    un point ou un espace sont supprimes
    
    Args:
        titre : un titre d'article
        
    Returns:
        le titre nettoye
        
    """
    for i in titre:
        if (not(i.isupper()) and not(i=='.') and not(i==' ')):
            titre=titre.replace(i, '')
    return titre


def titres(corpus):
    """Fonction qui retourne une liste d articles
    
    Cette fonction enregistre toutes les positions des titres d'articles, 
    on connait donc la position de tous les articles.
	Pour ce faire, on a remarque que les titres sont de la forme
	'\nTITRE EN MAJUSCULES\n'
    
    Args:
        corpus : le texte complet corrigé mais non decoupe
        
    Returns:
        une liste de liste, cette derniere comprend le titre nettoye, 
        sa position de début et sa position de fin.
        On peut donc connaitre la position de chaque article 
        (de la fin du titre au debut du titre suivant)
        
    """
    i = 0
    j = 0
    articles = []
    a1=[]
    nbArticles=0
    
    while (i<len(reader)):
        if ((reader[i] == "\\") and (reader[i+1]=="n")):
            j = i+2
            while (not(reader[j].islower()) and (not((reader[j] == '\\') and (reader[j+1]=='n')))):         
                j=j+1         
            if ((reader[j] =='\\') and (reader[j+1] == 'n')):
    
    #--------ENREGISTREMENT-TITRE-ET-POSITION--------
                a1 = [nettoie_titre(reader[i+2:j]), i+2, j]
                nbArticles = nbArticles + 1
                articles.append(a1)
                a1=[]
                i=j+2
            else: i = j+1    
        else: i=i+1
    return articles

def mot(article): 
    """Fonction qui decoupe un texte en liste de mots
    
    Une longue chaine de caracteres est decoupee en liste de mots.
    Le critere de separation est un espace entre chaque suite de chaine de caracteres.
    
    Args:
        article : un texte non decoupe
        
    Returns:
        une liste de mots
        
    """
    m = article.split(' ')
    return m

def corpus2list (corpus): 
    """Fonction qui decoupe un texte en liste d'articles
    
    Le corpus est decoupe en articles grace a la position des titres.
	Les articles sont decoupes en liste de mots.
    
    Args:
        corpus : un texte non decoupe
        
    Returns:
        une liste d'article ou chaque article est une liste de mots
        
    """
    res =[]
    i = 0
    j = 0
    articles = titres(corpus) 
    while i < len(articles): 
        if (i == len(articles) -1): art = corpus[articles[i][2]+2:]
        else : art = corpus[articles[i][2]+2:articles[i+1][1]-2]
        i =i+1 
        m = mot(art) 
        res.append(m)
    return res
   
# ----------CHARGEMENT--DU--JOURNAL----------------------------- 
    
jour = '26'
mois = '02'
annee = '1884'
date=annee+mois+jour
# journal non corrige
# file = annee + '/' + date + '/' + date + '.metadata.fulltext.json'
# journal corrige 
file = 'cleaned_files/' + date + '.txt'

f  = open(file,"r", encoding='utf-8')
reader = f.readline()
# transformation en liste d'articles = liste de liste de mots
articles = corpus2list(reader)

# ----------APPRENTISSAGE--AVEC--WORD2VEC------------------------

# Parametres:
# iter 		: nombre de tours d'apprentissage
# window 	: nombre de voisins pris en compte
# min_count 	: nombre de fois que doit apparaitre chaque mot pour être pris en compte

model = Word2Vec(articles,min_count=1, iter=10, window=10)

def sent_vectorizer(sent, model):
    """Fonction qui calcule le vecteur representant chaque article
    
    Chaque mot est transforme en vecteur grace au modele.
	Le resultat est pondere par le nombre de mots.
    
    Args:
        sent : article a tranforme en vecteur
        model : modele utilise par word2vec pour transformer les mots en vecteur
        
    Returns:
        le vecteur calcule
        
    """
    sent_vec =[]
    numw = 0
    for w in sent:
        try:
            if numw == 0:
                sent_vec = model[w]
            else:
                sent_vec = np.add(sent_vec, model[w])
            numw+=1
        except:
            pass
    return np.asarray(sent_vec) / numw 
    
X = []
for article in articles:
    X.append(sent_vectorizer(article, model))   

# nombre de mots etudies
print (len(list(model.wv.vocab)))
 
# nombre de cluster a choisir = nombre de themes differents souhaites
NUM_CLUSTERS=22
kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25, avoid_empty_clusters=False)
assigned_clusters = kclusterer.cluster(X, assign_clusters=True)

for index, article in enumerate(articles):    
    print ('Cluster ' + str(assigned_clusters[index]) + " :" + ' Article ' + str(index))
 
 
kmeans = cluster.KMeans(n_clusters=NUM_CLUSTERS)
kmeans.fit(X)
 
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# ------------------AFFICHAGE--------------------------------

import matplotlib.pyplot as plt
 
from sklearn.manifold import TSNE
 
model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
 
Y=model.fit_transform(X)
 
 
plt.scatter(Y[:, 0], Y[:, 1], c=assigned_clusters, s=290,alpha=.5)
 
 
for j in range(len(articles)):    
   plt.annotate(j,xy=(Y[j][0], Y[j][1]),xytext=(0,0),textcoords='offset points') 
 
plt.show()
