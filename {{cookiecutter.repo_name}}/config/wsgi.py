import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
{% if cookiecutter.new_relic_key != "" %}
if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.production":
    import newrelic.agent
    newrelic.agent.initialize('/app/newrelic.ini')
    application = get_wsgi_application()
    application = newrelic.agent.wsgi_application()(application)
else:
    application = get_wsgi_application()
{% else %}
application = get_wsgi_application()
{% endif %}