# Marion Schaeffer
# Cogmaster 1
# sch-marion@hotmail.com
# Décembre 2019

import nltk
from gensim.models import Word2Vec
from nltk.cluster import KMeansClusterer 
import numpy as np 
from sklearn import cluster
from sklearn import metrics

# ----------DECOUPE--ARTICLE-----------------------------------

# nettoie un titre donne
def nettoie_titre(titre):
    for i in titre:
        if (not(i.isupper()) and not(i=='.') and not(i==' ')):
            titre=titre.replace(i, '')
    return titre

# retourne une liste d'articles
def titres(corpus):

    # initialisation de la position du curseur
    i = 0
    j = 0
    
    # initialisation des resultats
    articles = []
    a1=[]
    nbArticles=0
    
    # parcours du fichier
    while (i<len(reader)):
       
    # on attend d'avoir un '\n'
        if ((reader[i] == "\\") and (reader[i+1]=="n")):
    # on sauvegarde la position juste apres le '\n'
            j = i+2
    # tant qu'il n'y a pas de minuscules ni de '\n' on est toujours dans le titre
            while (not(reader[j].islower()) and (not((reader[j] == '\\') and (reader[j+1]=='n')))):         
                j=j+1        
    # si on sort de la boucle parce il y a un '\n' on a un titre   
            if ((reader[j] =='\\') and (reader[j+1] == 'n')):
    
    #--------ENREGISTREMENT-TITRE-ET-POSITION--------
                a1 = [nettoie_titre(reader[i+2:j]), i+2, j]
                nbArticles = nbArticles + 1
                articles.append(a1)
                a1=[]
                i=j+2
    # si on sort de la boucle parce qu'il y a une minuscule, on recommence juste apres celle-ci
            else: i = j+1
    # si il y a pas de '\n' on continue a parcourir le fichier    
        else: i=i+1
    return articles

# renvoie une liste de mot
def mot(article): 
    m = article.split(' ')
    return m

# renvoie une liste(liste(mot))
def corpus2list (corpus): 
    res =[]
    i = 0
    j = 0
    # tout le corpus est separe en articles
    articles = titres(corpus) 
    while i < len(articles): 
        res_article = []
        if (i == len(articles) -1): art = corpus[articles[i][2]+2:]
        else : art = corpus[articles[i][2]+2:articles[i+1][1]-2]
        i =i+1
        m = mot(art) 
        res.append(m)
    return res
   
# ----------CHARGEMENT--DU--JOURNAL----------------------------- 
    
# date du journal que l'on souhaite ouvrir
jour = '26'
mois = '02'
annee = '1884'
date=annee+mois+jour
# journal non corrige
file = annee + '/' + date + '/' + date + '.metadata.fulltext.json'
# journal corrige 
file = 'fichiers_clean/' + date + '.txt'

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

# calcule le vecteur de chaque article en sommant les vecteurs de mot de l'article et divisant par le nombre de mots
def sent_vectorizer(sent, model):
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
NUM_CLUSTERS=23
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
