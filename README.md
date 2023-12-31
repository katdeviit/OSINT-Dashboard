# OSINT Dashboard

This dashboard retrieves information from various API sources and saves it to a file.

Current sources:

- TikTok
- Reddit
- X (Twitter)

## Usage

Install [Python 3.11 or higher](https://www.python.org/)

**Execute `run.bat` or `run.sh`**, or alternatively try the "Commands" section.

Select an option and enter a username to analyze. The results will be saved to a file in the working directory.

### Commands

Install the dependencies via `pip`. Install playwright's additional dependencies for TikTok support.

Run `dashboard.py`, either with command line or through opening with Python.

```sh
pip install -r requirements.txt
python -m playwright install
python dashboard.py
```

Or the following (depends on system configuration):

```sh
pip3 install -r requirements.txt
python3 -m playwright install
python3 dashboard.py
```
