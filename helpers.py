import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os


# Function to get the image folder
def get_image_folder(image_folder):
    current_folder = os.getcwd()
    image_path = os.path.join(current_folder, image_folder)
    # Return the path to the image folder
    return image_path


def get_book_folder(book_folder):
    current_folder = os.getcwd()
    book_path = os.path.join(current_folder, book_folder)
    # Return the path to the folder containing the csv files
    return book_path


# Function to initialize the script
def folder_init(image_folder, image_path, book_folder, book_path):
    if os.path.isdir(image_folder):
        pass
    else:
        os.mkdir(image_path)

    if os.path.isdir(book_folder):
        pass
    else:
        os.mkdir(book_path)


# Function to create/init category csv files:
def init_csv(category, book_path):
    filename = str(book_path) + "/" + str(category) + ".csv"
    with open(filename, 'w') as file:
        file.write(
            'Product Page URL;'
            'Universal Product Code;'
            'Title;'
            'Price Including Tax;'
            'Price Excluding Tax;'
            'Number Available;'
            'Product Description;'
            'Category;'
            'Review Rating;'
            'Image Url;'
            'Image Path'
            '\n')


# Function to write the book data within a file
def write_book_values(url, book_path, img_path):
    response = requests.get(url)
    response.encoding = 'UTF-8'
    # Check if webpage is reachable
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        product_page_url = response.url
        universal_product_code = soup.find(
            'table', {'class': 'table table-striped'}).findAll('td')[0].text
        title = soup.find('div', {'class': 'product_main'}).find('h1').text
        price_including_tax = soup.find(
            'table', {'class': 'table table-striped'}).findAll('td')[3].text
        price_excluding_tax = soup.find(
            'table', {'class': 'table table-striped'}).findAll('td')[2].text
        number_available = re.findall(
            '\\d+', soup.find('table', {'class': 'table table-striped'}).findAll('td')[5].text)[0]
        # Check if a book does have a product description
        if soup.find(
            'article', {
                'class': 'product_page'}).find(
            'p', {
                'class': None}) is not None:
            product_description = soup.find(
                'article', {
                    'class': 'product_page'}).find(
                'p', {
                    'class': None}).text
            # Replace ";" of description by "," to alifn csv columns
            product_description = re.sub(";", ",", product_description)
        else:
            product_description = ""
        category = soup.find(
            'ul', {'class': 'breadcrumb'}).findAll('a')[2].text
        review_rating = str(
            soup.find(
                'p', {
                    'class': 'star-rating'})['class'][1])
        image_url = 'http://books.toscrape.com/' + \
            re.sub("../../media/cache", 'media/cache', soup.find('img')['src'])

    filename = str(book_path) + "/" + str(category) + ".csv"

    with open(filename, 'a', encoding='UTF-8') as file:
        file.write(
            product_page_url +
            ";" +
            universal_product_code +
            ";" +
            title +
            ";" +
            price_including_tax +
            ";" +
            price_excluding_tax +
            ";" +
            number_available +
            ";" +
            product_description +
            ";" +
            category +
            ";" +
            review_rating +
            ";" +
            image_url +
            ";" +
            img_path +
            '\n')


# Function to create a dictionary with category keys and url values
def get_all_categories(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        category = {}
        get_cats = soup.find(
            'ul', {'class': 'nav-list'}).find('ul').findAll('li')
        # Associer chaque catégorie à une adresse url
        for get_cat in get_cats:
            cat_name = re.sub("\n", "", get_cat.find('a').text).strip()
            cat_address = "http://books.toscrape.com/" + \
                get_cat.find('a')['href']
            category[cat_name] = cat_address
    return category


# Function to get all books urls from a category
def get_books_from_category(cat_url):
    nextpage = "next"
    num_page = 1
    links = []
    # Visite chaque page d'une catégorie tant qu'il y a une page suivante
    while nextpage == "next":
        response = requests.get(cat_url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            divs = soup.findAll('div', {'class': 'image_container'})
            # Récupération de tous les livres de la page
            for div in divs:
                a = div.find('a')
                link = (
                    a['href']).replace(
                    "../../..",
                    "http://books.toscrape.com/catalogue")
                links.append(link)
                # Si le bouton next est présent alors la boucle continue sinon
                # elle s'arrête
                if soup.find('li', {'class': 'next'}) is not None:
                    nextpage = "next"
                    # Condition pour donner le nom de la page suivante
                    if cat_url.find('index.html') != -1:
                        cat_url = cat_url.replace("index.html", "page-2.html")
                    else:
                        cat_url = cat_url.replace(
                            "page-" + str(num_page) + ".html", "page-" + str(num_page + 1) + ".html")

                else:
                    nextpage = "stop"
            num_page += 1
    # Return list of
    return links


# Function to fetch the book title of an url
def book_title(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        res_book_title = soup.find(
            'div', {'class': 'product_main'}).find('h1').text
    return res_book_title


# Function to get the book title without forbidden caracters to create the
# filename
def clean_book_title(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        res_clean_book_title = soup.find(
            'div', {'class': 'product_main'}).find('h1').text

        chars = [
            '"',
            '/',
            "`",
            "'",
            "*",
            "_",
            "{",
            "}",
            "[",
            "]",
            "(",
            ")",
            ">",
            "#",
            "+",
            "-",
            ".",
            "!",
            "$",
            ":",
            ",",
            "\\ ",
            "?"]
        for c in chars:
            res_clean_book_title = res_clean_book_title.replace(c, "")
    return res_clean_book_title


# Function to fetch the book image url
def book_image(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        image_url = 'http://books.toscrape.com/' + \
            re.sub("../../media/cache", 'media/cache', soup.find('img')['src'])
    return image_url


# Function to fetch the book category
def book_category(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        res_book_category = soup.find(
            'ul', {'class': 'breadcrumb'}).findAll('a')[2].text
    return res_book_category

# Function to fetch the UPC


def book_upc(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        universal_product_code = soup.find(
            'table', {'class': 'table table-striped'}).findAll('td')[0].text
    return universal_product_code


# Fucntion to save image into a folder
def save_image(path, category, title, upc, url):
    filename = str(category) + "_" + str(upc) + "_" + str(title) + ".jpg"
    urllib.request.urlretrieve(url, str(path) + "/" + str(filename))
    # Give the path of the image
    return str(path) + "/" + str(filename)
