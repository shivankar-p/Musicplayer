from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import current_user
from ytmusicapi import YTMusic

music = Blueprint('music', __name__)
ytmusic = YTMusic()

@music.route('/playlist')
def playlist():
    return render_template('playlist.html')

@music.route('/choice1', methods=['POST', 'GET'])
def choice1():
    try:
        song_pl = request.args.get('song_name', 0, type=str)
        lst = song_pl.split("_")
        sng = lst[0]
        pl = lst[1]#we actually have to add song id

        song_results = ytmusic.search(query = sng, filter = "songs")
        song_ID = song_results[0]['videoId']
        songinfo = sng_in_pl(username = current_user.username, playlist = pl, song = song_ID)
        db.session.add(songinfo)
        db.session.commit()
        return jsonify(result='You added ' + sng + 'in' + pl)

    except Exception as e:
    	return str(e)

@music.route('/choice2', methods=['POST', 'GET'])
def choice2():
    try:
        song_pl = request.args.get('song_name', 0, type=str)
        lst = song_pl.split("_")
        sng = lst[0]
        pl = lst[1]#we actually have to add song id

        song_results = ytmusic.search(query = sng, filter = "songs")
        song_ID = song_results[0]['videoId']
        songinfo = sng_in_pl(username = current_user.username, playlist = pl, song = song_ID)
        db.session.delete(songinfo)
        db.session.commit()
        return jsonify(result='You added ' + sng + 'in' + pl)

    except Exception as e:
    	return str(e)

@music.route('/choice3')
def choice3():
    try:
        db.sng_in_pl.filter_by(username=current_user.username)
        return jsonify(result='You added ' + sng + 'in' + pl)

    except Exception as e:
    	return str(e)

@music.route('/choice4', methods=['POST', 'GET'])
def choice4():
    try:
        pl = request.args.get('song_name', 0, type=str)
        fil = db.sng_in_pl.filter_by(username=current_user.username)
        fil2 = fil.filter_by(playlist= pl)
        ls = []
        for i in fil2:
            ls.append(i.username)
        return jsonify(result= ls)

    except Exception as e:
    	return str(e)