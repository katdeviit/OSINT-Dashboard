import tkinter

window = tkinter.Tk()
window.title("OSINT Dashboard")
window.minsize(400, 200)

title = tkinter.Label(window, text="Welcome to OSINT Dashboard!", font='Helvetica 18 bold').pack()
tkinter.Label(window, text="Please select an option.").pack()
tkinter.Button(text="TikTok").pack()
tkinter.Button(text="Reddit").pack()
tkinter.Button(text="X (Twitter)").pack()
window.mainloop()