from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import login_required, current_user
from mplayer import db, bcrypt
from ytmusicapi import YTMusic
from mplayer.music.vlcpl import *
from mplayer.users.forms import SearchForm
from mplayer.models import sng_in_pl

music = Blueprint('music', __name__)
ytmusic = YTMusic()
player = playerwrapper()

@music.route('/browse/<song_ID>/<title>/<duration>/<artist>/<thumbnail>', methods=['GET', 'POST'])
def play_song(song_ID, title, duration, artist, thumbnail):
    thumbnail = 'https://lh3.googleusercontent.com/'+thumbnail
    print(thumbnail)
    return render_template('play_song.html', song_ID = song_ID, title=title, duration=duration, artist=artist, thumbnail=thumbnail)

@music.route('/play_song_process')
def play_song_process():
    try:
        song_ID = request.args.get('song_ID', 0, type=str)
        print('Playing ' + song_ID)
        song_url = 'song://' + song_ID
        player.setPlaylist(song_url)
        player.playPlaylist()
        return jsonify(result='You are playing ' + song_ID)

    except Exception as e:
        return str(e)

@music.route('/pause_song_process')
def pause_song_process():
    try:
        song_ID = request.args.get('song_ID', 0, type=str)
        print('Paused ' + song_ID)
        player.pausePlaylist()
        return jsonify(result='Paused ' + song_ID)

    except Exception as e:
        return str(e)
        
@music.route('/stop_song_process')
def stop_song_process():
    try:
        song_ID = request.args.get('song_ID', 0, type=str)
        print('Stopped ' + song_ID)
        player.stopPlaylist()
        return jsonify(result='Stopped ' + song_ID)

    except Exception as e:
        return str(e)

@music.route('/browse', methods=['POST', 'GET'])
def browse():
    form = SearchForm()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    if form.validate_on_submit():
        try:
            song_name = list(str(form.song_name))
            song_name = song_name[67:]
            song_name = song_name[0:-2]
            song_name = ''.join(song_name)
            song_results = ytmusic.search(query = song_name, filter = "songs")
            song_ID = song_results[0]['videoId']
            title = song_results[0]['title']
            duration=song_results[0]['duration']
            artist = song_results[0]['artists'][0]['name']
            thumbnail=song_results[0]['thumbnails'][0]['url']
            thumbnail=list(thumbnail)
            thumbnail=thumbnail[34:]
            thumbnail=''.join(thumbnail)
            return redirect(url_for('music.play_song', song_ID= song_ID,  title=title, duration=duration, artist=artist, thumbnail=thumbnail ))
        except Exception as e:
            return str(e)

    return render_template('browse.html', form=form, image_file=image_file)

'''@music.route('/background_process')
def background_process():
    try:
        song_name = request.args.get('song_name', 0, type=str)
        song_results = ytmusic.search(query = song_name, filter = "songs")
        song_ID = song_results[0]['videoId']
        return jsonify(result='You added ' + song_ID)

    except Exception as e:
        return str(e)'''

@login_required
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
        player.nextInPlaylist()
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

@music.route('/playlist_repeat')
def playlist_repeat():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.setPlaybackMode('repeat')
        return jsonify(result='Setting playback mode to repeating current song')

    except Exception as e:
        return str(e)

@music.route('/playlist_loop')
def playlist_loop():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.setPlaybackMode('loop')
        return jsonify(result='Setting playback mode to looping current playlist')

    except Exception as e:
        return str(e)

@music.route('/playlist_default')
def playlist_default():
    try:
        playlist_name = request.args.get('playlist_name', '0', type=str)
        player.setPlaybackMode('default')
        return jsonify(result='Restoring to default sequential playback mode')

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

#playlist choices
@login_required
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
        songinfo = sng_in_pl(username=current_user.username, playlist=pl, song=song_ID)
        db.session.add(songinfo)
        db.session.commit()
        return jsonify(result='You added ' + sng + 'in' + pl)

    except SQLAlchemyError as e:
        err = str(e.__dict__['orig'])
        print(err)
        return err
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
