from django.shortcuts import render, HttpResponse, redirect
from .forms import ArticleForm
from .models import Article


def index(request):
    return render(request, "main/index.html")


def create_article(request):
    if request.method == 'POST':
        article = ArticleForm(request.POST)
        if article.is_valid():
            article.save()
            return redirect('home')
        else:
            return HttpResponse(400)

    article = ArticleForm()
    context = {
        "form": article
    }

    return render(request, 'main/create-article.html', context=context)


def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'main/articles.html', {'articles': articles})


def get_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'main/article.html', {'article': article})


def delete_article(request, id):
    article = Article.objects.get(id=id)

    try:
        article.delete()
        return render(request, "main/index.html")
    except:
        return HttpResponse(400)


def update_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article.title = request.POST['title']
        article.intro = request.POST['intro']
        article.text = request.POST['text']
        try:
            article.save()
            return render(request, 'main/article.html', {'article': article})
        except:
            return HttpResponse(400)
    else:
        return render(request, 'main/update-article.html', {'article': article})
