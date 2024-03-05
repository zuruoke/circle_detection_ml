{% extends "base.html" %} {% block content %}
<h1>{{ song.title }}</h1>
<p>Artist: {{ song.artist }}</p>

<!-- Optional: if you want to show playlists containing this song -->
<h2>Playlists</h2>
<ul>
  {% for playlist in song.playlists %}
  <li>{{ playlist.name }}</li>
  {% else %}
  <li>This song is not in any playlists yet.</li>
  {% endfor %}
</ul>

<a href="/songs" class="btn btn-secondary">Back to All Songs</a>
{% endblock %}
