# Bike Share Demand Modelling

## Install

* Clone the repo
* Go the new rep directory
* Install the prerequisites 

```
pip install -r requirements.txt
```

## Usage

```
Usage: main.py [OPTIONS]

Options:
  --download / --no-download      Download raw data.
  --extract / --no-extract        Extract data from zip file.
  --pre_process / --no-pre_process
                                  Pre-process data.
  --help                          Show this message and exit.
```

### Download, extract and pre-process in the first use

The raw file has 300 Mb

```python3 main.py --download --extract --pre_process```

### Calling the function

```python3
from bike_model.bike_model import BikeModel
from datetime import timedelta

bikeModel = BikeModel()

# get interval in seconds, from users that will arrive in the span of 2 hours

time_interval = timedelta(hours=2)

start_time = bikeModel.next_bike_user('start', time_interval)
# start_time equals to array([3, 2])

end_time = bikeModel.next_bike_user('end', time_interval)
# start_time equals to array([1, 0, 0])
```


