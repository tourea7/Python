from pytube import YouTube
from colorama import Fore
import pyfiglet

#style du titre
title=pyfiglet.figlet_format("DOWLOADTUBE")
print(f'{Fore.RED}{title}')


def video_downloader(video_url):

    my_video = YouTube(video_url)
    my_video.streams.get_highest_resolution().download()
    return my_video.title

try:
    print("*"*100)    
    youtube_link = input(f'{Fore.CYAN} Entrer le lien Youtube:')
    print("*"*100)
    print("\n")
    print("*"*100)
    print(f'{Fore.CYAN} votre video en cours de telecharchement, veuillez patienter svp.......')
    print("*"*100)
    print("\n")
    print("*"*100)
    video = video_downloader(youtube_link)
    print(f'"{video}"{Fore.CYAN} telechargement reussi!!')
    print("*"*100)
    print("\n")
except:
    print("\n")
    print("*"*100)
    print(f'{Fore.RED} Failed to download video\nThe '\
          'following might be the causes\n->No internet '\
          'connection\n->Invalid video link')
    print("*"*100)
    print("\n")
# YouTube(url).streams.filter(res="360p").first().download()
#YouTube(url).streams.first().download()