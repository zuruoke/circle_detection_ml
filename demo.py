{% extends "base.html" %} {% block content %}
<h1>Add Playlist</h1>
{% if get_flashed_messages() %} {% for message in
get_flashed_messages(category_filter=["error"]) %}
<div class="alert alert-danger">{{ message }}</div>
{% endfor %} {% endif %}
<form method="POST" action="{{ url_for('add_playlist') }}">
  {{ form.hidden_tag() }}
  <div class="form-group">
    {{ form.name.label(class="form-control-label") }} {{
    form.name(class="form-control") }} {% if form.name.errors %}
    <div class="alert alert-danger" role="alert">{{ form.name.errors[0] }}</div>
    {% endif %}
  </div>
  <div class="form-group">
    {{ form.description.label(class="form-control-label") }} {{
    form.description(class="form-control") }} {% if form.description.errors %}
    <div class="alert alert-danger" role="alert">
      {{ form.description.errors[0] }}
    </div>
    {% endif %}
  </div>
  <button type="submit" class="btn btn-primary">Create</button>
</form>
{% endblock %}
