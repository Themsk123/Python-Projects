# yt_dlp library ko import kar rahe hain.
# Ye videos download karne mein help karti hai.
import yt_dlp


# tkinter ek GUI library hai.
# Isse graphical user interface banaya ja sakta hai.
import tkinter as tk


# filedialog user ko folder select karne ki facility deta hai.
from tkinter import filedialog


# Ye function video ka URL aur save karne ka folder receive karta hai.
def download_video(url, save_path):

    # try block mein wo code likhte hain jahan error aa sakta hai.
    try:

        # yt-dlp ki settings ko dictionary mein define kar rahe hain.
        ydl_opts = {

            # Best MP4 video aur best M4A audio select karne ki koshish karega.
            #
            # Agar ye available nahi hain to MP4 ka best format select karega.
            #
            # Last option mein koi bhi best available format select karega.
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",

            # Downloaded video ka folder aur naam set kar rahe hain.
            #
            # %(title)s = YouTube video ka title.
            #
            # %(ext)s = file extension.
            "outtmpl": save_path + r"\%(title)s.%(ext)s",

            # Video aur audio merge hone ke baad
            # final output MP4 format mein chahiye.
            "merge_output_format": "mp4",
        }


        # YoutubeDL object create kar rahe hain.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            # URL wali video download kar rahe hain.
            ydl.download([url])


        # Download successful hone par message print hoga.
        print("Video downloaded successfully!")


    # Agar koi error aaye to error message print hoga.
    except Exception as e:

        # Actual error ko print karenge.
        print("Error:", e)


url = "https://youtu.be/SGu53S5-Iu8"


# Ye folder hai jahan video download hogi.
save_path = r"C:\Users\lenovo\Python Projects\Project2- Youtube video Downloader"


# Function ko URL aur save path ke saath call kar rahe hain.
download_video(url, save_path)



# README.md content (comments form)
#
# Project Name: YouTube Video Downloader
# Description:
# This project downloads a YouTube video using the yt_dlp library.
# It allows the user to provide a video URL and a save folder, then
# downloads the video in MP4 format whenever possible.
#
# Features:
# - Downloads YouTube videos by URL
# - Saves the file to a selected folder
# - Tries to download best available MP4 video + audio combination
# - Merges audio and video automatically when supported
# - Displays success or error messages in the console
#
# Requirements:
# - Python 3.x
# - yt_dlp library
#
# Installation:
# pip install yt_dlp
#
# How to use:
# 1. Set the video URL in the 'url' variable.
# 2. Set the folder path in the 'save_path' variable.
# 3. Run the script.
# 4. The video will be downloaded to the selected folder.
#
# Example:
# url = "https://youtu.be/SGu53S5-Iu8"
# save_path = r"C:\Users\lenovo\Python Projects\Project2- Youtube video Downloader"
#
# Note:
# - The script may need updates if YouTube changes download behavior.
# - Internet access is required to download videos.
#
# YouTube video ka URL.