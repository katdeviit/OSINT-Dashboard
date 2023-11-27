import tkinter
import tiktok
import reddit
import x

window = tkinter.Tk()
window.title("OSINT Dashboard")
window.minsize(400, 200)

title = tkinter.Label(window, text="Welcome to OSINT Dashboard!", font='Helvetica 18 bold').pack()
tkinter.Label(window, text="Please select an option.").pack()
tkinter.Button(text="TikTok", command=tiktok.open).pack()
tkinter.Button(text="Reddit", command=reddit.open).pack()
tkinter.Button(text="X (Twitter)", command=x.open).pack()
window.mainloop()