from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint, jsonify
from mplayer import db, bcrypt
from ytmusicapi import YTMusic
from mplayer.music.vlcpl import *

music = Blueprint('music', __name__)
ytmusic = YTMusic()
#player = playerwrapper()

@music.route('/browse/<song_ID>')
def play_song(song_ID):
    return render_template('play_song.html', song_ID = song_ID)

@music.route('/play_song_process')
def play_song_process():
    try:
        song_ID = request.args.get('song_ID', 0, type=str)
        print('Playing ' + song_ID)
        return jsonify(result='You are playing ' + song_ID)

    except Exception as e:
        return str(e)

@music.route('/pause_song_process')
def pause_song_process():
    try:
        song_ID = request.args.get('song_ID', 0, type=str)
        print('Paused ' + song_ID)
        return jsonify(result='Paused ' + song_ID)

    except Exception as e:
        return str(e)
        
@music.route('/stop_song_process')
def stop_song_process():
    try:
        song_ID = request.args.get('song_ID', 0, type=str)
        print('Stopped ' + song_ID)
        return jsonify(result='Stopped ' + song_ID)

    except Exception as e:
        return str(e)








@music.route('/browse', methods=['POST', 'GET'])
def browse():
    return render_template('browse.html')

@music.route('/background_process')
def background_process():
    try:
        song_name = request.args.get('song_name', 0, type=str)
        song_results = ytmusic.search(query = song_name, filter = "songs")
        song_ID = song_results[0]['videoId']
        return jsonify(result='You added ' + song_ID)

    except Exception as e:
        return str(e)

'''@music.route('/playlist_play')
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
'''
