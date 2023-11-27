# Contains utility functions
import tkinter
import io
import json
import asyncio
import threading
import os
import pickle
from pathlib import Path

def create_window(name):
    window = tkinter.Tk()
    window.title(f'OSINT Dashboard - {name}')
    window.minsize(400, 200)
    return window

def write_data(filename, data):
    Path("data").mkdir(exist_ok=True)
    with io.open(f"data/{filename}", "w") as file:
        json.dump(data, file, indent=2)

def async_result(function):
    threading.Thread(
        target=lambda loop: loop.run_until_complete(function),
        args=(asyncio.new_event_loop(),)
    ).start()

'''
Loads an object from a file with name
'''
def do_unpickle(name):
    result = None
    try:
        with io.open(f".{name}.pkl", "rb") as pickle_file:
            result = pickle.load(pickle_file)
    except:
        return None
    return result

'''
Writes an object to a file with name
'''
def do_pickle(name, data):
    with io.open(f".{name}.pkl", "wb") as pickle_file:
        pickle.dump(data, pickle_file, pickle.HIGHEST_PROTOCOL)