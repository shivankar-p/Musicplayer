from mplayer import db, login_manager
from mplayer.models import sng_in_pl
from flask import current_app
from flask_login import current_user
from ytmusicapi import YTMusic
ytmusic = YTMusic()

def ret_songIDs(pl):
    ls = []
    if pl == 'testdummy':
        ls = ['kJQP7kiw5Fk', '60ItHLz5WEA', 'kffacxfA7G4']
    else:
        songlist = db.session.query(sng_in_pl).filter_by(username=current_user.username).all()
        for songpl in songlist:
            if (songpl.playlist == pl):
                ls.append(songpl.song)
    return ls

