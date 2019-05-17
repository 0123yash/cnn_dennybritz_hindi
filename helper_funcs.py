import urllib.request, json 
import csv

csv.field_size_limit(100000000)

def getJsonFromUrl(url):
    with urllib.request.urlopen(finalUrl) as url:
        data = json.loads(url.read().decode())
        return data

def getListFromCsv(filePath):
    with open(filePath, 'r', encoding='utf-8') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        return lines

def getListFromCsvV2(filePath):
    with open(filePath, 'r', encoding='utf-8') as readFile:
        lines = [line.rstrip('\n') for line in readFile]
        return lines

