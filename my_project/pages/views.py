from django.shortcuts import render


def index(request):

    context = {
        'title': 'Главная страница',
        'welcome_text': 'Добро пожаловать на наш сайт!'
    }

    return render(
        request,
        'pages/index.html',
        context
    )


def about(request):
    return render(
        request,
        'pages/about.html'
    )