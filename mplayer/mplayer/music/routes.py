from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint, jsonify
from mplayer import db, bcrypt
from ytmusicapi import YTMusic
from mplayer.music.vlcpl import *

music = Blueprint('music', __name__)
ytmusic = YTMusic()
player = playerwrapper()

@music.route('/browse', methods=['POST', 'GET'])
def browse():
    return render_template('browse.html')

'''@music.route('/browse/<pl_ID>')
def browse_pl_ID(pl_ID):
    pass'''

@music.route('/background_process')
def background_process():
    try:
        song_name = request.args.get('song_name', 0, type=str)
        song_results = ytmusic.search(query = song_name, filter = "songs")
        song_ID = song_results[0]['videoId']
        return jsonify(result='You added ' + song_ID)

    except Exception as e:
    	return str(e)

@music.route('/playlist_play')
def playlist_play():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        playlist_url = 'playlist://' + playlist_name
        player.setPlaylist(playlist_url)
        player.playPlaylist()
        return jsonify(result='Playing ' + playlist_name)

    except Exception as e:
    	return str(e)


@music.route('/playlist_pause')
def playlist_pause():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.pausePlaylist()
        return jsonify(result='Pausing ' + playlist_name)

    except Exception as e:
    	return str(e)

@music.route('/playlist_next')
def playlist_next():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.NextInPlaylist()
        return jsonify(result='Playing next song in ' + playlist_name)

    except Exception as e:
    	return str(e)

@music.route('/playlist_previous')
def playlist_previous():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.previousInPlaylist()
        return jsonify(result='Playing previous song in ' + playlist_name)

    except Exception as e:
    	return str(e)

@music.route('/playlist_stop')
def playlist_stop():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.stopPlaylist()
        return jsonify(result='Stopping ' + playlist_name)

    except Exception as e:
    	return str(e)

