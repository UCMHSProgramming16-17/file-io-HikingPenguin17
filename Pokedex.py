# Import requests
import requests
# Import cSV
import csv

file = open('pokedex.csv', 'w')
csvwriter = csv.writer(file, delimiter=',')
# Create URL
base_url = "http://pokeapi.co/api/v1/"

r = requests.get(base_url + 'pokedex/1')
national = r.json(['national'])

print(national)
csvwriter.writerow([])
for item in national:
    csvwriter.writerow()