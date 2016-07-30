# coding=utf8
from __future__ import unicode_literals, print_function

import urllib2
from bs4 import BeautifulSoup

# 財政部官網
request_url = 'http://invoice.etax.nat.gov.tw/' 

# 取得HTML
htmlContent = urllib2.urlopen(request_url).read()
soup = BeautifulSoup(htmlContent, "html.parser")

results = soup.find_all("span", class_="t18Red")

subTitle = ['特別獎', '特獎', '頭獎', '增開六獎'] # 獎項


months = soup.find_all('h2', {'id': 'tabTitle'})
# 最新一期
month_newst = months[0].find_next_sibling('h2').text
# 上一期
month_previous = months[1].find_next_sibling('h2').text

print ("最新一期統一發票開獎號碼 ({0})：".format(month_newst))
for index, item in enumerate(results[:4]):
	print ('>> {0} : {1}'.format(subTitle[index], item.text))

print ("上期統一發票開獎號碼 ({0})：".format(month_previous))
for index2, item2 in enumerate(results[4:8]):
	print ('>> {0} : {1}'.format(subTitle[index2], item2.text))