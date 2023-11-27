import tkinter
from . import util
from TikTokApi import TikTokApi
from tkinter import messagebox

# Stores data for next use
class TikTokFields:
    def __init__(self, username, ms_token):
        self.username = username
        self.ms_token = ms_token

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

    
    tkinter.Button(window, text="Get Data", command=lambda : util.async_result(get_user_info(text_user.get(1.0, "end-1c"), text.get(1.0, "end-1c")))).pack()

async def get_user_info(username, ms_token):
    util.do_pickle("tiktok", TikTokFields(username, ms_token))
    print(f"username: {username}")
    print(f"ms_token: {ms_token}")
    async with TikTokApi() as api:
        try:
            await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False, override_browser_args=["--incognito"])
            data = await api.user(username=username).info()
            id_x = data["userInfo"]["user"]["id"]
            fname = f"tiktok-user-{id_x}.json"
            util.write_data(fname, data)
            messagebox.showinfo("Success!", f"Successfully retrieved profile information. Saved to {fname}")
        except Exception as e:
            print(e)
            if e == "TikTokException.__init__() missing 2 required positional arguments: 'raw_response' and 'message'":
                print("Try retrieving a new msToken after refreshing page, it may have changed.")
                print("You may have also been rate limited by TikTok. Try changing your IP via a VPN.")
            messagebox.showerror("Error", "Error retrieving profile. See console output for error.")
          