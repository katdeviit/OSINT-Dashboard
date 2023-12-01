import tkinter
from . import util
from TikTokApi import TikTokApi
from tkinter import messagebox
from tkinter import ttk

# Stores data for next use
class TikTokFields:
    def __init__(self, username, ms_token):
        self.username = username
        self.ms_token = ms_token

bar = None
progress = None

def open():
    print("Opening TikTok")

    unpickled = util.do_unpickle("tiktok")
    if unpickled == None:
        unpickled = TikTokFields("", "")

    window = util.create_window("TikTok")
    tkinter.Label(window, text="Get 'msToken' from TikTok website cookies after signing in and enter here:").pack()
    text = tkinter.Text(window, height = 1, width = 50)
    text.insert(tkinter.INSERT, unpickled.ms_token)
    text.pack()

    tkinter.Label(window, text="Username to retrieve:").pack()
    text_user = tkinter.Text(window, height = 1, width = 50)
    text_user.insert(tkinter.INSERT, unpickled.username)
    text_user.pack()

    
    tkinter.Button(window, text="Get Data", command=lambda : on_click(text_user, text, window)).pack()

def on_click(text_user, text, window):
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
    msToken = text.get(1.0, "end-1c")
    window.destroy()
    util.async_result(get_user_info(username, msToken))

async def get_user_info(username, ms_token):
    global bar
    global progress
    util.do_pickle("tiktok", TikTokFields(username, ms_token))
    print(f"username: {username}")
    print(f"ms_token: {ms_token}")
    async with TikTokApi() as api:
        try:
            if bar is not None:
                progress.set(10)
            await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False, override_browser_args=["--incognito"])
            if bar is not None:
                progress.set(40)
            data = await api.user(username=username).info()
            if bar is not None:
                progress.set(90)
            #print(await api.user(sec_uid=data["userInfo"]["user"]["secUid"]).following())
            id_x = data["userInfo"]["user"]["id"]
            fname = f"tiktok-user-{id_x}.json"
            util.write_data(fname, data)
            if bar is not None:
                progress.set(100)
            messagebox.showinfo("Success!", f"Successfully retrieved profile information. Saved to {fname}")
            if bar is not None:
                bar.destroy()
                bar = None
        except Exception as e:
            print(e)
            if e == "TikTokException.__init__() missing 2 required positional arguments: 'raw_response' and 'message'":
                print("Try retrieving a new msToken after refreshing page, it may have changed.")
                print("You may have also been rate limited by TikTok. Try changing your IP via a VPN.")
            if bar is not None:
                bar.destroy()
                bar = None
            messagebox.showerror("Error", "Error retrieving profile. See console output for error.")
          