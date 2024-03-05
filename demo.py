from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
import os

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm
from flask import flash
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
# Please do not modify the following line on submission
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///playlist-app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    playlist = Playlist.query.get_or_404(playlist_id)
    
    return render_template("show_playlist.html", playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()
    if form.validate_on_submit():
        try:
            new_playlist = Playlist(name=form.name.data, description=form.description.data)
            db.session.add(new_playlist)
            db.session.commit()
            return redirect('/playlists')
        except IntegrityError:
            db.session.rollback()
            flash('A playlist with that name already exists. Please use a different name.', 'error')
    return render_template('add_playlist.html', form=form)
   
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    song = Song.query.get_or_404(song_id)
    return render_template("show_song.html", song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    
    form = SongForm()
    if form.validate_on_submit():
        new_song = Song(title=form.title.data, artist=form.artist.data)
        db.session.add(new_song)
        db.session.commit()
        return redirect('/songs')
    return render_template('add_song.html', form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    
    # Fetch songs not currently in the playlist
    existing_song_ids = [ps.id for ps in playlist.songs]
    available_songs = Song.query.filter(Song.id.notin_(existing_song_ids)).all()
    
    form = NewSongForPlaylistForm()
   
    # Restrict form to songs not already on this playlist

    curr_on_playlist = ...
    form.song.choices = [(song.id, song.title) for song in available_songs]

    if form.validate_on_submit():

        # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        
        song_id = form.song.data
        new_playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=song_id)
        db.session.add(new_playlist_song)
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                           playlist=playlist,
                           form=form)
