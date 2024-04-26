import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import vlc
from customtkinter import *


class YouTubePlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Player")
        self.root.geometry("400x250")  # Set window size
        self.root.configure(bg="#282828")  # Set background color

        self.url_label = tk.Label(root, text="Enter YouTube URL:", fg="white", bg="#282828", font=("Helvetica", 10))
        self.url_label.pack(pady=(10, 0))

        self.url_entry = tk.Entry(root, width=40, bg="#383838", fg="white", font=("Helvetica", 10))
        self.url_entry.pack(pady=5)

        button_frame = tk.Frame(root, bg="#282828")
        button_frame.pack(pady=5)

        self.play_button = tk.Button(button_frame, text="▶ Play", command=self.play_audio, bg="#4CAF50", fg="white", font=("Helvetica", 10))
        self.play_button.pack(side=tk.LEFT, padx=(10, 5))

        self.pause_button = tk.Button(button_frame, text="⏸ Pause", command=self.pause_audio, state=tk.DISABLED, bg="#FFA500", fg="white", font=("Helvetica", 10))
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(button_frame, text="⏹ Stop", command=self.stop_audio, state=tk.DISABLED, bg="#f44336", fg="white", font=("Helvetica", 10))
        self.stop_button.pack(side=tk.LEFT, padx=(5, 10))

        self.volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, bg="#282828", fg="white")
        self.volume_scale.set(50)  # Default volume
        self.volume_scale.pack(pady=(10, 0))

        self.media = None
        self.playback_position = 0  # To store playback position

    def play_audio(self):
        url = self.url_entry.get()
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            if self.media:
                self.media.stop()
            self.media = vlc.MediaPlayer(stream.url)
            if self.playback_position > 0:  # If resuming from a paused position
                self.media.set_time(self.playback_position)  # Seek to the stored position
            self.media.audio_set_volume(self.volume_scale.get())  # Set initial volume
            self.media.play()
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.root.after(100, self.check_stop)
        except Exception as e:
            self.show_message("An error occurred: " + str(e))

    def pause_audio(self):
        if self.media:
            self.playback_position = self.media.get_time()  # Store playback position
            self.media.pause()
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)

    def stop_audio(self):
        if self.media:
            self.media.stop()
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)

    def set_volume(self, volume):
        if self.media:
            self.media.audio_set_volume(int(volume))

    def check_stop(self):
        if self.media is not None:
            state = self.media.get_state()
            if state == vlc.State.Ended or state == vlc.State.Error:
                self.media.stop()
                self.media = None
                self.play_button.config(state=tk.NORMAL)
                self.pause_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.DISABLED)
                self.show_message("Playback stopped")
            else:
                self.root.after(100, self.check_stop)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubePlayerApp(root)
    root.mainloop()
