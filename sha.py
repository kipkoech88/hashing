import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'No' to
			# be the primary key
			key = rows['Name']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'C://Users//User//Downloads//nftteams.csv'
jsonFilePath = r'C://Users//User//Downloads//Names.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)


csvFilePath = 'C://Users//User//Downloads//nftteams.csv'
jsonpath = 'C://Users//User//Downloads//file.json'


# storing the data
data = {}
def read_csv():
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Name']
            data[key] = rows

# write data into a new json file

    with open(jsonpath, 'w',  encoding='utf-8') as jsonFile:
        # adding enugh spaces for readability.
        jsonFile.write(json.dumps(data, indent=4))

read_csv()
