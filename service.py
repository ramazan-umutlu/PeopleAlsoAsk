import requests
from lxml.html import fromstring
import lxml.html
import pandas as pd
import xlsxwriter
file1 = open('YOUR KEYWORDS FILE PATH/keywords.txt',
             'r', encoding="utf-8")
Lines = file1.readlines()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept-Language': 'tr-tr,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
questions = []
for line in Lines:
    query = line.strip()
    response = requests.get(
        f'https://www.google.com/search?q={query}&start=0', headers=header).text
    tree = lxml.html.fromstring(response)
    nodes = tree.xpath('//@data-q')
    fixssues = {'Questions': nodes}
    to_excel = dict([(k, pd.Series(v)) for k, v in fixssues.items()])
    df = pd.DataFrame.from_dict(to_excel)
    writer = pd.ExcelWriter(f'{query}_questions.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet', index=False)
    writer.close()
file1.close()
