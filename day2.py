import requests
import array
from bs4 import BeautifulSoup
#val = input("Enter link for the article: ") 
#result=requests.get(val)
result=requests.get("https://en.wikipedia.org/wiki/Negativity_bias")
src=result.content
soup = BeautifulSoup(result.content, 'html.parser')
#print(soup.prettify())
a=soup.find_all('p')
l=len(a)
b=[]
n=0
po=0
ne=0
flag=0
count=0
avg=0
bad_chars=['\n','[',']','(',')','1','2','3','4','5','6','7','8','9','0','.',',',':','~','@','#','$','%','^','&','*','+','=','_']


negative=requests.get("https://gist.github.com/mkulakowski2/4289441")
soup2=BeautifulSoup(negative.content, 'html.parser')
a1=soup2.find_all('tr')
l2=len(a1)
b1=[]
for i in range(37,l2-1):
	b1.append(soup2.find_all('tr')[i].get_text().replace('\n',''))
	#b1=b1.replace('\n','')
#print(b1)


positive=requests.get("https://gist.github.com/mkulakowski2/4289437")
soup3=BeautifulSoup(positive.content, 'html.parser')
a2=soup3.find_all('tr')
l3=len(a2)
b2=[]
for i in range(35,l3-3):
	b2.append(soup3.find_all('tr')[i].get_text().replace('\n',''))
#print(b2)


for i in range(l):
	b.append(soup.find_all('p')[i].get_text())
	c=soup.find_all('p')[i].get_text()
	for j in bad_chars :
    		c = c.replace(j, '')
	p=c.split()
	plen=len(p)
	#print(p)
	
	for i in range(plen):
		for j in range(len(b1)):
			if(p[i]==b1[j]):
				n=n-10
				count=count+1
				#print(count)
				flag=1
		for k in range(len(b2)):
			if(p[i]==b2[k]):
				po=po+10
				count=count+1
				#print(count)
				flag=1



try:
	avg=(n+po)/count
	print("Average is")
	print(avg)
	if(avg<0):
		print("Negative")
	elif(avg>0):
		print("Positive")
	else:
		print("Neutral")

except:
	print("exception")


