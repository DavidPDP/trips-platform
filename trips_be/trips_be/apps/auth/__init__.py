from django.apps import AppConfig

class AuthConfig(AppConfig):
  name = 'trips_be.apps.auth'
  label = 'authentication' # not to be confused with Django's auth module.
  verbose_name = 'Authentication'

default_app_config = 'trips_be.apps.auth.AuthConfig'