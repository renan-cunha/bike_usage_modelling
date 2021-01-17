import subprocess
import requests
import os

url = 'https://s3.amazonaws.com/tripdata/201904-citibike-tripdata.csv.zip'
print("Downloading Data...")

r = requests.get(url, allow_redirects=True)



subprocess.run(["mkdir", "-p", "data"])
path = os.path.join("data", "data.zip")
open(path, 'wb').write(r.content)
print("Download completed")


