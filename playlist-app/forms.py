"""Forms for playlist app."""

from wtforms import SelectField, StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[DataRequired(), Length(min=1, max=50)])
    description = StringField("Playlist Description", validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField("Create Playlist")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[DataRequired(), Length(min=1, max=50)])
    artist = StringField("Artist", validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField("Add Song")


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
    submit = SubmitField("Add Song")
