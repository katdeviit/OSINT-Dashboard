import tkinter
from tkinter import messagebox, ttk
import asyncpraw
from . import util

class RedditFields:
    def __init__(self, username, client_id, client_secret):
        self.username = username
        self.client_id = client_id
        self.client_secret = client_secret

bar = None
progress = None

def open_reddit():
    print("Opening Reddit")

    unpickled = util.do_unpickle("reddit")
    if unpickled is None:
        unpickled = RedditFields("", "", "")

    window = util.create_window("Reddit")

    tkinter.Label(window, text="Reddit API Client ID:").pack()
    text_ci = tkinter.Text(window, height = 1, width = 50)
    text_ci.insert(tkinter.INSERT, unpickled.client_id)
    text_ci.pack()

    tkinter.Label(window, text="Reddit API Client Secret:").pack()
    text_cs = tkinter.Text(window, height = 1, width = 50)
    text_cs.insert(tkinter.INSERT, unpickled.client_secret)
    text_cs.pack()


    tkinter.Label(window, text="Username to retrieve:").pack()
    text_user = tkinter.Text(window, height=1, width=50)
    text_user.insert(tkinter.INSERT, unpickled.username)
    text_user.pack()

    tkinter.Button(window, text="Get Data", command=lambda: on_click(text_user, text_ci, text_cs, window)).pack()

def on_click(text_user, text_ci, text_cs, window):
    global bar
    global progress

    if bar is not None:
        bar.destroy()
        bar = None
    progress = tkinter.IntVar()
    bar = ttk.Progressbar(variable=progress)
    bar.place(x=45, y=145, width=300)
    username = text_user.get(1.0, "end-1c")
    client_id = text_ci.get(1.0, "end-1c")
    client_secret = text_cs.get(1.0, "end-1c")
    window.destroy()
    util.async_result(get_user_info(username, client_id, client_secret))

async def get_user_info(username, client_id, client_secret):
    global bar
    global fetch_status
    util.do_pickle("reddit", RedditFields(username, client_id, client_secret))
    fname = f"reddit-user-{username}.json"
    user_agent = 'MyRedditApp/1.0 (by /u/yourusername)'
    #print(client_id)
    #print(client_secret)
    try:
        if bar is not None:
            progress.set(10)
        reddit = asyncpraw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        if bar is not None:
            progress.set(30)
        # Fetch the comments and store in a list
        comments_data = []
        redditor = await reddit.redditor(username)
        if bar is not None:
            progress.set(60)
        async for comment in redditor.comments.new(limit=100):
            comments_data.append({"comment": comment.body, "created_at": str(comment.created_utc)})
        if bar is not None:
            progress.set(70)
        util.write_data(fname, comments_data)
        if bar is not None:
            progress.set(100)
        await reddit.close()
        messagebox.showinfo("Success!", f"Successfully retrieved profile information. Saved to {fname}")
        if bar is not None:
            bar.destroy()
            bar = None
    except Exception as e:
        print(e)
        if bar is not None:
            bar.destroy()
            bar = None
        messagebox.showerror("Error", "Error retrieving profile. See console output for error.")
