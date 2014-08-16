from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from cards.forms import EmailUserCreationForm
from cards.models import *
from playingcards import settings
from django.db.models import Count


def home(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'cards.html', data)

def clubs(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'clubs.html', data)

def diamonds(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'diamonds.html', data)

def face(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'face.html', data)

def card_filters(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'card_filters.html', data)

def templatetags(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'templatetags.html', data)

def templatefilters(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'templatefilters.html', data)

def random_cards(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'random_cards.html', data)

def newpage(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'newpage.html', data)


def profile(request):
    return render(request, 'profile.html')

def faq(request):
    return render(request, 'faq.html')


def newrpage(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'newrpage.html', data)


def blackjack(request):
    data = {
        'cards': Card.objects.order_by('?')[:2]
    }
    if data['cards'][0].rank == 'ace' or data['cards'][1].rank == 'ace':
            user = request.user
            if data['cards'][0].rank == 'ace':
                user.email_user('Whoaa!!', 'Nice ace {}'.format(data['cards'][0].get_suit_display()), settings.DEFAULT_FROM_EMAIL)
            elif data['cards'][1].rank == 'ace':
                user.email_user('Whoaa!!', 'Nice ace {}'.format(data['cards'][1].get_suit_display()), settings.DEFAULT_FROM_EMAIL)
    return render(request, 'blackjack.html', data)

@login_required
def poker(request):
    data = {'cards': Card.objects.order_by('?')[:5]}

    return render(request, 'poker.html', data)

@login_required
def heartpage(request):
    data = {
        'cards': Card.objects.filter(suit=3)
    }

    return render(request, 'heartpage.html', data)

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site</div><br><div>you joined at {}</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def war(request):
    cards = list(Card.objects.order_by('?'))
    user_card = cards[0]
    dealer_card = cards[1]

    result = user_card.get_war_result(dealer_card)
    WarGame.objects.create(result=result, player=request.user)

    war_game = WarGame.objects.filter(player=request.user)
    if war_game.count() == 10:
        user = request.user
        user.email_user('wow', 'thanks for playing 10 games')


    # if i == 10:
    #     user = request.user
    #     user.email_user('Thanks', 'Thanks for playing our game')
    return render(request, 'war.html', {
        'h': h,
        'user_cards': user_card,
        'dealer_cards': dealer_card,
        'result': result
    })

