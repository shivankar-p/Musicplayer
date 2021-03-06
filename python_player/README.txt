
Extract the zip in a folder.
The vlcpl.py is wrapper class for integration with VLC player.
Change permission of vlcpl.py to 755.
$ chmod 755 ./vlcpl.py

The usage is demonstrated when run as program.
Run ./vlcpl.py from bash command prompt in terminal.


1. Playing all songs in a folder by providing playlist as file:///<path>/

$ ./vlcpl.py 
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

$ ./vlcpl.py 
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
[00007f9874004e50] prefetch stream error: unimplemented query (264) in control
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
[00007f98743033c0] prefetch stream error: unimplemented query (264) in control
9
$

The options are self-explainatory and input required is prompted for – wherever required.

