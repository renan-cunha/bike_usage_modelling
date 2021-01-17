import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List

data_dir = "data"


class BikeModel:

    def __init__(self) -> None:
        self.__start_data = pd.read_csv(os.path.join(data_dir,
            "start.csv")).values.flatten()
        self.__end_data = pd.read_csv(os.path.join(data_dir,
            "end.csv")).values.flatten()

    
    def next_bike_user(self, mode: str, size: int = 1) -> List[float]:
        if mode not in ['start', 'end']:
            raise ValueError(f"mode should be 'start' or 'end', not {mode}")

        if mode == 'start':
            result = np.random.choice(self.__start_data, size)
        else:
            result = np.random.choice(self.__end_data, size)
        return result


if __name__ == "__main__":
    bike_model = BikeModel()
    start_data = bike_model.next_bike_user('start', size=10000)
    end_data = bike_model.next_bike_user('end', size=10000)
    sns.histplot(start_data)
    plt.show()
    sns.histplot(end_data)
    plt.show()
    
