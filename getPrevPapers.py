import urllib.request
import urllib.parse
import os
from bs4 import BeautifulSoup
courseCode = input("Enter course code with spaces: ")
courseCode = courseCode.upper()
os.mkdir(courseCode)
response = os.system("ping 172.16.100.176 -c 1 -W 1 >/dev/null")
if(response == 0):
	baseUrl = "http://172.16.100.176:8080"
else:
	baseUrl = "http://125.22.54.221:8080/"
codes = courseCode.split()
html_doc = urllib.request.urlopen(f"{baseUrl}/jspui/browse?type=author&value="+codes[0]+"+"+codes[1])
soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all('a'):
    if("handle" in link.get('href')):
        semLink = baseUrl+link.get('href')
        semHtml_doc = urllib.request.urlopen(semLink)
        semSoup = BeautifulSoup(semHtml_doc, 'html.parser')
        for name in semSoup.find_all("td", class_ = "metadataFieldValue dc_date_issued"):
                os.mkdir("./"+courseCode+"/"+name.get_text())
        for inlink in semSoup.find_all('a'):
                if("bitstream" in inlink.get('href')):
                        linkParts = inlink.get('href').split("/")
                        print(f'downloading {linkParts[-1]}')
                        urllib.request.urlretrieve(baseUrl+inlink.get('href'), "./"+courseCode+"/"+name.get_text()+"/"+urllib.parse.unquote(linkParts[-1]))
        
