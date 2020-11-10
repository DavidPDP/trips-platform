from django.apps import AppConfig

class TripsConfig(AppConfig):
  name = 'trips_be.apps.trips'
  label = 'trips'
  verbose_name = 'Trips'

default_app_config = 'trips_be.apps.trips.TripsConfig'