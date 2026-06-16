from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import FeedbackForm, ArticleForm
from django.contrib.auth.forms import UserCreationForm

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

def contact(request):

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            return redirect('home')

    else:

        form = FeedbackForm()

    context = {
        'form': form
    }

    return render(
        request,
        'pages/contact.html',
        context
    )

def article_create(request):

    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():

            article = form.save(
              commit=False
            )

            article.author = request.user

            article.save()

            return redirect(
                'article_detail',
                pk=article.pk
            )

    else:

        form = ArticleForm()

    context = {
        'form': form,
        'title': 'Создание статьи'
    }

    return render(
        request,
        'pages/form.html',
        context
    )

def article_update(request, pk):

    article = get_object_or_404(
        Article,
        pk=pk
    )

    if request.method == 'POST':

        form = ArticleForm(
            request.POST,
            instance=article
        )

        if form.is_valid():

            form.save()

            return redirect(
                'article_detail',
                pk=article.pk
            )

    else:

        form = ArticleForm(
            instance=article
        )

    context = {
        'form': form,
        'title': 'Редактирование статьи'
    }

    return render(
        request,
        'pages/form.html',
        context
    )

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(
        request,
        'pages/register.html',
        {'form': form}
    )