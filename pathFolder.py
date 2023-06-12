import os


def path_folder(final_name):    
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    # Create the path to the youtube_down folder
    youtube_down_folder = os.path.join(downloads_folder, "YazLoader")
    
    if not os.path.exists(youtube_down_folder):
    
        os.makedirs(youtube_down_folder)

    playlist_OR_video_path = os.path.join(youtube_down_folder, final_name)

    if not os.path.exists(playlist_OR_video_path):
        os.makedirs(playlist_OR_video_path)
    return playlist_OR_video_path
