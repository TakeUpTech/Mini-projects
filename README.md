# Mini projects

## 11/2022 - Message for Myself
> Challenge: Development of a small application without using internet (tutorials, video...).

Message for Myself is a diary in the form of a messaging application. You can send messages and choose the mood of this message. Once sent, your messages are saved. 
Each time you open the application again the conversation field is reset. Nevertheless, if one day you want to remember events or feelings from your past, you can ask (by pressing a button) to receive a old message from yourself by choosing again the mood of the message.

<p align="center">
  <img width="720" alt="Message_for_Myself" src="https://user-images.githubusercontent.com/73184884/201381122-d8cf7e78-d7c6-4f8c-8bd5-a70d4cfd7510.png">
</p>

The application is developed on Unity 3D for smartphone. Its releases is in the associated section of this repository.

## 11/2022 - Contact Manager:
> Need: Helping someone with an assignment.

The script allows to deal with list, file writing and reading and also function and parameter creation: it's like a recap course.

The first function have for objective to search a contact in a .csv file by last name or first name. Then, it displays contact information such as first name, last name and telephone number (but other information can be added thanks to dynamic list). If it doesn't find the contact (doesn't exist), so it displays a warning message. A second function allows the user to add a new contact in the .csv file.

## 07/2022 - Web Images Downloader:
> Need: How can I read manga offline instead of using scans from a web site?

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

## 01/2022 - Laplacian Edge Detection:

> Challenge: Part of a school project, use the laplacian formula in matlab.

Part of a school project, in a group of 4, we decided to use the Laplacian formula to make an edge detection script. It allowed to read an image, apply some filters on it and the Laplacian on each pixel to return only edges of this image. Then, we also conducted an analysis of the script execution time regarding to image sizes. All details are in the report (in French) in the corresponding folder of this repository. An example of our script result is displayed below:

<p align="center">
  <img width="720" alt="Laplacian_Landscape" src="https://user-images.githubusercontent.com/73184884/204942985-196e16b1-6045-48c2-8af3-1474354feecc.JPG">
</p>

## Note:
All codes are available in this repository and are commented in detail.
