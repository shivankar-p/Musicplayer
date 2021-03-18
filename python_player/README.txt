Package requirements:
=====================
If not already done:
1. install pip3 using command "sudo apt install python3-pip"
2. install python-vlc using command "sudo pip3 install python-vlc"
3. install vlc media player using command "sudo apt-get install vlc"
4. correct youtube.luac using following steps:
   4.1 download https://github.com/videolan/vlc/blob/master/share/lua/playlist/youtube.lua to Dowloads folder
   4.2 copy the downloaded youtube.lua using command:
       cp ~/Downloads/youtube.lua /usr/lib/x86_64-linux-gnu/vlc/lua/playlist/youtube.luac
5. install pafy using command "sudo pip3 install pafy"
6. install youtube-dl using command "sudo pip3 install youtube-dl"

Usage:
======
Change permission of callingmodule.py to 755 using following commands in Musicplayer/python_player/ :
$ chmod 755 ./callingmodule.py

The usage is demonstrated when run as program.
Run ./callingmodule.py from bash command prompt in terminal.

Example executions of callingmodule.py:
=======================================
1. Playing all songs in a folder by providing playlist as file:///<path>/

$ ./callingmodule.py 
Enter option:
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
1
Enter playlist url: 
file:///home/songs
Setting playlist: file:///home/songs
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
2
Playing playlist: file:///home/songs
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
9
$


2. Playing all songs in a .m3u or .pls playlist file by providing playlist as file:///<path>/<filename>.m3u or https://<server-path>/<filename>.m3u or
file:///<path>/<filename>.pls or https://<server-path>/<filename>.pls

$ ./callingmodule.py
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
1
Enter playlist url: 
file:///home/playlist/index.m3u
Setting playlist: file:///home/playlist/index.m3u
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
2
Playing playlist: file:///home/playlist/index.m3u
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
5
Playing next in playlist: file:///home/playlist/index.m3u
Enter option:
 1: Set playlist
 2: Play playlist
 3: Pause playlist
 4: Stop playlist
 5. Next in playlist
 6. Previous in playlist
 7. Set playback mode
 8. Play item at index
 9. Exit
9
$

The options are self-explainatory and input required is prompted for – wherever required.

