from tkinter import *
from tkinter import ttk

custom_font=('Helvetica',24)
class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.login()
    
    def login(self):

        
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='Solace', font=custom_font)
        self.reg_txt.pack(pady=50)
        self.emotion_btn = ttk.Button(self.frame1, text="Detect Emotion", command=self.detectEmotion)
        self.emotion_btn.pack()
        self.recommendSong_btn = ttk.Button(self.frame1, text="Recommend song", command=self.recommendSong)
        self.recommendSong_btn.pack()
        self.playSong_btn=ttk.Button(self.frame1, text="Song Player", command=self.playSong)
        self.playSong_btn.pack()
    
    def detectEmotion(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='Detect Emotion',font=custom_font)
        self.reg_txt2.pack(pady=70)
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()
        

    def recommendSong(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='Song Recommendation Page',font=custom_font)
        self.reg_txt2.pack(pady=70)
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

    def playSong(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='Song Player',font=custom_font)
        self.reg_txt2.pack(pady=70)
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()    

root = Tk()
app(root)
root.mainloop()