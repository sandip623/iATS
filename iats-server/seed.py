""" Seed the database with data (project specific) for reproducability. """
import os 
from utils import ReadDataset
from dbutils import MySqlCls, DBCONFIG, UserRepository

""" Get the job applications dataset """
DATASETPATH = os.path.join('dataset', 'jobapplications01.csv')
dataset = []
dataset.append(ReadDataset.readFromCsv(DATASETPATH))

""" Create the tables """
dbinstance = MySqlCls(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
dbinstance.createAllTables()