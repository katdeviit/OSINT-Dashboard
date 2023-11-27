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
    py dashboard.py
) else if [%PYTHON3] NEQ [] (
    python3 dashboard.py
) else (
    python dashboard.py
)

PAUSE