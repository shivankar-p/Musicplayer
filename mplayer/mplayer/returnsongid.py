from mplayer import db, login_manager
from flask import current_app
from ytmusicapi import YTMusic
ytmusic = YTMusic()

def ret_songIDs(pl):
    ls = []
    if pl == 'testdummy':
        ls = ['kJQP7kiw5Fk', '60ItHLz5WEA', 'kffacxfA7G4']
    else:
        songlist = db.sng_in_pl.filter_by(username=current_user.username)
        for song in songlist:
            if (songlist.playlist == pl):
                ls.append(songlist.name)
    return ls
