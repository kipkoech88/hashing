import json
import csv
import ast 
from ast import parse

# importing modules from other scripts.....



from sha import read_csv
from hashing import hash_json

csvFilePath = 'C://Users//User//Downloads//nftteams.csv'
jsonpath = 'C://Users//User//Downloads//file.json'
filename = 'C://Users//User//Downloads//file.json'
output = 'C://Users//User//Downloads//output_data.csv'

read_csv()
hash_json()

with open(filename) as json_file:
    json_data = json.load(json_file)
data_file = open(output, 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0

for data in json_data:
    if count == 0:
        json_data = ast.literal_eval(json_data)
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
        csv_writer.writerow(data.values())
        data_file.close()