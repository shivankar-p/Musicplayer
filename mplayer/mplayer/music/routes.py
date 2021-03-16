from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint, jsonify
from mplayer import db, bcrypt
from ytmusicapi import YTMusic

music = Blueprint('music', __name__)
ytmusic = YTMusic()


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


