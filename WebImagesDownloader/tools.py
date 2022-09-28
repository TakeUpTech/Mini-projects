import requests
from bs4 import BeautifulSoup
import os
import re
from PIL import Image

class Tools:
    def create_folder(self, folder_name):
        try:
            os.mkdir(os.path.join(os.getcwd(), folder_name)) # create folder in script location
        except Exception:
            print("Already created.")
        os.chdir(os.path.join(os.getcwd(), folder_name)) # change location in created folder

    def find_specific_urls(self, url, pattern, exception):
        r = requests.get(url) # web url request launched
        soup = BeautifulSoup(r.text, 'html.parser') # return html script
        urls = []

        for link in soup.find_all('a'): # find all links in html page
            # if link contain a specific content (pattern) but has a different pattern of an exception, add it to a list
            # the * means that there is any caracters after the pattern content
            if re.search(f'{pattern}*', link.get('href')) and link.get('href') not in urls and link.get('href') != exception:
                print(link.get('href'))
                urls.append(link.get('href'))

        return urls
    
    def check_corrupted_img(self, path):
        for image in os.listdir(path):
            if image.endswith(".jpg"):
                try:
                    Image.open(image).verify() # check images (format .jpg) in a directory by opening them
                except Exception:
                    print(f"Corrupted image deleted : {image}")
                    os.remove(os.path.join(os.getcwd(), image)) # ff it didn't work, the script delete the image (using its path)
