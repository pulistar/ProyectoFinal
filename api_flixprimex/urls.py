from django.urls import path
from .views import peliculas_api_view, series_api_view


urlpatterns = [
    path('crear-pelicua', peliculas_api_view.as_view()),
    path('actualizar-pelicula/<int:pkid>', peliculas_api_view.as_view(), name='actualizar'),
    path('eliminar-pelicula/<int:pkid>', peliculas_api_view.as_view(), name='eliminar'),
    path('crear-serie', series_api_view.as_view()),
    path('actualizar-serie/<int:pkid>', series_api_view.as_view(), name='actualizar'),
    path('eliminar-serie/<int:pkid>', series_api_view.as_view(), name='eliminar'),
]
