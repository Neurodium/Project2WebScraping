# Projet 2: Web Scrapping de BooksToScrape
***
## Description
***
Dans ce projet, l'utilisation du script permettra de récupérer des données contenues dans les pages HTML du site web BooksToScrape:\
**http://books.toscrape.com/**

Le script va récupérer les informations suivantes dans chaque page et les enregistrer dans un fichier csv correspondant à sa catégorie: 
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
L'exécution du script nécessitera de suivre les étapes suivantes:
### 1. Installation Python
\
Installation de python 3.4 ou supérieur : https://www.python.org/downloads/

	(Documentation d'installation de python: https://fr.wikihow.com/installer-Python)

### 2. Création d'environnement virtuel
\
Exécution de la commande:

	python -m venv env

Puis activer l'environnement:

	source env/bin/activate
ou sous windows:

	source env/Scripts/activate.bat

### 3. Installation des modules
\
Installation du module **requests**

	pip install requests

Installation du module **beautifulsoup4**

	pip install beautifulsoup4

Installation du module **lxml**

	pip install lxml

Pour consulter les versions utilisées, consulter

	(requirements.txt)



***
## Utilisation
***
Exécuter le script en utilisant 'main.py', les données des livres seront sauvegardées par catégorie dans le dossier 'Books' et les images dans le dossier 'Images'.\
Les données dans les fichiers csv sont encodées au format 'UTF-8', si les données sont lues dans un tableur, il faudra spécifier ce format de fichier pour lire les données.


