


def filter_name(playlist_OR_video_name):    


    #symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    symbols = '!"#$%&\'*+,/:;<=>|?@[\\]`{^}'
    symbols2 = [*symbols]
    #print(symbols2)

    playlist_OR_video_name2 = list(playlist_OR_video_name)

    for i in playlist_OR_video_name2:
        for m in symbols2:
            if i == m:
                if i == '&':
                    playlist_OR_video_name2[playlist_OR_video_name2.index(i)] = 'and'                
                elif i == ':':
                    playlist_OR_video_name2[playlist_OR_video_name2.index(i)] = '-'
                else:
                    playlist_OR_video_name2.remove(i)

    final_name = ''
    for j in playlist_OR_video_name2:
        final_name += j 
    print(f'\n\nthe final name is:{final_name}')
    return final_name