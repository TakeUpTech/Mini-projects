import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

class Downloader:
    def download_one_img(self, url):
        img_data = requests.get(url).content # web url request launched
        url_split = str(url).split('/') # split image path url to find the image name
        image_name = f"{url_split[-1]}.jpg"

        with open(image_name, "wb") as file:
            file.write(img_data) # download the image using the link 

    def download_verify_one_img(self, url, img_name):
        img_data = requests.get(url).content # web url request launched

        with open(img_name, "wb") as file:
            file.write(img_data) # download the image using the link 

        try:
            Image.open(img_name).verify()
            print(img_name)
            return True
        except Exception:
            print("Corrupted image")
            os.remove(os.path.join(os.getcwd(), img_name))
            return False

    def download_all_img(self, url, wb_p, chap):
        img_list = []
        r = requests.get(url) # web url request launched
        soup = BeautifulSoup(r.text, 'html.parser') # return html script
        images = soup.find_all('img') # fin all terms in the html script (default : img)

        print("Start finding and downloading...")
        for p in range(len(images)): # for each html img line found do following lines
            try:
                # name = images[p]['alt'] # find in html line the image name (default : alt)
                link = images[p]['src'] # find in html line the image url source (default : alt)
                
                # img_name = name.replace(' ', '_').replace('/', '').replace(':', '') + '.jpg'
                img_name = f"{wb_p};{chap};{p+1}.jpg"
                
                with open(img_name, 'wb') as file:
                    im = requests.get(link) # get image link
                    file.write(im.content) # download the image using the link
                    img_list.append(bytes(img_name, 'utf-8')) # add the image name in a list (no corrupted images thanks to the try)
                    print(img_name)
            except Exception:
                print("Error") # the image couldn't be download because of corrupted or protected link 

        return img_list

    def remove_images(self):     
        file_list = os.listdir(os.getcwd()) # get list of file in the current location
        
        for item in file_list: # for each items
            if item.endswith(".jpg") or item.endswith(".png"): # il the fil extension is an image
                os.remove(os.path.join(os.getcwd(), item)) # remove the image