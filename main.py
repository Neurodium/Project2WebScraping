from helpers import get_all_categories, get_books_from_category, write_book_values, \
    book_title, book_image, book_category, book_upc, \
    save_image, clean_book_title, folder_init, init_csv, get_image_folder, get_book_folder


image_folder = "Images"
book_folder = "Books"

# Website to be scrapped
url = 'http://books.toscrape.com/index.html'

print("Webscrapping of website '" + str(url) + "' starts:\n")

# Initialize script creating image folder if does not exist and create or
# empty data file
image_path = get_image_folder(image_folder)
book_path = get_book_folder(book_folder)

print(
    "Data will be stored in folder " +
    str(book_folder) +
    " and covers will be stored in folder " +
    str(image_folder) +
    "\n")
folder_init(image_folder, image_path, book_folder, book_path)


# Dictionnary creation with key categories and url values
categories = get_all_categories(url)

print(str(len(categories)) + " categories have been found.\n")

# Category names list creation
cat_names = categories.keys()
all_urls = []
current_category = 1

# Display message for starting retrieving all books url
print("Fetching all books\n")

# List creation of all books urls
for i in cat_names:
    # Création/initialisation du fichier csv pour la catégorie
    init_csv(i, book_path)
    # Affichage de la catégorie en cours de traitement
    print("Fetching books of category : " + str(i))
    all_urls += get_books_from_category(categories[i])
    progress_url = round((current_category / len(cat_names)) * 100, 2)
    # Affichage de la progression de récupération des urls
    print("Progress......" + str(progress_url) + " %\n")
    current_category += 1

# Identify the number of books
nb_book_url = len(all_urls)

# Display message showing number of books found
print(str(nb_book_url) + " books found.\n")

# Display message for starting data fetching process
print("Start fetching books data.\n")

current_book = 1

# Import data in specified file and save images in the folder specified
for u in all_urls:
    # Affichage du titre du livre dont on récupère les données
    print("Current book : " + str(book_title(u)))
    write_book_values(u, book_path)
    save_image(
        image_path,
        book_category(u),
        book_upc(u),
        clean_book_title(u),
        book_image(u))
    progress_book = round((current_book / nb_book_url) * 100, 2)
    # Affichage de la progression de la récupération de données
    print("Progress....... " + str(progress_book) + " %\n")
    current_book += 1


# Display script end message
print("Webscrapping of : '" + str(url) + "' is over.")
