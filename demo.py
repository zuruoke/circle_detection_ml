{% extends "base.html" %} {% block content %}
<div class="container mt-5">
  <h2>Add a New Song</h2>
  <form method="POST" action="">
    {{ form.hidden_tag() }}
    <div class="form-group">
      {{ form.title.label(class="form-control-label") }} {{
      form.title(class="form-control") }} {% if form.title.errors %} {% for
      error in form.title.errors %}
      <div class="alert alert-danger" role="alert">{{ error }}</div>
      {% endfor %} {% endif %}
    </div>
    <div class="form-group">
      {{ form.artist.label(class="form-control-label") }} {{
      form.artist(class="form-control") }} {% if form.artist.errors %} {% for
      error in form.artist.errors %}
      <div class="alert alert-danger" role="alert">{{ error }}</div>
      {% endfor %} {% endif %}
    </div>
    <button type="submit" class="btn btn-primary">Add Song</button>
  </form>
</div>
{% endblock %}
