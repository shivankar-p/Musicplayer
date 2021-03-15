#!/usr/bin/env python3

from vlcpl import *

# Player instantiation
player = player_wrapper()

op = 0
while (op != 9):
    sleep(1)
    print("Enter option:\n 1: Set playlist\n 2: Play playlist\n 3: Pause playlist\n 4: Stop playlist\n 5. Next in playlist\n 6. Previous in playlist\n 7. Set playback mode\n 8. Play item at index\n 9. Exit")
    op = int(input())

    if op == 1:
        # Take playlist URL
        print("Enter playlist url: ")
        plurl = input()
        # Add playlist
        print("Setting playlist: " + plurl)
        player.setPlaylist(plurl)
        continue

    elif op == 2:
        # Play the song
        print("Playing playlist: " + plurl)
        player.playPlaylist()
        continue

    elif op == 3:
        # Pause the song
        print("Pausing playlist: " + plurl)
        player.pausePlaylist()
        continue

    elif op == 4:
        # Stop the song
        print("Stopping playlist: " + plurl)
        player.stopPlaylist()
        continue

    elif op == 5:
        # Play the next song
        print("Playing next in playlist: " + plurl)
        player.nextInPlaylist()
        continue

    elif op == 6:
        # Previous song
        print("Playing previous in playlist: " + plurl)
        player.previousInPlaylist()
        continue

    elif op == 7:
        # Change playback mode
        print("Enter playbak mode (default, loop, repeat): ")
        mode = input()
        print("Setting " + mode + " playback")
        player.setPlaybackMode(mode)
        continue

    elif op == 8:
        # Play item at index
        print("Enter item number in the playlist to play: ")
        idx = int(input())
        print("Playing item " + str(idx) + " in playlist: " + plurl)
        player.playItemAtIndex(idx)
        continue

    elif op == 9:
        break

