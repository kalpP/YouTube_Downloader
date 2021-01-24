from tkinter import *
from tkinter import filedialog as fdialog, ttk
from pytube import YouTube

# Choose/Change the File Path
global download_path
BACKGROUND_COLOR = '#272822'
ERROR_COLOR = '#99334f'
TITLE_COLOR = '#ffffff'
SUCESS_COLOR = '#a6e22e'
MISC_COLOR = '#ffff00'

def SelectFilePath():
    download_path = fdialog.askdirectory()
    download_path.replace(' ', '')
    if(len(download_path) < 2):
        locationError.config(text = 'Please select the download location!', fg = 'red')
    else:
        locationError.config(text = download_path, fg = 'green')

#donwload video
def DownloadVideoOrAudio():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Please try pasting the link again",fg="red")


    #download function
    select.download(download_path)
    ytdError.config(text="Download Complete!")

root = Tk()
root.title("YTD Downloader")
root.configure(background = BACKGROUND_COLOR)
root.geometry("500x500") #set window
root.columnconfigure(0, weight = 1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root, text = 'Enter the Video URL', bg = BACKGROUND_COLOR, fg = TITLE_COLOR, font = ('jost', 15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width = 50, bg = BACKGROUND_COLOR, fg = TITLE_COLOR, textvariable = ytdEntryVar)
ytdEntry.config(highlightbackground = BACKGROUND_COLOR)
ytdEntry.grid()

#Error Msg
ytdError = Label(root, text = '', bg = BACKGROUND_COLOR, fg=ERROR_COLOR, font = ('jost', 15, 'bold'))
ytdError.grid()

#Asking save file label
saveLabel = Label(root, text = 'Save the Video File', bg = BACKGROUND_COLOR, fg = TITLE_COLOR, font = ('jost', 15, 'bold'))
saveLabel.grid()


#btn of save file
saveEntry = Button(root, font = ('jost', 14, 'bold'), highlightbackground = BACKGROUND_COLOR, fg = MISC_COLOR, text = 'Choose Path', command = SelectFilePath)
saveEntry.grid()

#Error Msg location
locationError = Label(root, text = '', bg = BACKGROUND_COLOR, fg=ERROR_COLOR, font = ('jost', 15))
locationError.grid()

#Download Quality
ytdQuality = Label(root, text = 'Select Download Type', bg = BACKGROUND_COLOR, fg = TITLE_COLOR, font = ('jost', 15))
ytdQuality.grid()

#combobox
choices = ['Video', 'Audio']
ytdchoices = ttk.Combobox(root, values = choices)
ytdchoices.grid()

#spacer
spacer = Label(root, text = '', bg = BACKGROUND_COLOR, font = ('jost', 3))
spacer.grid()

#donwload btn
downloadbtn = Button(root, font = ('jost', 14, 'bold'), highlightbackground = BACKGROUND_COLOR, fg = MISC_COLOR, text = 'Download', command = DownloadVideoOrAudio)
downloadbtn.grid()

root.mainloop()