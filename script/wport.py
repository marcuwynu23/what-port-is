import requests
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml"
content = requests.get(url).content
soup = bs(content, "html.parser")

# threading function asyncronous request


def generate_links():
	links = []
	lastLinkNumber = soup.select("div.pagination > a")[-1].text
	for i in range(1, int(lastLinkNumber)):
		links.append(url + "?page=" + str(i))
	return links

                              
def get_data(soup,port_filter):
	table = soup.select("table#table-service-names-port-numbers")
	rows = table[0].select("tr")
	header_row = rows[0]

	headers = [header.text for header in header_row.select("th")[:-3]]
	data = []
	
	for row in rows[1:]:
		cells = row.select("td")
		if int(cells[1].text) == port_filter:
			data.append([cells[0].text, cells[1].text,cells[2].text, cells[3].text])
			break
	print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
	exit(0)

def wport(message,port_filter):
	print(message,port_filter)
	links = generate_links()
	for link in links:
		# add error exception if link not access or not found
		try:
			content = requests.get(link).content
			soup = bs(content, "html.parser")
			get_data(soup,port_filter)
		except Exception as e:
			print(e)
			exit(1)
