from nested__data import albums

#You can assign a variable to an index number so you don't have to remember the index position everytime you need certain
# data
#(as long as the index position of that specific piece of data won't change). For example the index postiong of the songs
# list (list) is index 3 in albums
#below code allows an easier way to find this data than remember index position.
SONGS_LISTS_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album(invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}:".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LISTS_INDEX]
    else:
        break

    print("PLEASE CHOOSE YOUR SONG:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}:".format(index + 1, song))

    song_choice = int(input())
    if 1<= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        break

    print("now playing: {}".format(title))
    print("=" * 40)

# album = albums[3, 2, 1, 0]
# title = album[0, 1, 2]
# song = title[0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# if choice == (1,2,3,4,5,6,7,8):
#     print("now playing")


