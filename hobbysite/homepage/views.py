from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from merchstore.models import Transaction
from commissions.models import JobApplication, Commission
from wiki.models import Article as wikiArticle
from blog.models import Article as blogArticle

from user_management.models import Profile

# Create your views here.

def homepage_test(request):
    return HttpResponse("hello from homepage")


def homepage(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        profile = Profile.objects.filter(user=user).first()
    return render(
        request,
        "homepage/home.html",
        {
            "user": user,
            "profile": profile
        }
    )


@login_required
def dashboard(request):
    user_name = request.user.profile.display_name

    products_bought = Transaction.objects.filter(buyer__display_name=user_name)
    products_sold = Transaction.objects.filter(product__owner__display_name=user_name)

    commissions_created = Commission.objects.filter(owner__display_name=user_name)
    commissions_joined = JobApplication.objects.filter(status='A', applicant__display_name=user_name)

    wiki_articles = wikiArticle.objects.filter(author__display_name=user_name)
    blog_articles = blogArticle.objects.filter(author__display_name=user_name)

    user_profile = request.user.profile

    ctx = {
        "products_bought": products_bought, 
        "products_sold": products_sold, 
        "commissions_created": commissions_created, 
        "commissions_joined": commissions_joined, 
        "wiki_articles": wiki_articles,
        "blog_articles": blog_articles,
        "user_profile": user_profile
    }

    return render (
        request,
        "homepage/dashboard.html",
        ctx
    )