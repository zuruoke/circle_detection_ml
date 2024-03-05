{% extends "base.html" %} {% block content %}
<h1>{{ playlist.name }}</h1>
<p>{{ playlist.description }}</p>

<h2>Songs</h2>
<ul>
  {% for song in playlist.songs %}
  <li>{{ song.title }} by {{ song.artist }}</li>
  {% else %}
  <li>No songs in this playlist yet.</li>
  {% endfor %}
</ul>

<a href="/playlists/{{ playlist.id }}/add-song" class="btn btn-primary"
  >Add Song to Playlist</a
>
<br />
<a href="/playlists" class="btn btn-secondary">Back to All Playlists</a>
{% endblock %}
