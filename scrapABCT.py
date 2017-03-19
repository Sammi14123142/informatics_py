from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getName(url):
	# check if the link is accessable
	# break if an HTTP error is returned
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	# check if a tag exists
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
		nameList = bsObj.findAll("a", {"class": "blue"})
		links = bsObj.findAll("a", href=re.compile("^(staff-singledemo).*"))
	except AttributeError as e:
		return None
	return nameList, links

nameList, links = getName("https://www.polyu.edu.hk/abct/en/staff-acad_staff.html")
if nameList == None:
	print("Name could not be found")
else:
	for name in nameList:
		print(name.get_text())

def getSummary(researchUrl):
	print(researchUrl)
	html = urlopen(researchUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	summary = bsObj.find("div", {"class", "info_box"}).children
	for child in summary:
		print(child)

for link in links:
	researchUrl = "https://www.polyu.edu.hk/abct/en/staff-singledemo3" + link.attrs['href'][16:]
	getSummary(researchUrl)
