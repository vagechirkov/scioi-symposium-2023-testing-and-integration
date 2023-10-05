# SCIoI Symposium 2023: Python Testing and Integration

## Task

We want to implement simple statistical functions (median, mean, variance) and **make sure** they work as expected.
We use the `pytest` framework to write and execute tests for our functions.

# Setup

## Step 1: clone the repository

```bash
git clone
```

## Step 2: create a virtual environment

```bash
python3 -m venv venv
```

## Step 3: activate the virtual environment

```bash
source venv/bin/activate
```

## Step 4: install the dependencies

```bash
pip install -r requirements.txt
```

## Step 5: run the tests

```bash
pytest
```

<details>
<summary>Click to expand the expected output of running pytest command</summary>

```bash
============================================================================== test session starts ==============================================================================
platform [your platform]
rootdir: [your path]/scioi_symposium_2023_python_testing_and_integration
collected 1 item                                                                                                                                                                

test_my_stats.py .                                                                                                                                                        [100%]

=============================================================================== 1 passed in 0.00s ===============================================================================

```

</details>


## Step 6: run test coverage

```bash
 pytest -v --cov-report html:cov_html --cov=my_stats
```