from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from demo.models import Book


class Second(View):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.output = f'We have {len(books)} books in our Database.'

	def get(self, request):
		return HttpResponse(self.output)

books = Book.objects.all()
