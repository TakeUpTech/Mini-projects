import downloader
import img_to_pdf
import tools

class Main:
    def __init__(self):
        self.folder_name = "Images"
        self.path = f"D:/Documents/1-Projets/Python/WebImagesDownloader/{self.folder_name}"

        self.dw = downloader.Downloader()
        self.i2p = img_to_pdf.Convertor()
        self.tool = tools.Tools()
        self.tool.create_folder(self.folder_name)
        self.main()

    def main(self):        
        if input("> Download image with image url : Y/N ? ").lower() == 'y':
            self.dw.download_one_img(input("Write image url > "))

        if input("> Download images with web site url : Y/N ? ").lower() == 'y':
            image_list = self.dw.download_all_img(input("Write web site url > "), 1, 0)
            self.i2p.img_to_pdf_in_list(input("Write pdf name > "), image_list)
            self.dw.remove_images()

        if input("> Extract manga urls from one url : Y/N ? ").lower() == 'y':
            web_page = 1
            try:
                web_page = int(input("> Number of page of the web site : "))
            except Exception:
                print("Not an integer")

            for i in range(web_page):
                print(f"> Web site page : {i+1}")
                urls = self.tool.find_specific_urls(f"https://mangaflix.fr/manga/sky-high-survival.tenkuu-shinpan-scan-vf-fr?page={i+1}", "https://mangaflix.fr/manga/sky-high-survival.tenkuu-shinpan-scan-vf-fr/chapitre-", "https://mangaflix.fr/manga/sky-high-survival.tenkuu-shinpan-scan-vf-fr/chapitre-258-la-soeur-dont-je-suis-fier-2-fin")
                for j in range(len(urls)):
                    self.dw.download_all_img(urls[j], i+1, j+1)
                self.tool.check_corrupted_img(self.path)
                self.i2p.img_to_pdf_in_folder(self.path, f"Sky_High_Survival_web_page_{i+1}")
                self.dw.remove_images()

        if input("> Extract manga images from image url pattern : Y/N ? ").lower() == 'y':
            good = True
            page = 1
            for chap in range(53):
                while good:
                    good = self.dw.download_verify_one_img(f"https://scansmangas.ws/scans/gleipnir/{chap+1}/{page}.jpg", f"1;{chap+1};{page}.jpg")
                    page += 1
                page = 1
                good = True
                self.tool.check_corrupted_img(self.path)
                self.i2p.img_to_pdf_in_folder(self.path, f"Gleipnir_Chap_{chap+1}")
                self.dw.remove_images()

        print("Good read !")

main = Main()

# https://mangaflix.fr/
# https://scanmanga-vf.cc/