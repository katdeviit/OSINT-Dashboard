@echo off
for /f "delims=" %%a in ('where pip3') do (
    set PIP=%%a
)
for /f "delims=" %%a in ('where py') do (
    set PYTHON=%%a
)
for /f "delims=" %%a in ('where python3') do (
    set PYTHON3=%%a
)

if [%PIP] NEQ [] (
    pip3 install -r requirements.txt
) else (
    pip install -r requirements.txt
)

if [%PYTHON] NEQ [] (
    py -m playwright install
    py dashboard.py
) else if [%PYTHON3] NEQ [] (
    python3 -m playwright install
    python3 dashboard.py
) else (
    python -m playwright install
    python dashboard.py
)

PAUSE