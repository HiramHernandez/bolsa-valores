from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from .services import EmpresaService
from .serializers import *
from .utils import validate_post_empresa, simbol_is_accepted

class CheckAuth(APIView):
    def get(self, request):
        authentication_classes = [SessionAuthentication]
        #example = [{'id': 24}, {'id': 25}]
        return Response({'detail': 'You\'re Authenticated'})


class EmpresaListController(APIView):
    authentication_classes = [SessionAuthentication]
    def __init__(self):
        self.empresa_service = EmpresaService()

    def get(self, request):
        companies = self.empresa_service.get_empresas()
        data = []
        page = request.GET.get('page', 1)
        paginator = Paginator(companies, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        serializer = SerializerEmpresa(data, context={'request': request}, many=True)
        next_page = data.next_page_number if data.has_next() else 1
        previous_page = data.previous_page_number() if data.has_previous() else 1

        return Response(
            {
                'data': serializer.data ,
                'count': paginator.count,
                'numpages' : paginator.num_pages,
                'nextlink': '/api/empresas/?page=' + str(next_page),
                'prevlink': '/api/empresas/?page=' + str(previous_page)
            }
        )

    def post(self, request):
        
        #00d708a6-0038-4d8b-94c3-d1c97aac6597
        fields_empty = validate_post_empresa(request.data)
        if len(fields_empty) > 0:
            return Response({'message': fields_empty}, status=status.HTTP_400_BAD_REQUEST)
        if not simbol_is_accepted(request.data['simbolo']):
            return Response(
                {
                    'message': 'Los simbolos de la Bolsa de NY no pueden tener mas de 4 letras o contener caracteres de otro tipo'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = SerializerEmpresa(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def empresa_detail(request, pk):
    empresa = Empresa.objects.get(pk=pk)
    if not empresa:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializerEmpresa(empresa, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SerializerEmpresa(empresa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request == 'DELETE':
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
