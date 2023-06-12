
# create code to download video 
# create gui 
# deleate url after download the video 
# print error if user dont set url valed or dont set url 

import os
import pytube
from pytube import Playlist
from tqdm import tqdm
from pytube import YouTube
import time

from colored import fg, bg, attr
import pyfiglet

# import files names filter and path folder
import namesFilter
import pathFolder

def main():
    # print progress bar at run file
    for x in tqdm(range(100)):
        time.sleep(0.01)
        
    # code goes here   
    while True: 
        color = fg('green')
        res = attr('reset',)
        print('\n\n')
        logo = "YazLoader"
        
        print(color + pyfiglet.figlet_format(logo) + res)
    
        info = """\033[1;32m
        developed by:   yazeed bani issa 
        github:         https://github.com/yazeedb95
        linkedin:       https://www.linkedin.com/in/yazeedb91/
        ====================================================


        1- Enter the URL of the video OR play list you want to download
        2- Press Q to exit
        """
        print(info)
        
        # Enter the YouTube playlist URL
        URL = input(" ->> ")


        if 'playlist?list=' in  URL:        

            # Create a PyTube playlist object
            playlist = pytube.Playlist(URL)

            # Get the name of the playlist
            playlist_name = playlist.title
            print(playlist_name, f'\ntype name is:{type(playlist_name)}')
            final_name = filter_name(playlist_name)

            playlist_path = path_folder(final_name)

            # Iterate through all the videos in the playlist and download them
            for video_url in tqdm(playlist.video_urls, desc="Downloading"):
                # Create a PyTube video object
                video = pytube.YouTube(video_url)

                # Choose the highest resolution stream
                stream = video.streams.get_highest_resolution()

                file_name = stream.default_filename
                file_path = os.path.join(playlist_path, file_name)
                if os.path.exists(file_name):
                    tqdm.write(f"Video {file_name} already exists. Skipping download.")
                else:
                # Download the video to the directory with a progress bar
                    stream.download(playlist_path)


        elif 'watch?v=' in  URL:
            video_filename = YouTube(URL).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().default_filename
            print(f"video name is: {video_filename}")

            # size = YouTube(URL).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            # print(f'size video is:{size}')
            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            # Create the path to the youtube_down folder
            youtube_down_folder0 = os.path.join(downloads_folder, "youtube_videos")
            youtube_down_folder = os.path.join(youtube_down_folder0, "videos")
            
            if not os.path.exists(youtube_down_folder):    
                os.makedirs(youtube_down_folder)

            # Download the video
            yt = YouTube(URL)            

            tqdm(yt.video_id, desc="Downloading")    
            stream = yt.streams.get_highest_resolution()
            stream.download(youtube_down_folder)

            print("Video downloaded successfully to:", youtube_down_folder)
            print("Video filename:", os.path.basename(video_filename))
        elif 'q' == URL or 'Q' == URL: 
            break
        else: print('error! Enter a valid download URL or Q to exit')


    


if __name__ == "__main__":
    main()

