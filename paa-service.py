import requests
from lxml.html import fromstring
import lxml.html

file1 = open('C:/xampp/htdocs/RAO/PeopleAlsoAsk/keywords.txt', 'r',encoding="utf-8")
file2 = open('C:/xampp/htdocs/RAO/PeopleAlsoAsk/paa.txt', 'w',encoding="utf-8")
Lines = file1.readlines()
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept-Language': 'tr-tr,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
for line in Lines:
        query = line.strip()
        response = requests.get(f'https://www.google.com/search?q={query}&start=0', headers=header).text
        tree = lxml.html.fromstring(response)
        nodes = tree.xpath('//@data-q')
        print(query)
        file2.write(query)
        file2.write(": ")
        for node in nodes:
            file2.write(node)
            file2.write(" , ")
        file2.write("\n")
file1.close()
file2.close()