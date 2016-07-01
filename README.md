# Scraping-data-from-ebuild.in-professionals and creating a Database using pymongo

If the code and the output files are not opening I recommend you to download the 
files and open them as the code and the output are large.

If you run the code for the first time it will download all the webpages in the folder where the code is present.
If in the first run if the network is broken then no need to worry the code will automatically resume the download of the webpages.
If you run the code second time the doesn't download the webpages because it checks for the html files in the folder,
if they are not present in the folder only then the code will download the webpages.
I have done this because to reduce the use of data and to save your time.

Using requests module I have downloaded the each webpage of the http://ebuild.in/professionals.
Using BeautifulSoup I have parsed the html content.
Using pymongo I created a database from the scraped content.

This webCrawler first takes the details of the firm in the first page and goes to the firm page and collects the details of
his office and go to the projects of the link and collets the images of the projects and finally goes to the each project 
page and will scrape the image gallery of the each project.

Using pymongo I have created four collections firmCollection, projectCollection, projectLinkCollection, and imageGalleryCollection.
(->) = linking (joining)
firmCollection -> projectCollection (To get image of each and every project) (using FIRMID I have linked two collections).
fimrCollection -> projectLinkCollection -> imagGalleryColection (using FIRMID and PROJECTLINKID I have linked collections(respectively)).
