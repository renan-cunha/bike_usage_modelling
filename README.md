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
bikeModel = BikeModel()

# get interval in minutes
# from the next user who will rent a bike

start_time = bikeModel.next_bike_user('start')
# start_time equals to array([0.95468333])

start_time = bikeModel.next_bike_user('start', size=2)
# start_time equals to array([0.95468333, 1.256677])

# get interval in minutes
# from the next user who will leave a bike

end_time = bikeModel.next_bike_user('end', size=1)
```


