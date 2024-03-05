"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField('Playlist Name', validators=[InputRequired(), Length(min=2, max=30)])
    description = TextAreaField('Playlist Description', validators=[Length(max=150)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField('Song Title', validators=[InputRequired(), Length(min=2, max=100)])
    artist = StringField('Artist', validators=[InputRequired(), Length(min=2, max=100)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
