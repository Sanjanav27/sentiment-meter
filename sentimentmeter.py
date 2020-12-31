import requests
import array
from bs4 import BeautifulSoup
val = input("Enter link for the article: ") 
result=requests.get(val)
src=result.content
soup = BeautifulSoup(result.content, 'html.parser')
#print(soup.prettify())
a=soup.find_all('p')
l=len(a)
b=[]
n=0
count=0
avg=0
bad_chars=['\n','[',']','(',')','1','2','3','4','5','6','7','8','9','0','.',',',':']

negative=requests.get("https://gist.github.com/mkulakowski2/4289441")
soup2=BeautifulSoup(negative.content, 'html.parser')
a1=soup2.find_all('tr')
l2=len(a1)
b1=[]
for i in range(37,l2-1):
	b1.append(soup2.find_all('tr')[i].get_text().replace('\n',''))
	#b1=b1.replace('\n','')
#print(b1)
for i in range(l):
	b.append(soup.find_all('p')[i].get_text())
	c=soup.find_all('p')[i].get_text()
	for j in bad_chars :
    		c = c.replace(j, '')
	p=c.split()
	plen=len(p)
	for i in range(plen):
		for j in range(len(b1)):
			if(p[i]==b1[j]):
				n=n+3
				count=count+1
				print(count)
try:
	avg=(n/count)
	print("Average of negative words is")
	print(avg)
except:
	print("exception")


