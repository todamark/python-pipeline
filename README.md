# `Pipeline` -- Simple data processing through a multi-step pipeline

Avoid repeating code on long data pipelines by creating the flow once and reusing it. 

#### `pipe` - Add a new linear step in the pipeline
###### arguments:
* `fn: (data) => data` The next step in the pipeline

#### `split` - Add a conditional step in the pipeline
###### arguments:
* `check: (data) => boolean` The conditional to check
* `fn_if_true: (data) => data` The pipeline step if check returns true
* `fn_if_false: (data) => data` The pipeline step if check returns false

#### `apply` - Apply the pipeline to some data
###### arguments:
* `data` The data to apply to the pipeline


## Example
```python
data_from_somewhere = {
    "status": 200,
    "result": {
        "number_of_the_day": 100,
        "requests_today": 1
    }
}

def is_valid(data):
    return "status" in data and data["status"] == 200 and "result" in data

def clean(data):
    return data["result"]
    
def decorate(number):
    return f"The number of the day is {number} for some reason"
    
def notify(notification):
    requests.post("https://my-server.com/numberofday", data = { "message": notification })

pipe_cleaner = Pipeline().split(is_valid, clean, lambda data: print(f"Invalid data received: {data}"))

pipe_cleaner.pipe(decorate).pipe(notify).apply(data_from_somewhere)
```

## Test

`python -m unittest discover  -p "*_test.py"`