#!/bin/bash
if [[ $(which pip3) != 0 ]]; then
    pip3 install -r requirements.txt
else
    pip install -r requirements.txt
fi


if [[ $(which python3) != 0 ]]; then
    python3 dashboard.py
else
    python dashboard.py
fi
