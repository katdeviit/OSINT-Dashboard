import tkinter
from . import util
from tkinter import messagebox
from tkinter import ttk
from twitter.scraper import Scraper
from twitter.util import init_session

# Stores data for next use
class XFields:
    def __init__(self, username):
        self.username = username

bar = None
progress = None

def open():
    print("Opening TikTok")

    unpickled = util.do_unpickle("X")
    if unpickled == None:
        unpickled = XFields("")

    window = util.create_window("X")

    tkinter.Label(window, text="Username to retrieve:").pack()
    text_user = tkinter.Text(window, height = 1, width = 50)
    text_user.insert(tkinter.INSERT, unpickled.username)
    text_user.pack()

    
    tkinter.Button(window, text="Get Data", command=lambda : on_click(text_user, window)).pack()

def on_click(text_user, window):
    global bar
    global progress
    if bar is not None:
        bar.destroy()
        bar = None
    progress = tkinter.IntVar()
    bar = ttk.Progressbar(variable=progress)
    progress.set(5)
    bar.place(x=45, y=145, width=300)
    username = text_user.get(1.0, "end-1c")
    window.destroy()
    get_user_info(username)

def get_user_info(username):
    global bar
    global progress
    util.do_pickle("X", XFields(username))
    try:
        print(f"username: {username}")
        if bar is not None:
            progress.set(10)
        scraper = Scraper(session=init_session())
        if bar is not None:
            progress.set(20)
        users = scraper.users([username])
        if bar is not None:
            progress.set(50)
        
        data = users[0]["data"]["user"]["result"]
        id_x = data["rest_id"]

        # Need actual user account for this
        #following = scraper.following([id_x])
        #print(following)

        if bar is not None:
            progress.set(90)

        fname = f"x-user-{id_x}.json"
        util.write_data(fname, data)
        if bar is not None:
            progress.set(100)
        messagebox.showinfo("Success!", f"Successfully retrieved profile information. Saved to {fname}")
        bar.destroy()
        bar = None
    except Exception as e:
        print(e)
        bar.destroy()
        bar = None
        messagebox.showerror("Error", "Error retrieving profile. See console output for error.")
          