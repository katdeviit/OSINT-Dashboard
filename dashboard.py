import tkinter
from sources import tiktok
from sources import reddit
from sources import x

"""
Creates and opens the OSINT Dashboard UI.
Attaches methods to open the data source UIs.
"""
def main():
    window = tkinter.Tk()
    window.title("OSINT Dashboard")
    window.minsize(400, 200)

    title = tkinter.Label(window, text="Welcome to OSINT Dashboard!", font='Helvetica 18 bold').pack()
    tkinter.Label(window, text="Please select an option.").pack()
    tkinter.Button(text="TikTok", command=tiktok.open).pack()
    tkinter.Button(text="Reddit", command=reddit.open).pack()
    tkinter.Button(text="X (Twitter)", command=x.open).pack()
    window.mainloop()

if __name__ == "__main__":
    main()