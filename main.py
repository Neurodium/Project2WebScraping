from helpers import getAllCategories, getBooksfromCategory,writeBookValues, writeUrls, bookTitle, bookImage, bookCategory, saveImage, cleanBookTitle

#Adresse du site à scrapper
url = 'http://books.toscrape.com/index.html'

#Creation du dictionnaire contenant les catégories et leur lien associé
categories = getAllCategories(url)

print(str(len(categories)) + " categories ont été trouvées.\n")

#Création d'une liste contenant les noms des catégories
cat_names = categories.keys()
all_urls = []
current_category = 1

#Affichage du débutg du traitement de récupération des adresses par catégorie
print("Récupération de toutes les adresses de chaque livre\n")

#Création d'une liste contenant toutes les url des livres du site
for i in cat_names:
    print("Récupération des livres de la catégorie: " + str(i))#Affichage de la catégorie en cours de traitement
    all_urls += getBooksfromCategory(categories[i])
    progress_url = round((current_category / len(cat_names))*100, 2)
    print("Progression......" + str(progress_url) + " %")#Affichage de la progression de récupération des urls
    current_category += 1

#Crée le fichier pour contenir toutes les adresses en cas de vérification, vide le fichier si déjà existant
with open('urls.csv', 'w') as file:
    file.write('Address\n')

#Identifie le nombre de livres du site
nb_book_url = len(all_urls)

#Affichage du nombre de livres trouvés
print(str(nb_book_url) + " livres ont été trouvés.")

#Crée le fichier de récupération des données de chaque livre, vide le fichier si déjà existant
with open('books.csv', 'w') as file:
    file.write('Product Page URL;Universal Product Code;Title;Price Including Tax;Price Excluding Tax;Number Available;Product Description;Category;Review Rating;Image Url\n')

#Affichage du début du traitement des données
print("Démarrage de la récupération des données.")

current_book = 1

#Importe les données dans le fichier books.csv et urls.csv
for u in all_urls:
    print("Traitement du livre: "+ str(bookTitle(u))) #Affichage du titre du livre dont on récupère les données
    writeBookValues('books.csv', u)
    # writeUrls('urls.csv', u)
    # saveImage(bookCategory(u), cleanBookTitle(u), bookImage(u))
    progress_book = round((current_book/nb_book_url)*100, 2)
    print("Progression....... " + str(progress_book) + " %") #Affichage de la progression de la récupération de données
    current_book +=1


#Affichage de la fin du traitement des données
print("Le scrapping de l'adresse: " + str(url) + " est terminé.")
