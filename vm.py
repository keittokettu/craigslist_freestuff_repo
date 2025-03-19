# Version 1: Scrapes thumbnail images from the first page of books.toscrape.com

import requests
from bs4 import BeautifulSoup
from PIL import Image
import os

city = "pittsburgh"
# version of city string for tsv file, associated w/ listing entry. if city has two words, manually input:
citycap = city.capitalize()

# Create a directory to save the book cover thumbnail images      
os.makedirs(city + '_craigslist_images', exist_ok=True)
# Create a TSV file to store the book title, image URL, and image file name
tsv_file = open((city + '_craigslist_images.tsv'), 'w')
tsv_file.write('Title\tImage URL\tImage File Name\tCity\n') # Write the header row

# Scrape the site for book cover images

with open(city + "_imgs.txt", "r") as file:
    data = file.read()

site_url = data.split(",")  # Split by comma to get individual URLs

print("the length of website-array is: ", len(site_url))

for site in site_url:  
    response = requests.get(site)
    #response.raise_for_status() # Raise an exception if the response is not successful
    if not(response.ok):
        print("this url doesn't work!:\n")
        print(image_url)
        print("\n")
        continue
    soup = BeautifulSoup(response.text, 'html.parser')      

    # Find all the book items on the page 
    listing_items = soup.find_all('div', class_='swipe-wrap')
    
    # print(listing_items)
    for listings in listing_items:
        listing_title = listings.find('img').get('alt')
        # print(listing_title)
        image_url = listings.find('img').get('src')
        image_url = image_url # Construct the full image URL
        image_file_name = listing_title + '.jpg'
        image_file_name = image_file_name.replace(" ", "_")
        safe_file_name = image_file_name.replace("/", "-")
        image_file_path = os.path.join((city + '_craigslist_images'), safe_file_name)
        
        # Download the thumbnail image
        response = requests.get(image_url)
        # response.raise_for_status() # Raise an exception if the response is not successful
        if not(response.ok):
            print("this url doesn't work!:\n")
            print(image_url)
            print("\n")
            continue
        with open(image_file_path, 'wb') as image_file:
            image_file.write(response.content)
        
        # Write the book title, image URL, and image file name to the TSV file
        tsv_file.write(f'{listing_title}\t{image_url}\t{safe_file_name}\t{citycap}\n')

tsv_file.close()
print('Scraping complete!')

# Input and output folders
input_folder = "/Users/santiago/Desktop/yaydemo/" + city + "_craigslist_images"
output_folder = "/Users/santiago/Desktop/yaydemo/" + city + "_craigslist_images_sized"
output_smlr_folder = "/Users/santiago/Desktop/yaydemo/" + city + "_craigslist_images_sized_smlr"
os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_smlr_folder, exist_ok=True)

# Resize and save images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize((512, 512))
        img_resized.save(os.path.join(output_folder, filename))
        img_resized_2 = img.resize((128, 128)) 
        img_resized_2.save(os.path.join(output_smlr_folder, filename))

print("Batch resizing complete!")