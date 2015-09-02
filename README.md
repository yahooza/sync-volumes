# Sync volumes
How I keep multiple copies of my data in sync


## Configuration options
The  ```mount``` key is where all volumes reside. For simplicity, tis a single location.

The ```actives``` key all of synced volumes, where each key is the 'master' and its value is an array of 'slaves'

In the example config below, ```Devastator```'s data will be synced to ```Scapper```, ```Bonecrusher```, ```Mixmaster```, etc.


```
config = {
    "mount": "/tmp/sync",
    "actives": {
      "Devastator" : [
        "Scrapper",
        "Hook",
        "Bonecrusher",
        "Longhaul",
        "Mixmaster",
        "Scavenger"
      ],
      "Voltron": [
        "Black",
        "Blue",
        "Green",
        "Red",
        "Yellow"
      ]
    }
  }
  ```

## Unit Test

```py.test test_sync.py```
