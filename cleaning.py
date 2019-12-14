# Marion Schaeffer
# Cogmaster 1
# sch-marion@hotmail.com
# Décembre 2019

def clean (reader):
    """ Fonction qui nettoie un texte
    
    Cette fonction enleve les caracteres autres que chiffres, lettres minuscules, 
    lettres majuscules, lettres accentuees et ponctuation classique.
    
    Args: 
        reader : le texte a modifier
        
    Returns:
        le texte nettoye c est a dire sans les caracteres indesirables
    
    """
    text = ''
    for car in reader:
        if ((ord(car) >= 46 and ord(car) <= 122) or (ord(car) == 32) or (ord(car) == 44) or (ord(car) == 39) or (ord(car) == 233) or (ord(car) == 232) or (ord(car) == 224) or (ord(car) == 249) or (ord(car) == 238) or (ord(car) == 234)):
            text = text + car
    return text


""" NETTOIE TOUTE L'ANNEE 1884 ET RECREER UNE BASE DE DONNEES
 Fichier source : 1884
 Fichier destination : cleaned_files"""

# initialisation de la date
jour = '26'
mois = '02'
annee = '1884'


while((int(mois)<13) and (int(jour)<32)):
	date=annee+mois+jour
	# fichier source
	file = annee+'/'+date+'/'+date+'.metadata.fulltext.json'
	# fichier nettoye
	copie = 'cleaned_files/'+date+'.txt'
	f  = open(file,"r")
	c = open(copie, "a")
	reader = f.readline()
	text = ''
	c.write(clean(reader))
	f.close();
	c.close();

	# passe au jour suivant
	if(((int(mois)==2)and(int(jour)==29)) or (((int(mois)==3) or (int(mois)==5) or (int(mois)==7) or (int(mois)==8) or (int(mois)==10))and(int(jour)==31)) or (((int(mois)==4) or (int(mois)==6) or (int(mois)==9) or (int(mois)==11))and(int(jour)==30))):
		jour = '01'
		if (int(mois)<9):
			mois = '0'+ str(int(mois)+1)
		else :
			mois = str(int(mois)+1)
	# 5 septembre manquant dans la BDD
	elif((int(mois)==9) and (int(jour)==4)):
		jour='06'
	elif (int(jour)<9):
		jour = '0'+str(int(jour)+1)
	else :
		jour = str(int(jour)+1)
	
	
