"""Seed the database with data (project specific)"""
import os 
from utils import ReadDataset

""" Get the dataset """
DATASETPATH = os.path.join('dataset', 'jobapplications01.csv')
dataset = []
dataset.append(ReadDataset.readFromCsv(DATASETPATH))

print((dataset))