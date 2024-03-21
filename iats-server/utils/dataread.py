"""
To read data from csv files (project specific)
NB: @staticmethod - denotes that the function belongs to the class and not to instance of the class...
"""
import csv 

class ReadDataset:
    """Path must be passed using os module"""
    @staticmethod
    def readFromCsv(PATH : str) -> list:
        try:
            dataset = []
            with open(PATH, 'r', newline='') as file:
                csvfile = csv.reader(file)
                for row in csvfile:
                    dataset.append(tuple(row))
            if file:
                file.close()
            return dataset
        except Exception as err:
            print(f'Something went wrong ReadDataset.readFromCsv(), {err}')
            return err