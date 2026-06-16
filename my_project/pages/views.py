from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):

    items = Article.objects.all()

    context = {
        'title': 'Главная страница',
        'welcome_text': 'Добро пожаловать на наш сайт!',
        'items': items,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(
        request,
        'pages/about.html'
    )

def article_detail(request, pk):

    article = get_object_or_404(
        Article,
        pk=pk
    )

    context = {
        'article': article
    }

    return render(
        request,
        'pages/detail.html',
        context
    )