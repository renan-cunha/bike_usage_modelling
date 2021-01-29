import pandas as pd
import os
import numpy as np
import seaborn as sns
from datetime import timedelta
import matplotlib.pyplot as plt
from typing import List

data_dir = "data"

class BikeModel:

    max_number_riders = 10000

    def __init__(self) -> None:
        self.__start_data = pd.read_csv(os.path.join(data_dir,
            "start.csv")).values.flatten()
        self.__end_data = pd.read_csv(os.path.join(data_dir,
            "end.csv")).values.flatten()

    def __get_bike_users_in_interval(self, 
                                     data: np.ndarray, 
                                     time_interval: timedelta) -> List[int]:
    
        result = np.random.choice(data, self.max_number_riders)
        result_cum_sum = np.cumsum(result)
        is_in_time_interval = result_cum_sum <= time_interval.total_seconds()
        result = result[is_in_time_interval]
        if len(result) == self.max_number_riders:
            self.max_number_riders *= 10
            return self.__get_bike_users_in_interval(data, time_interval)
        else:
            return result

    
    def next_bike_user(self, mode: str, time_interval: timedelta) -> List[float]:
        """Gets the bikes users that will appear in the defined time interval
            
            The return is a list like [3, 6, 4, 2, 0...]

            This list reprents the time interval in seconds that a user appears
            after the one before. For example, in this list, the first user
            appeared in the time '3', the second one in the time '9', the third
            one in the time '13', and so on.

            Mode is a input that defines if the users are the ones that are
            taking bikes or delivering. 'start' is a user that is taking bikes. 
            'end' are users that are delivering bikes in the docks.
        """
        if mode not in ['start', 'end']:
            raise ValueError(f"mode should be 'start' or 'end', not {mode}")

        if mode == 'start':
            result = self.__get_bike_users_in_interval(self.__start_data, time_interval)
        else:
            result = self.__get_bike_users_in_interval(self.__end_data, time_interval)
        return result


if __name__ == "__main__":
    bike_model = BikeModel()
    runs = 10000
    time_interval = timedelta(hours=24)
    number_start = []
    number_end = []
    for run in range(runs):
        start_data = bike_model.next_bike_user('start', time_interval)
        end_data = bike_model.next_bike_user('end', time_interval)
        number_start.append(len(start_data))
        number_end.append(len(end_data))
    print(np.mean(number_start), np.std(number_start, ddof=1))
    print(np.mean(number_end), np.std(number_end, ddof=1))
    
