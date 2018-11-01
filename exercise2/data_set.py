import numpy as np

class DataSet:
  def __init__(self):
    self.records = []

  def create_from_csv(self, file_path):
    # [4]: education-num
    # [14]: income
    self.records = np.genfromtxt(file_path, delimiter=',', skip_header=1, dtype=None)

  def copy_from_dataset(self, dataset):
    self.records = list(dataset.records)
