# Projet 2: Web Scrapping de BooksToScrape
***
## Description
***
Dans ce projet, l'utilisation du script permettra de récupérer des données contenues dans les pages HTML du site web BooksToScrape:\
**http://books.toscrape.com/**

Le script va récupérer les informations suivantes dans chaque page et les enregistrer dans un fichier 'books.csv': 
* Product Page URL
* Universal Product Code (UPC)
* Title
* Price Including Tax
* Price Excluding Tax
* Number Available
* Product Description
* Category
* Review Rating
* Image Url

Et sauvegardera aussi toutes les images de couvertures de livres dans un dossier 'Images'.
***
## Installation
***
L'exécution du script nécessitera:
* l'installation de python 3: https://www.python.org/downloads/\
	(Documentation d'installation de python: https://fr.wikihow.com/installer-Python)
* l'installation du module **requests**
* l'installation du module **beautifulsoup4**
* l'installation du module **lxml**\
	(Documentation d'installation de modules python: https://docs.python.org/fr/3.6/installing/index.html)
	(Voir requirements.txt)

***
## Utilisation
***
Exécuter le script en utilisant 'main.py', les données seront sauvegardées dans le fichier books.csv et les images dans le dossier 'Images'.
Les données dans le fichier books.csv sont encodées au format 'UTF-8', si les données sont lues dans un tableur, il faudra spécifier ce format de fichier pour lire les données.


