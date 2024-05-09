from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Serie,Categoria,Producto
from .serializer import SerieSerializer,ProductoSerializer, CategoriaSerializer


class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class SeriesView(APIView):
    
    def get(self,request):
        dataSeries = Serie.objects.all()
        serSeries = SerieSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = SerieSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class SerieDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)

class CategoriaView(APIView):
    
    def get(self,request):
        dataCategorias = Categoria.objects.all()
        serCategorias = CategoriaSerializer(dataCategorias,many=True)
        return Response(serCategorias.data)
    
    def post(self,request):
        serCategoria = CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        
        return Response(serCategoria.data)
    
class ProductoView(APIView):
    
    def get(self,request):
        dataProductos = Producto.objects.all()
        serProductos = ProductoSerializer(dataProductos,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
    
class CategoriaDetalleView(APIView):
    
    def get(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        return Response(serCategoria.data)
    
    def put(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria,data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)
    
    def delete(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        dataCategoria.delete()
        return Response(serCategoria.data)
    
class ProductoDetalleView(APIView):
    
    def get(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)