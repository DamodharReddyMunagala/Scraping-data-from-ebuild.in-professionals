from bs4 import BeautifulSoup
import urllib.request as urlRequest
from urllib.request import urlopen
import re
import pandas as pd
import pymongo
import requests
from pymongo import MongoClient
from pymongo import MongoClient as Connection

firm_link = []
company_name = []
firm_name = []
role_name = []
place = []
service_area = []
project_type = []
projects_listed = []
firm_project_link = []
firm_team = []

#For firm_details()
firm_image_list = []
Postal_Address = []
mail_Address = []
website_Address = []
phone_number = []
owner = []
Year_Established = []
Employees = []

#For firm_project_details
#firm_project_image_list = []                                ##Not needed after modifying the code
firm_project_image_title_list = []
firm_project_image_url_list = []
Image_Gallery_TITLES_list = []
Image_Gallery_URLS_list = []

#For ProjectImageGallery
project_image_gallery_list = []


url = "http://ebuild.in/professionals"

req = requests.get(url)
response = open('ebuild.html', 'wb')
for chunk in req.iter_content(100000):
    response.write(chunk)
response.close()

soup = BeautifulSoup(open('ebuild.html'), 'lxml')
for data in (soup.find('div',{'id' : 'profInner'}).findAll('a', {'target' : '_blank'})):
    firm_link.append('http://ebuild.in/' + data.attrs['href'])
     
    """First for loop wil get the details of the Company, Firm, Firm_role, City."""
    
    for item in data.find('div', {'id' : 'arcds'}):
        company_name.append(item.h3.text.replace('.', ''))
        
        try:
            firm_name.append(item.h4.text.replace('By ', ''))
        except AttributeError as e:
            firm_name.append('')
        
        try:
            ele = (item.find('h5').text)
            if ele[0] == "(":
                role_name.append(ele)
            else:
                role_name.append('')
        except AttributeError as e:
            role_name.append('')
            
        try:
            cells = []
            cells = item.find('h5', {'class' : 'ct'}).text
            place.append(cells)
        except AttributeError as e:
            place.append('')
    
    
    cells = data.find('figcaption', {'class' : 'clearfix'}).findAll('div')
    try:
        for ele in cells[1].findAll('table', {'id' : 'mtb1'}):
            atoms = ele.findAll('tr')
            if 'Service Area' in atoms[0].td.text:
                service_area.append(atoms[0].text.replace('Service Area:', ''))
            elif 'Service Area' in atoms[1].td.text:
                service_area.append(atoms[1].text.replace('Service Area:', ''))
            elif 'Service Area' in atoms[2].td.text:
                service_area.append(atoms[2].text.replace('Service Area:', ''))
            else:
                service_area.append('')
    except IndexError as e:
        service_area.append('')
        
    try:
        for ele in cells[1].findAll('table', {'id' : 'mtb1'}):
            atoms = ele.findAll('tr')
            if 'Project Type' in atoms[0].td.text:
                project_type.append(atoms[0].text.text.replace('Project Type:', ''))
            elif 'Project Type' in atoms[1].td.text:
                project_type.append(atoms[1].text.replace('Project Type:', ''))
            elif 'Project Type' in atoms[2].td.text:
                project_type.append(atoms[2].text.replace('Project Type:', ''))
            else:
                project_type.append('')
    except IndexError as e:
        project_type.append('')
        
    try:
        for ele in cells[1].findAll('table', {'id' : 'mtb1'}):
            atoms = ele.findAll('tr')
            if 'Projects Listed' in (atoms[0].td.text):
                projects_listed.append(atoms[0].text.replace('Projects Listed :', ''))
            elif 'Projects Listed' in (atoms[1].td.text):
                projects_listed.append(atoms[1].text.replace('Projects Listed :', ''))
            elif 'Projects Listed' in (atoms[2].td.text):
                projects_listed.append(atoms[2].text.replace('Projects Listed :', ''))
            else:
                projects_listed.append('')
    except IndexError as e:
        projects_listed.append('')

for link in firm_link:
    firm_project_link.append(link + '-projects')
    firm_team.append(link + '-team')

