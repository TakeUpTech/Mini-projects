# Python projects

## WebImagesDownloader:
The 'WebImagesDownloader' project allows you to download all the images of a website with distinct characteristics.
### Search and download images:
- Download an image with its link,
- Download an image with its link and check that it is not corrupted,
- Download all the images from a web page by searching in the HTML page url links associated with the 'img' tags.
### Post processing:
- Checks for corrupted images from all images downloaded,
- Converts downloaded images into a .pdf file.

The software tries to automate as much as possible the downloading of images. When the images are on different web pages, it can :
- Use a pattern (given by the user) that repeats in the url links of those images,
- Download images from links of web pages found from a main web page.

However, as each web site is coded differently, it is very difficult to find a universal pattern, that's why the program works according to very specific patterns. The user will have to add a new function dealing with a new pattern if it comes from a web site whose pattern has not been processed.

## ContactManager:
The script allows to deal with list, file writing and reading and also function and parameter creation: it's like a recap course.

The first function have for objective to search a contact in a .csv file by last name or first name. Then, it displays contact information such as first name, last name and telephone number (but other information can be added thanks to dynamic list). If it doesn't find the contact (doesn't exist), so it displays a warning message. A second function allows the user to add a new contact in the .csv file.

## Note:
All codes are available in this repository and are commented in detail.
