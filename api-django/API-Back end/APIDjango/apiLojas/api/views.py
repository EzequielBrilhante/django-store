from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .pagination import *

# Create your views here.
class LojaList(APIView):
    def get(self, request):
        try:
            lista_lojas = Estabelecimento.objects.all()
            paginator = PaginacaoLojas()
            result_page = paginator.paginate_queryset(lista_lojas, request)
            serializer = LojaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = LojaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LojaDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
             return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                status=status.HTTP_400_BAD_REQUEST)
            loja = Estabelecimento.objects.get(pk=pk)
            serializer = LojaSerializer(loja)
            return Response(serializer.data)
        except Estabelecimento.DoesNotExist:
            return JsonResponse({'mensagem': "A loja não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
             return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                status=status.HTTP_400_BAD_REQUEST)
            loja = Estabelecimento.objects.get(pk=pk)
            serializer = LojaSerializer(loja, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Estabelecimento.DoesNoExist:
            return JsonResponse({'mensagem': "A loja não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "o ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            loja = Estabelecimento.objects.get(pk=pk)
            loja.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Estabelecimento.DoesNotExist:
            return JsonResponse({'mensagem': "A loja não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu uum erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)