from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('serie',views.SeriesView.as_view(),name='series'),
    path('serie/<int:serie_id>',views.SerieDetailView.as_view()),
    path('categoria',views.CategoriaView.as_view(),name='serializer.categoria'),
    path('producto',views.ProductoView.as_view(),name='serializer.producto'),
    path('categoria/<int:categoria_id>',views.CategoriaDetalleView.as_view()),
    path('producto/<int:producto_id>',views.ProductoDetalleView.as_view()),
]
