import os
import img2pdf

class Convertor:
    def img_to_pdf_in_list(self, file_name, img_list):
        try:
            with open(f"{file_name}.pdf", "wb") as f:
                f.write(img2pdf.convert(img_list)) # write a pdf by converting all images in the list
        except Exception:
            print("Conversion impossible")

    def img_to_pdf_in_folder(self, path, file_name):
        img_list = []
        for image in os.listdir(path):
            if not image.endswith(".jpg"): # check in the file is an image
                continue
            path = os.path.join(path, image)
            if os.path.isdir(path): # check in the file exist
                continue
            img_list.append(image) # add in list only existing images (using path to verify) in .jpg format

        # sort images by web page number, then chapter and manga page
        img_list.sort(key=lambda x: (int(x.split('.')[0].split(';')[0]), int(x.split('.')[0].split(';')[1]), int(x.split('.')[0].split(';')[2])))

        with open(f"{file_name}.pdf","wb") as f:
            f.write(img2pdf.convert(img_list)) # write a pdf by converting all images in the list