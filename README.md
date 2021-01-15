# Bike Share Demand Modelling

## Install

* Clone the repo
* Go the new rep directory
* ```pip install -e .```

## Usage

```python3
from bike_model.bike_model import BikeModel
bikeModel = BikeModel()

# get interval in minutes
# from the next user who will rent a bike

start_time = bikeModel.next_bike_user('start')

# get interval in minutes
# from the next user who will leave a bike

end_time = bikeModel.next_bike_user('end')
```