def firm_details(firm_link):
    
    try:
        BeautifulSoup(open(firm_link.replace('.','-').replace('/','') + '.html'), 'lxml')
    except FileNotFoundError as e:
        req = requests.get(firm_link)
        response = open(firm_link.replace('.','-').replace('/','') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            response.write(chunk)
        response.close()
    
    soup = BeautifulSoup(open(firm_link.replace('.','-').replace('/','') + '.html'), 'lxml')
    
    firm_name = []
    firm_image_url = []
    firm_image = {}
    
    try:
        for data in soup.find('div', {'class' : 'pro-cell1'}).find('div', {'class' : 'img'}).findAll('a', href = re.compile('^(#)')):
            firm_name = data.find('img').attrs['alt'].replace('.', '')
            firm_image_url = data.find('img').attrs['src']
            firm_image[firm_name] = firm_image_url
    except AttributeError as e:
        firm_image[' '] = ''
    firm_image_list.append(firm_image)
    
    try:
        Postal_Address.append(soup.find('div', {'itemtype' : 'http://schema.org/PostalAddress'}).text)
    except AttributeError as e:
        Postal_Address.append('')

    try:
        cells = soup.find('div', {'id' : 'otherInfo'}).findAll('p')
    except AttributeError as e:
        cells = []
        
    try:
        if 'mailto:' in cells[0].find('a').attrs['href']:
            mail_Address.append(cells[0].find('a').attrs['href'].replace('mailto:', ''))
        elif 'mailto:' in cells[1].find('a').attrs['href']:
            mail_Address.append(cells[1].find('a').attrs['href'].replace('mailto:', ''))
        elif 'mailto:' in cells[2].find('a').attrs['href']:
            mail_Address.append(cells[2].find('a').attrs['href'].replace('mailto:', ''))
        elif 'mailto:' in cells[3].find('a').attrs['href']:
            mail_Address.append(cells[3].find('a').attrs['href'].replace('mailto:', ''))
        elif 'mailto:' in cells[4].find('a').attrs['href']:
            mail_Address.append(cells[4].find('a').attrs['href'].replace('mailto:', ''))
        elif 'mailto:' in cells[5].find('a').attrs['href']:
            mail_Address.append(cells[5].find('a').attrs['href'].replace('mailto:', ''))
        else:
            mail_Address.append('')
    except IndexError as e:
        mail_Address.append('')
    except AttributeError as e:
        mail_Address.append('')

    try:
        if 'http:' in cells[0].find('a').attrs['href']:
            website_Address.append(cells[0].find('a').attrs['href'])
        elif 'http:' in cells[1].find('a').attrs['href']:
            website_Address.append(cells[1].find('a').attrs['href'])
        elif 'http:' in cells[2].find('a').attrs['href']:
            website_Address.append(cells[2].find('a').attrs['href'])
        elif 'http:' in cells[3].find('a').attrs['href']:
            website_Address.append(cells[3].find('a').attrs['href'])
        elif 'http:' in cells[4].find('a').attrs['href']:
            website_Address.append(cells[4].find('a').attrs['href'])
        elif 'http:' in cells[5].find('a').attrs['href']:
            website_Address.append(cells[5].find('a').attrs['href'])
        else:
            website_Address.append('')
    except IndexError as e:
        website_Address.append('')
    except AttributeError as e:
        website_Address.append('')

    try:
        if 'Phone:' in cells[0].text:
            phone_number.append(cells[0].text.replace('Phone:', ''))
        elif 'Phone:' in cells[1].text:
            phone_number.append(cells[1].text.replace('Phone:', ''))
        elif 'Phone:' in cells[2].text:
            phone_number.append(cells[2].text.replace('Phone:', ''))
        elif 'Phone:' in cells[3].text:
            phone_number.append(cells[3].text.replace('Phone:', ''))
        elif 'Phone:' in cells[4].text:
            phone_number.append(cells[4].text.replace('Phone:', ''))
        elif 'Phone:' in cells[5].text:
            phone_number.append(cells[5].text.replace('Phone:', ''))
        else:
            phone_number.append('')
    except IndexError as e:
        phone_number.append('')
    except AttributeError as e:
        phone_number.append('')

    try:
        if 'Owner:' in cells[0].text:
            owner.append(cells[0].text.replace('Owner: ', ''))
        elif 'Owner:' in cells[1].text:
            owner.append(cells[1].text.replace('Owner: ', ''))
        elif 'Owner:' in cells[2].text:
            owner.append(cells[2].text.replace('Owner: ', ''))
        elif 'Owner:' in cells[3].text:
            owner.append(cells[3].text.replace('Owner: ', ''))
        elif 'Owner:' in cells[4].text:
            owner.append(cells[4].text.replace('Owner: ', ''))
        elif 'Owner:' in cells[5].text:
            owner.append(cells[5].text.replace('Owner: ', ''))
        else:
            owner.append('')
    except IndexError as e:
        owner.append('')
    except AttributeError as e:
        owner.append('')

    try:
        if 'Founded:' in cells[0].text:
            Year_Established.append(cells[0].text.replace('Founded: ', ''))
        elif 'Founded:' in cells[1].text:
            Year_Established.append(cells[1].text.replace('Founded: ', ''))
        elif 'Founded:' in cells[2].text:
            Year_Established.append(cells[2].text.replace('Founded: ', ''))
        elif 'Founded:' in cells[3].text:
            Year_Established.append(cells[3].text.replace('Founded: ', ''))
        elif 'Founded:' in cells[4].text:
            Year_Established.append(cells[4].text.replace('Founded: ', ''))
        elif 'Founded:' in cells[5].text:
            Year_Established.append(cells[5].text.replace('Founded: ', ''))
        else:
            Year_Established.append('')
    except IndexError as e:
        Year_Established.append('')
    except AttributeError as e:
        Year_Established.append('')

    try:
        if 'Employees:' in cells[0].text:
            Employees.append(cells[0].text.replace('Employees: ', ''))
        elif 'Employees:' in cells[1].text:
            Employees.append(cells[1].text.replace('Employees: ', '')) 
        elif 'Employees:' in cells[2].text:
            Employees.append(cells[2].text.replace('Employees: ', ''))
        elif 'Employees:' in cells[3].text:
            Employees.append(cells[3].text.replace('Employees: ', ''))
        elif 'Employees:' in cells[4].text:
            Employees.append(cells[4].text.replace('Employees: ', '')) 
        elif 'Employees:' in cells[5].text:
            Employees.append(cells[5].text.replace('Employees: ', ''))  
        else:
            Employees.append('')
    except IndexError as e:
        Employees.append('')
    except AttributeError as e:
        Employees.append('')

def firm_project_details(firm_project_link):
    
    try:
        BeautifulSoup(open(firm_project_link.replace('/','').replace('.','-') + '.html'), 'lxml')
    except FileNotFoundError as e:
        req = requests.get(firm_project_link)
        response = open(firm_project_link.replace('/','').replace('.','-') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            response.write(chunk)
        response.close()
    
    project_link = []
    project_title = []
    project_image = {}
    image_title_list = []
    image_url_list = []
    ProjectGalleryImagesTITLE = []
    ProjectGalleryImagesURL = []
    soup = BeautifulSoup(open(firm_project_link.replace('/','').replace('.','-') + '.html'), 'lxml')
    try:
        for data in soup.find('div', {'id' : 'projectAll'}).findAll('div', {'class' : 'photo'}):
            image_title = data.find('a').attrs['title']
            image_url = data.find('a').find('img').attrs['data-original']
            image_title_list.append(image_title)
            image_url_list.append(image_url)
            #project_image[image_title] = image_url               ##Not needed after modifying the code
            if data.find('a').attrs['href'] == '/':
                pass
            else:
                project_link.append('http://ebuild.in' + data.find('a').attrs['href'])
                project_title.append(data.find('a').attrs['title'])
    except AttributeError as e:
        project_link.append('')
        project_title.append('')
        
    #firm_project_image_list.append(project_image)                ##Not needed after modifying the code
    firm_project_image_title_list.append(image_title_list)
    firm_project_image_url_list.append(image_url_list)
    
    for link in project_link:
        ProjectGalleryImagesTITLE.append(ProjectImageGallery(link)[0])
        ProjectGalleryImagesURL.append(ProjectImageGallery(link)[1])
    Image_Gallery_TITLES_list.append(ProjectGalleryImagesTITLE)
    Image_Gallery_URLS_list.append(ProjectGalleryImagesURL)

def ProjectImageGallery(project_link):
    
    try:
        BeautifulSoup(open(project_link.replace('/','').replace('.','-') + '.html'), 'lxml')
    except FileNotFoundError as e:
        req = requests.get(project_link)
        sample = open(project_link.replace('/','').replace('.','-') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            sample.write(chunk)
        sample.close()
    
    project_image_gallery = {}
    project_image_name = []
    project_image_url = []
    project_image_gallery_title = []
    project_image_gallery_url = []
    soup = BeautifulSoup(open(project_link.replace('/','').replace('.','-') + '.html'), 'lxml')
    try:
        for data in soup.find('div',{'class' : 'gal'}).findAll('div', {'class' : 'pin'}):
            project_image_name.append(data.find('img').attrs['alt'])
            project_image_url.append(data.find('img').attrs['src'])
    except AttributeError as e:
        project_image_name.append('')
        project_image_url.append('')
        
    for i in range(len(project_image_name)):
        #project_image_gallery[project_image_name[i]] = project_image_url[i]  ##Not needed(This will store only one image)
            project_image_gallery_title.append(project_image_name[i])
            project_image_gallery_url.append(project_image_url[i])
    project_image_gallery_list.append(project_image_gallery)
    
    return (project_image_gallery_title, project_image_gallery_url)


for link in firm_link:
    firm_details(link)

for link in firm_project_link:
    firm_project_details(link)

###Creating the Database
connection = Connection()
db = connection.hutstory
firmCollection = db.firms
projectCollection = db.projects
projectLinkCollection = db.projectLinks
imageGalleryCollection = db.images
for i in range(len(firm_link)):
    insertFirmData = {"CompanyName" : company_name[i],
            "FirmImage" : firm_image_list[i],
            "FirmName" : firm_name[i],
            "RoleName" : role_name[i],
            "Place" : place[i],
            "ServiceArea" : service_area[i],
            "ProjectType" : project_type[i],
            "ProjectsListed" : projects_listed[i],
            "PostalAddress" : Postal_Address[i],
            "WebsiteAddress" : website_Address[i],
            "MailAddress" : mail_Address[i],
            "Owner" : owner[i],
            "YearEstablished" : Year_Established[i],
            "NumberOfEmployees" : Employees[i],
            "FirmLink" : firm_link[i]}
    FIRMID = firmCollection.insert_one(insertFirmData).inserted_id
    
    for j in range(len(firm_project_image_title_list[i])):
        insertProjectData = {"ProjectImageTitle" : firm_project_image_title_list[i][j],
                      "ProjectImageURL" : firm_project_image_url_list[i][j],
                      "firmId" : FIRMID}
        PROJECTID = projectCollection.insert_one(insertProjectData).inserted_id
        
    for j in range(len(Image_Gallery_TITLES_list[i])):
        insertProjectLinkData = {"ProjectWithGalleryTitle" : Image_Gallery_TITLES_list[i][j],
                                 "ProjectWithGalleryUrl" : Image_Gallery_URLS_list[i][j],
                                 "firmId" : FIRMID}
        PROJECTLINKID = projectLinkCollection.insert_one(insertProjectLinkData).inserted_id
        
        for k in range(len(Image_Gallery_TITLES_list[i][j])):
            insertImageData = {"ImageGalleryOfProjectTitle" : Image_Gallery_TITLES_list[i][j][k],
                               "ImageGalleryOfProjectUrl" : Image_Gallery_URLS_list[i][j][k],
                          "projectLinkId" : PROJECTLINKID}
            IMAGEID = imageGalleryCollection.insert_one(insertImageData).inserted_id

#Creating a DataFrame
df=pd.DataFrame(company_name,columns=['Company Name'])
df['Firm Name']=firm_name
df['Firm Image']=firm_image_list
df['Role Name'] = role_name
df['Place'] = place
df['Service Area'] = service_area
df['Project Type'] = project_type
df['Projects Listed'] = projects_listed
df['Postal Address'] = Postal_Address
df['Website Address'] = website_Address
df['Mail Address'] = mail_Address
df['Owner'] = owner
df['Year Established'] = Year_Established
df['Number of Employees'] = Employees
df['Firm Link'] = firm_link
df['Project Image Title'] = firm_project_image_title_list
df['Project Image Url'] = firm_project_image_url_list
df['Image Gallery of Project Titles'] = Image_Gallery_TITLES_list
df['Image Gallery of Project Urls'] = Image_Gallery_URLS_list
df.to_csv('output.csv',index=True,header=True)
