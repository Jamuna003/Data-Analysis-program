#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import json
r = requests.get("http://www.fccsingapore.com/membership/directory/")
r.content
soup = BeautifulSoup(r.content)
links = soup.findAll("a")
filename = "companies.json"
f=open(filename,"w")

for link in links:
    if "http" in link.get("href"):    
        link ="<a href='%s'>%s</a>"%(link.get("href"), link.text)
        print("Link:" +link)


for link in links:
    if "http" not in link.get("href"):
        without_http ="<a href='%s'>%s</a>"%(link.get("href"),link.text)
        print("without_http:" +without_http)
company_description = soup.findAll("div",{"class":"list_company_description"})
company_description[0].text.strip()

for item in company_description:
    company_description = item.text
    print("company_description:" +company_description)   
company_keywords = soup.findAll("div",{"class":"list_company_keywords"})
company_keywords[0].text.strip()

for value in company_keywords:
    company_keywords = value.text
    print("company_keywords:" +company_keywords)   
    
f.write(link.text +","+company_description.replace("  ","")+","+ company_keywords+"\n") 
f.close()


# In[79]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import re
url ="http://www.fccsingapore.com/membership/directory/"
html = urlopen(url)
bs = BeautifulSoup(html,"html.parser")

filename = "companies.csv"
f=open(filename,"w")
links = bs.find("div",{"id":"content"}).findAll("a",href = re.compile("(/membership/directory/account/)+([A-Za-z0-9_:()])+") )
                                                              
for link in links:
    uid =link["href"]
    print(uid)

company_description = bs.findAll("div",{"class":"list_company_description"})
company_description[0].text.strip()

for item in company_description:
    company_description = item.text.strip()
    print(company_description[0:50])
    
company_keywords = bs.findAll("div",{"class":"list_company_keywords"})
company_keywords[0].text.strip()

for value in company_keywords:
    company_keywords = value.text.strip()
    print("company_keywords:" +company_keywords)

f.write(uid +","+company_description.replace("  ","")+","+ company_keywords+"\n") 
f.close()

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




