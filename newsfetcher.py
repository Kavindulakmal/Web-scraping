import requests
from bs4 import BeautifulSoup

def write_heading_to_file(file_path: str, headings) :

    try :
        with open(file_path, 'w') as new_file :
         for heading in headings:
            new_file.write(heading)
            new_file.write("\n")
    except OSError:
       print("IO error")


url = "https://www.reuters.com/world/us/"
response = requests.get(url)

if response.status_code == 200:
    content = response.content
   
    soup = BeautifulSoup(content,'html.parser')

    try:
        headings = soup.select('h3[data-testid="Heading"]')
        heading_list =[]
        for heading in headings:
            link = heading.find("a")
            if link is not None:
             text = link.text
             heading_list.append(text)

    except Exception:
       print("Error processing")

    write_heading_to_file("C:/Users/hp/Desktop/Web_Scraping/textfile.txt",heading_list)
    print("Successful!")


    
