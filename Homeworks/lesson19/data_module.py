# data_module.py
import numpy as np

def generate_data():

    X = np.linspace(0, 10, 100)  # 100 точок від 0 до 10
    Y = np.sin(X)
    return X, Y
