import tkinter as tk
import powerhour

def startScript():
    powerhour.gui(txtPlaylist.get())

    #Root Setup
root = tk.Tk()
root.title("Power Hour")
root.maxsize(1000, 800)

#Setup
lblPlaylist = tk.Label(root, text="Enter a Playlist URL:")
lblPlaylist.grid(row=0, column=0, padx=10, pady=10)

txtPlaylist = tk.Entry(root)
txtPlaylist.grid(row=1, column=0, padx=10, pady=10)

btnPlay = tk.Button(root, text="POWER HOUR!", command=startScript)
btnPlay.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()