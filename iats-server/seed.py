"""Seed the database with data (project specific) for reproducability"""
import os 
from utils import ReadDataset

""" Get the job applications dataset """
DATASETPATH = os.path.join('dataset', 'jobapplications01.csv')
dataset = []
dataset.append(ReadDataset.readFromCsv(DATASETPATH))

""" Seed users table """