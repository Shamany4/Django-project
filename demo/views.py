from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from demo.models import Book


class Second(View):
	def __init__(self, **kwargs):
		books = Book.objects.all()
		super().__init__(**kwargs)
		self.output = ''
		for book in books:
			self.output += (f'We have {book.title} with ID {book.id} in our Database <br>')

	def get(self, request):
		return HttpResponse(self.output)

