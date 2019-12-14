# CONSTRUCTION D'UN FICHIER TEXTE COMPOSE DE PLUSIEURS ARTICLES

# premier texte du modele
jour = '26'
mois = '02'
annee = '1884'

# nombre d'articles utilises pour generer le modele
# taille minimum = 2 et taille maximum = 10
taille = 3

for i in range(taille):
	if (int(mois)<9): 
		mois='0'+str(int(mois)+1)
	else : 
		mois=str(int(mois)+1)
	date=annee+mois+jour
	# fichiers sources
	copie = 'fichiers_clean/'+date+'.txt'
	# fichier modele creer
	res = 'fichiers_clean/modele_'+str(taille)+'textes.txt'
	r  = open(res,"a")
	c = open(copie, "r")
	reader = c.readline()
	r.write(reader)
	r.close()
	c.close()

	
	
