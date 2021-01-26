import pandas as pd
import os
dir_path = "data"
path = os.path.join(dir_path, "201904-citibike-tripdata.csv")
print("Pre-Processing...")
df = pd.read_csv(path)
station_name = 'Christopher St & Greenwich St'

def pre_process_df(df, station_name_col, time_col):
    station_df = df.loc[df[station_name_col] == station_name]
    station_df[time_col] = pd.to_datetime(station_df[time_col],
                                        infer_datetime_format=True)

    dayweek = station_df[time_col].dt.dayofweek.isin([0,1,2,3])
    station_dayweek_df = station_df.loc[dayweek]

    station_dayweek_df = station_dayweek_df.sort_values(time_col)
    time_interval = station_dayweek_df[time_col].diff().dt.total_seconds()
    
    amplitude = time_interval.quantile(0.75) - time_interval.quantile(0.25)
    max_value = time_interval.quantile(0.75) + 3*amplitude
    time_interval_clean = time_interval.loc[time_interval < max_value]

    return time_interval_clean

start_time_interval = pre_process_df(df, 'start station name', 'starttime')
start_time_interval.to_csv(os.path.join(dir_path, "start.csv"), index=False)

end_time_interval = pre_process_df(df, 'end station name', 'stoptime')
end_time_interval.to_csv(os.path.join(dir_path, "end.csv"), index=False)
print("Done")
