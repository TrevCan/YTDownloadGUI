from pytube import YouTube
from tkinter import *
import tkinter.filedialog

root = Tk()

e = Entry(root, width=150, bg='black', fg="green", border=9)
e.pack()


def download_click():
    video_link = e.get()
    video = YouTube(video_link)
    file_opt = options = {}
    options['filetypes'] = [('All Files', '.*'), ('MP4 Files', '.mp4')]
    options['initialfile'] = video.title + '.mp4'
    options['parent'] = root
    filename = tkinter.filedialog.asksaveasfilename(**file_opt)
    label = Label(root, text='File: ' + filename).pack()

    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=filename)



def main():
    root.mainloop()


downloadButton = Button(root, text='Download video', command=download_click)
downloadButton.pack()

if __name__ == "__main__":
    main()
