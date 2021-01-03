import requests
import array
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://sanju:1234@cluster0.wllvz.mongodb.net/sanju?retryWrites=true&w=majority")
db=cluster["sentiment_meter"]
collection=db["words"]
results=collection.find({})
for x in results:
	#print(x)
	keys = x.keys()
	y=[]
	for k in x.keys():
		#i=i+1
		y.append(k)

result=requests.get("https://en.wikipedia.org/wiki/Negativity_bias")
src=result.content
soup = BeautifulSoup(result.content, 'html.parser')
#print(soup.prettify())
a=soup.find_all('p')
l=len(a)
b=[]
n=0

bad_chars=['\n','[',']','(',')','1','2','3','4','5','6','7','8','9','0','.',',',':','~','@','#','$','%','^','&','*','+','=','_']

for i in range(l):
	b.append(soup.find_all('p')[i].get_text())
	c=soup.find_all('p')[i].get_text()
	for j in bad_chars :
    		c = c.replace(j, '')
	p=c.split()
	plen=len(p)
	#print(p)
	
	for i in range(plen):
		for j in range(len(y)):
			if(p[i]==y[j]):
				u=x.get(y[j])
				n=n+u

if(n<0):
	print("Negative")
elif(n>0):
	print("Positive")
else:
	print("Neutral")


