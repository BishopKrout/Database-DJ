"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    songs = db.relationship("Song", secondary="playlist_songs", back_populates="playlists")

class Song(db.Model):
    """Song."""
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)

    playlists = db.relationship("Playlist", secondary="playlist_songs", back_populates="songs")

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (
        db.ForeignKeyConstraint([playlist_id], [Playlist.id]),
        db.ForeignKeyConstraint([song_id], [Song.id]),
    )

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
