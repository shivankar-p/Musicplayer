#!/usr/bin/env python3

import requests
from vlc import Instance
from vlc import PlaybackMode
from time import sleep
import os


class playerwrapper(object):

    playlists = set(['pls','m3u'])

    def __init__(self):
        self.vlc = Instance("--no-video")
        self.listPlayer = self.vlc.media_list_player_new()

    @staticmethod
    def extract_song_ids(playlist_name):
        return ['kJQP7kiw5Fk', '60ItHLz5WEA', 'kffacxfA7G4']

    def setPlaylist(self, url):
        ext = (url.rpartition(".")[2])[:3]
        valid = 'Invalid'
        try:
            if url.startswith('playlist://'):
                valid = 'Application'
            elif url.startswith('http://') or url.startswith('https://'):
                ret = requests.get(url, stream=True)
                if ret.ok:
                    valid = 'Web'
            elif url.startswith('file:///'):
                valid = 'Local'
        except Exception as e:
            print('Failed to get stream: {e}'.format(e=e))
            valid = False
        else:
            if valid == 'Application':
                playlist_name = url[len('playlist://') - 1:]
                songs = playerwrapper.extract_song_ids(playlist_name)
                self.mediaList = self.vlc.media_list_new()
                for song_id in songs:
                    self.mediaList.add_media(self.vlc.media_new('https://www.youtube.com/watch?v=' + song_id))
            elif valid == 'Web':
                if ext in playerwrapper.playlists:
                    self.mediaList = self.vlc.media_list_new([url])
            elif valid == 'Local':
                path = url[len('file:///') - 1:]
                songs = os.listdir(path)
                self.mediaList = self.vlc.media_list_new()
                for s in songs:
                    self.mediaList.add_media(self.vlc.media_new(os.path.join(path,s)))
            else:
                print('error getting the audio')
                return False
            self.listPlayer.set_media_list(self.mediaList)
            return True

    def playPlaylist(self):
        self.listPlayer.play()

    def nextInPlaylist(self):
        self.listPlayer.next()

    def pausePlaylist(self):
        self.listPlayer.pause()

    def previousInPlaylist(self):
        self.listPlayer.previous()

    def stopPlaylist(self):
        self.listPlayer.stop()

    def setPlaybackMode(self, mode):
        pbm = PlaybackMode.default
        if mode == "default":
            pbm = PlaybackMode.default
        elif mode == "loop":
            pbm = PlaybackMode.loop
        elif mode == "repeat":
            pbm = PlaybackMode.repeat
        self.listPlayer.set_playback_mode(pbm)

    def playItemAtIndex(self, idx):
        self.listPlayer.play_item_at_index(idx)

# testing code
if __name__ == "__main__":
    # Player instantiation
    player = playerwrapper()
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
            print("Enter playback mode (default, loop, repeat): ")
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

