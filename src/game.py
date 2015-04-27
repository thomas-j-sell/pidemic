# game.py: Handles game logic stuff

from deck import Deck

num_epidemics = 0
deck = Deck()
travel_ban = False


def infection_rate():
  global num_epidemics

  if travel_ban:
    infection_rate = 1
  else:
    if num_epidemics < 3:
      infection_rate = 2
    elif num_epidemics < 5:
      infection_rate = 3
    else:
      infection_rate = 4

  return infection_rate


def infection_rate_will_change():
  global num_epidemics
  will_change = False

  if num_epidemics == 2 or num_epidemics == 4:
    will_change = True

  return will_change


def toggle_travel_ban():
  global travel_ban
  travel_ban = False if travel_ban else True


def new_game():
  global num_epidemics
  num_epidemics = 0
  # deck = Deck()
  deck.shuffle_discard_onto_deck() # returns discard pile to deck
  deck.shuffle()

  setup_cards = []
  for i in range(9):
    setup_cards.append(deck.draw())

  return setup_cards


# returns bottom card of infection deck
def epidemic_draw():
  global num_epidemics
  num_epidemics += 1
  card = deck.bottom_draw()

  return card


def epidemic_shuffle():
  deck.shuffle_discard_onto_deck()


# returns array of infection cards
def infect():

  rate = infection_rate()
  infection_cards = []

  for i in range(rate):
    infection_cards.append(deck.draw())

  return infection_cards


# returns the discard pile
def discard_pile():
  return deck.get_discard()


# returns the top [number] cards without discarding them
def peek(number):
  return deck.peek(number)


def troubleshoot():
  return peek(infection_rate())


def forecast_pop():
  return deck.forecast_pop()


def forecast_append(cards):
  deck.forecast_append(cards)


def remove_card(card):
  deck.remove_card(card)
