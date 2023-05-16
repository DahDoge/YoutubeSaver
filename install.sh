#!/bin/sh

#install dependencies
pip install -r requirements.txt

# symlink yt_downloader.py to /bin/yt_downloader
sudo ln -s $PWD/yt_downloader.py /bin/yt_downloader

# make /bin/yt_downloader executable
sudo chmod +x /bin/yt_downloader
