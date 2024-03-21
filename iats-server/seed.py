"""Seed the database with data (project specific)"""
import os 
from utils import ReadDataset

DATASETPATH = os.path.join('dataset', 'jobapplications01.csv')
"""
print(DATASETPATH)
dataset = []
with open(DATASETPATH, 'r', newline='') as file:
#    csv_reader = csv.reader(csvfile)
#    print(csv_reader)
#    for row in csv_reader:
#        print(row)
    csvfile = csv.reader(file)
    for row in csvfile:
        print(tuple(row))
        dataset.append(tuple(row))

print(dataset[0])
file.close()
"""
dataset = ReadDataset.readFromCsv(DATASETPATH)

print(dataset)