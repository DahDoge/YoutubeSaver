#!/bin/env python3

from pytube import YouTube
import tkinter as tk
import os
from tkinter import ttk

def quit_app():
    root.destroy()

def search_video():
    query = str(query_box.get())
    print(f"Searching youtube with string {query}...")
    # search youtube using ytfind and store it in an object
    ytfind = os.popen("ytfind " + query + "| sed 's/ID: /URL: https:\/\//g'")
    results = ytfind.read()
    # print results
    print(results)

def download_video():
    url = str(url_box.get())
    path = str(path_box.get())
    name = str(name_box.get())
    # Create a youtube object
    video = YouTube(url)

    # Get highest resolution
    video = video.streams.get_highest_resolution()

    # Download video
    print("**********Downloading**********")

    video.download(output_path=path, filename=f"{name}.mp4")

    print("**********Download Complete**********")
    done = tk.Label(root, text="Download Complete!")
    done.configure(fg="red")
    done.configure(font=("Arial", 20))
    done.pack(anchor="w")
    quit = tk.Button(root, text="Quit", command=quit_app)
    quit.pack(anchor="w")

# Create the root window
root = tk.Tk()
# Set font
root.configure(bg="#1a1a1a")
root.option_add("*Font", "Arial 12")
root.option_add("*foreground", "white")
root.option_add("*background", "#1a1a1a")

# Set the size of the window
root.geometry("600x300")

title = tk.Label(root, text="YOUTUBE VIDEO DOWNLOADER!")
title.configure(font=("Arial", 25))
title.pack(anchor="w")

url_name = tk.Label(root, text="Type The Link Here:")
url_name.pack(anchor="w")
url_box = tk.Entry(root)
url_box.pack(anchor="w")

path_name = tk.Label(root, text="Type Save Location Here:")
path_name.pack(anchor="w")
path_box = tk.Entry(root)
path_box.pack(anchor="w")

name_name = tk.Label(root, text="Type Video Name Here:")
name_name.pack(anchor="w")
name_box = tk.Entry(root)
name_box.pack(anchor="w")

query_name = tk.Label(root, text="Search:")
query_name.pack(anchor="w")
query_box = tk.Entry(root)
query_box.pack(anchor="w")

searchbutton = tk.Button(root, text="search!", command=search_video)
searchbutton.pack(anchor="w")

downloadbutton = tk.Button(root, text="Download!", command=download_video)
downloadbutton.pack(anchor="w")

# Run the event loop
root.mainloop()
