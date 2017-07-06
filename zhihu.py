
# coding: utf-8

# In[24]:

from urllib.request import urlretrieve
import urllib.request
from bs4 import BeautifulSoup as Soup

targeturl = 'https://www.zhihu.com/question/61235373'
count = 0
imagelist = []
req = urllib.request.Request(targeturl)
html = urllib.request.urlopen(req)
bsObj = Soup(html, 'lxml')

#print(bsObj.get_text())
t = bsObj.findAll('img')
for a in t:
    if 'src' in a.attrs:
        print(a.attrs['src'])


# In[31]:

imagelist = []
html = urllib.request.urlopen(urllib.request.Request(targeturl))
bsObj = Soup(html, 'lxml')
answerlist = bsObj.findAll('div', {'class':'List-item'})
print(len(answerlist))
for answer in answerlist:
    templist = answer.find('div', {'class':'RichContent-inner'}).findAll('img')
    for each in templist:
        if 'src' in each.attrs:
            imagelist.append(each.attrs['src'])
print(len(imagelist))
for imagelocation in imagelist:
    #path = 'E:/pic/'+str(count)+'.jpg'
    #urlretrieve(imagelocation., path)
    if 'https://' in imagelocation:
        print(imagelocation)


# In[33]:

count = 0
for imagelocation in imagelist:
    #path = 'E:/pic/'+str(count)+'.jpg'
    p = str(count)+'.jpg'
    if 'https:' in imagelocation:
        urlretrieve(location, p)
        count += 1


# In[ ]:



