#!/bin/env python3

from pytube import YouTube
import tkinter as tk

def quit_app():
    root.destroy()

def download_video():
    url = str(url_box.get())
    path = str(path_box.get())
    name = str(name_box.get())
    # Create a youtube object
    video = YouTube(url)

    # Get highest resolution
    video = video.streams.get_highest_resolution()

    #Download video
    print("**********Downloading**********")

    video.download(output_path=path, filename=f"{name}.mp4")

    print("**********Download Complete**********")
    done = tk.Label(root, text="Download Complete!")
    done.configure(fg="red")
    done.configure(font=("Arial", 20))
    done.pack()
    quit = tk.Button(root, text="Quit", command=quit_app)
    quit.pack()


# Create the root window
root = tk.Tk()
#set font
root.configure(bg="#1a1a1a")
root.option_add("*Font", "Arial 12")
root.option_add("*foreground", "white")
root.option_add("*background", "#1a1a1a")

# Set the size of the window
root.geometry("600x300")

title = tk.Label(root, text="YOUTUBE VIDEO DOWNLOADER!")
title.configure(font=("Arial", 25))
title.pack()

url_name = tk.Label(root, text="Type The Link Here:")
url_name.pack()
url_box = tk.Entry(root)
url_box.pack()

path_name = tk.Label(root, text="Type Save Location Here:")
path_name.pack()
path_box = tk.Entry(root)
path_box.pack()

name_name = tk.Label(root, text="Type Video Name Here:")
name_name.pack()
name_box = tk.Entry(root)
name_box.pack()

downloadbutton = tk.Button(root, text="Download!", command=download_video)
downloadbutton.pack()

# Run the event loop
root.mainloop()


