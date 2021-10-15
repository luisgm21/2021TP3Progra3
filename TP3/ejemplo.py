# {{request.resolver_match.view_name}} con este vemos el nombre de la vista

# {% with request.resolver_match.view_name as view_name %}
#     ...
#     {{ view_name }} Asignamos un valor a un entorno
#     ...
# {% endwith %}

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) configuracion de los directorios