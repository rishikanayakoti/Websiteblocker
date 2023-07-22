from cgitb import text
from textwrap import wrap
from tkinter import *
from datetime import datetime as dt
# import time

root = Tk()
root.geometry('500x400')
# root.resizable(0, 0)
root.title("Website Blocker")

# heading
Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').place(x = 125, y = 1)

# label for enter websites
Label(root, text='Enter Website:', font='arial 11').place(x=5, y=60)

# entering websites
Websites = Text(root, font='arial 10', height='1', width='40', wrap=WORD, padx=10, pady=10)
Websites.place(x=110, y=55)

# host file path
host_path = "C://Windows//System32//drivers//etc//hosts"
redirect = "127.0.0.1"

# label for working hours
Label(root, text='Enter Working Hours:', font='arial 11').place(x=5, y=110)

# starting time
Label(root, text='Start time:', font='arial 11').place(x=5, y=150)
start_time = Text(root, font='arial 10', height='1', width='18', wrap=WORD, padx=10, pady=10)
start_time.place(x=85, y=145)

# end time
Label(root, text='End time:', font='arial 11').place(x=240, y=150)
end_time = Text(root, font='arial 10', height='1', width='20', wrap=WORD, padx=10, pady=10)
end_time.place(x=315, y=145)

# 'BLOCKER' function
def BLOCKER():
    websites = Websites.get(1.0, END)
    website_list = list(websites.split(","))
    st = start_time.get(1.0, END)
    et = end_time.get(1.0, END)
    h1, m1, s1 = map(int, st.split(":"))
    h2, m2, s2 = map(int, et.split(":"))
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, h1, m1, s1) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, h2, m2, s2):
            with open(host_path, "r+") as file:
                content = file.read()
                for site in website_list:
                    if site in content:
                        # Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=250)
                        # pass
                        continue
                    else:
                        file.write(redirect + " " + site + "\n")
                        # Label(root, text = "Blocked", font = 'arial 12 bold').place(x=200,y =250)
            print("Websites are blocked")
        else:
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in website_list):
                        file.write(line)
                file.truncate()
            print("All sites are unblocked")
            break
        # time.sleep(5)


# block button
block_btn = Button(root, text='BLOCK', font='arial 12 bold', command=BLOCKER, width=6, bg='royal blue1', activebackground='sky blue')
block_btn.place(x=210, y=210)


root.mainloop()
