{% extends "base.html" %} {% block content %}
<h2>Add Song to "{{ playlist.name }}"</h2>
<form method="POST">
  {{ form.hidden_tag() }}
  <div class="form-group">
    {{ form.song.label(class="form-control-label") }} {{
    form.song(class="form-control") }} {% if form.song.errors %} {% for error in
    form.song.errors %}
    <div class="alert alert-danger" role="alert">{{ error }}</div>
    {% endfor %} {% endif %}
  </div>
  <button type="submit" class="btn btn-primary">Add Song</button>
</form>
{% endblock %}
