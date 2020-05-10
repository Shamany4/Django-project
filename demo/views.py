from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from demo.models import Book
from demo.serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication

class Second(View):
	def __init__(self, **kwargs):
		books = Book.objects.all()
		super().__init__(**kwargs)
		self.output = ''
		for book in books:
			self.output += (f'We have {book.title} with ID {book.id} in our Database <br>')

	def get(self, request):
		return HttpResponse(self.output)

def first(request):
	books = Book.objects.all()
	return render(request, 'index.html', {'books': books})


class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	authentication_classes = (TokenAuthentication,)
