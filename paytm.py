import requests,pprint
from bs4 import BeautifulSoup
a=requests.get('https://paytm.com/shop/search?q=pickles&from=organic&child_site_id=1&site_id=1&category=101471')
print (a)
b=BeautifulSoup(a.text,'html.parser')
name=[]
rate=[]
cashback=[]
details={'name':'','rate':'','cashback':''}
piss=b.findAll('div',class_='_2apC')
for i in piss:
	name.append (i.text)
rates=b.findAll('span',class_='_1kMS')
for i in rates:
	rate.append(i.text)
cashbacks=b.findAll('div',class_='_27VV')
for i in cashbacks:
	cashback.append(i.text)
ipo=[]
for j in range(len(name)):
	details['name']= name[j]
	details['rate']=rate[j]
	details['cashback']= cashback[j]
	ipo.append(details.copy())
pprint.pprint (ipo)
dude=input('Enter')
for i in range(len(ipo)):
	if dude==ipo[i]['rate']:
		print (ipo[i])
