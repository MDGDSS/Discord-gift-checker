import time
import requests
import pyfiglet
import csv;
csvfile = open('codes.txt','r')
csvFileArray = []
for row in csv.reader(csvfile, delimiter = ';'):
        csvFileArray.append(row)

banner = pyfiglet.figlet_format("KINGMAN")
print(banner)
i = 0
webhook = ""
def spam( i, webhook):
    while i < 100:
        i = i + 1
        n = i
        print(n)
        
        e = csvFileArray[n]
        data = requests.post(webhook, json={'content': "https://discord.gift/" + e[0]})
        print("post")
        e= False
        data = False
        row = False
       
kingman_top = 1
while kingman_top == 1:
    spam(i, webhook)


