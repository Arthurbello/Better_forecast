from django import template
import random

register = template.Library()

@register.filter
def suit(list, suit_type):
    items = []
    for item in list:
        if item.get_suit_display() == suit_type:
            items.append(item)

    return items

@register.filter
def ranks(list, rank_type='ace'):
    items = []
    for item in list:
        if item.rank == rank_type:
            items.append(item)
        elif item.rank != 'ace':
            pass
    return items

@register.filter
def rank(list, rank_type):
    items = []
    for item in list:
        if item.rank == rank_type:
            items.append(item)


    return items

@register.filter
def shuffle(cards):
    cards = list(cards)
    random.shuffle(cards)
    return cards


@register.filter
def deal(list, amount):
    return list[:amount]

@register.filter
def r(list, rank_type):
    items = []
    for item in list:
        if item.rank == rank_type:
            items.append(item)
    return items