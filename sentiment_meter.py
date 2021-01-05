import requests
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
print("1.User can give link for the article.\n2.Example for negative article.\n3.Example for positive article.\n")
ch=int(input("Enter Your choice:"))

if ch==1:
	val = input("Enter the link: ")
	result=requests.get(val)
	#src=result.content
	#soup = BeautifulSoup(result.content, 'html.parser')

if ch==2:
	result=requests.get("https://en.wikipedia.org/wiki/Negativity_bias")
	#src=result1.content
	#soup = BeautifulSoup(result1.content, 'html.parser')
if ch==3:
	result=requests.get("https://en.wikipedia.org/wiki/Encyclopedia")




#src=result.content
soup = BeautifulSoup(result.content, 'html.parser')
#print(soup.prettify())
a=soup.find_all('p')
l=len(a)
b=[]
n=0
count=0
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
				count=count+1

try:
	avg=(n*10)/count
	#print("average points:",avg)

except:
	print("exception")

if(n<0):
	print("\nThe given aritcle is Negative.\nThe average Points for negative words in the article: ",int(-2*avg),"/10")
	#print(int(-2*avg),"/10")

elif(n>0):
	print("\nThe given article is Positive.\nThe average points for positive words in the article: ",int(2*avg),"/10")
else:
	print("Neutral")


