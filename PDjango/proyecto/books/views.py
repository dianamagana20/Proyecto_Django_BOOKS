#from django.shortcuts import render

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author

# Create your views here.
class RetrieveBooks(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        books_list = Book.objects.all().values()
        return Response(books_list, status=status.HTTP_200_OK)


class RetrieveAuthor(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        author_list = Author.objects.all().values()
        return Response(author_list, status=status.HTTP_200_OK)


class CreateAuthor(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        author_objeto= Author.objects.create(
            first_name = request.data.get('firts_name',''),
            last_name = request.data.get('last_name',''),
            birth_date = request.data.get('birth_date','')       
        )
        return Response({'message':'Creado'}, status=status.HTTP_201_CREATED)


class CreateBook(APIView):
    permissions_classes = (AllowAny,)

    def post(self, request):
        book_objeto = Book.objects.create(
            name = request.data.get('name',''),
            isbn = request.data.get('isbn',0),
            publisher_date = request.data.get('publisher_date','17-03-22'),
            author_id = request.data.get('author_id',1)
        ) 
        return Response({'message':'Creado'}, status=status.HTTP_201_CREATED)