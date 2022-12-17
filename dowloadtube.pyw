from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
import threading
from colorama import Fore
import pyfiglet

def download_video():
    
    try:
        video_link = url_entry.get()
        resolution = video_resolution.get()
        if resolution == '' and video_link == '':
            showerror(title='Error', message='Please enter both the video URL and resolution!!')
        elif resolution == '':
            showerror(title='Error', message='Please select a video resolution!!') 
        elif resolution == 'None':
            showerror(title='Error', message='None is an invalid video resolution!!\n'\
                    'Please select a valid video resolution')     
        else:
            try:   
                def on_progress(stream, chunk, bytes_remaining):
                    total_size = stream.filesize   
                    def get_formatted_size(total_size, factor=1024, suffix='B'):
                        for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
                            if total_size < factor:
                                return f"{total_size:.2f}{unit}{suffix}"
                            total_size /= factor
                        return f"{total_size:.2f}Y{suffix}"
                    
                    formatted_size = get_formatted_size(total_size)
                    # the size downloaded after the start
                    bytes_downloaded = total_size - bytes_remaining
                    # the percentage downloaded after the start
                    percentage_completed = round(bytes_downloaded / total_size * 100)
                    # updating the progress bar value
                    progress_bar['value'] = percentage_completed
                    # updating the empty label with the percentage value
                    progress_label.config(text=str(percentage_completed) + '%, File size:' + formatted_size)
                    # updating the main window of the app
                    window.update()
                
                # creating the YouTube object and passing the the on_progress function
                video = YouTube(video_link, on_progress_callback=on_progress)
                # downlaoding the actual video  
                video.streams.filter(res=resolution).first().download()
                # popup for dispalying the video downlaoded success message
                showinfo(title='Download Complete', message='Video has been downloaded successfully.')
                
                # ressetting the progress bar and the progress label
                progress_label.config(text='')
                progress_bar['value'] = 0
            # the except will run when the resolution is not available or invalid
            except:
                showerror(title='Download Error', message='Failed to download video for this resolution')
                # ressetting the progress bar and the progress label
                progress_label.config(text='')
                progress_bar['value'] = 0
    # the except statement to catch errors, URLConnectError, RegMatchError  
    except:
        # popup for displaying the error message
        showerror(title='Download Error', message='An error occurred while trying to ' \
                    'download the video\nThe following could ' \
                    'be the causes:\n->Invalid link\n->No internet connection\n'\
                     'Make sure you have stable internet connection and the video link is valid')
        # ressetting the progress bar and the progress label
        progress_label.config(text='')
        progress_bar['value'] = 0
        

# function for searching video resolutions
def searchResolution():
    # getting video url from entry
    video_link = url_entry.get()
    # checking if the video link is empty
    if video_link == '':
        showerror(title='Error', message='Provide the video link please!')
    # if video link not empty search resolution  
    else:
        try:
            # creating a YouTube object
            video = YouTube(video_link)
            # an empty list that will hold all the video resolutions
            resolutions = []
            # looping through the video streams
            for i in video.streams.filter(file_extension='mp4'):
                # adding the video resolutions to the resolutions list
                resolutions.append(i.resolution)
            # adding the resolutions to the combobox
            video_resolution['values'] = resolutions
            # when search is complete notify the user
            showinfo(title='Search Complete', message='Check the Combobox for the available video resolutions')
        # catch any errors if they occur  
        except:
            # notify the user if errors are caught
            showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link')


# the function to run the searchResolution function as a thread
def searchThread():
    t1 = threading.Thread(target=searchResolution)
    t1.start()
    
    
# the function to run the download_video function as a thread   
def downloadThread():
    t2 = threading.Thread(target=download_video)
    t2.start()


# creates the window using Tk() fucntion
window = Tk()

# creates title for the window
window.title('DOWLOADTUBE')
# dimensions and position of the window
window.geometry('500x460+430+180')
# makes the window non-resizable
window.resizable(height=FALSE, width=FALSE)
# creates the canvas for containing all the widgets
canvas = Canvas(window, width=500, height=400)
canvas.pack()
"""Styles for the widgets"""
W= ttk.Label(window, text="DOWLOADTUBE", anchor='center')
W.pack()
# style for the label
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('Courier', 15))
# style for the entry
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# style for the button
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='Helvetica')
# creating a ttk label
url_label = ttk.Label(window, text='Enter Video URL:', style='TLabel')
# creating a ttk entry
url_entry = ttk.Entry(window, width=76, style='TEntry')
# adding the label to the canvas
canvas.create_window(114, 200, window=url_label)
# adding the entry to the canvas
canvas.create_window(250, 230, window=url_entry)
# creating resolution label
resolution_label = Label(window, text='Resolution:')
# adding the label to the canvas
canvas.create_window(50, 260, window=resolution_label)
# creating a combobox to hold the video resolutions
video_resolution = ttk.Combobox(window, width=10)
# adding the combobox to the canvas
canvas.create_window(60, 280, window=video_resolution)
# creating a button for searching resolutions
search_resolution = ttk.Button(window, text='Search Resolution', command=searchThread)
# adding the button to the canvas
canvas.create_window(85, 315, window=search_resolution)
# creating the empty label for displaying download progress
progress_label = Label(window, text='')
# adding the label to the canvas
canvas.create_window(240, 360, window=progress_label)
# creating a progress bar to display progress
progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=450, mode='determinate')
# adding the progress bar to the canvas
canvas.create_window(250, 380, window=progress_bar)
# creating the button
download_button = ttk.Button(window, text='Download Video', style='TButton', command=downloadThread)
# adding the button to the canvas
canvas.create_window(240, 410, window=download_button)
# runs the window infinitely
window.mainloop()