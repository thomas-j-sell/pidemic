# game.py: Handles game logic stuff

from deck import Deck

epidemic_rate = 0;
deck = Deck()


def infection_rate():
  global epidemic_rate

  if epidemic_rate < 3:
    infection_rate = 2
  elif epidemic_rate < 5:
    infection_rate = 3
  else:
    infection_rate = 4

  return infection_rate


def new_game():
  global epidemic_rate
  epidemic_rate = 0
  deck.epidemic() # returns discard pile to deck 
  deck.shuffle()

  setup_cards = []
  for i in range(9):
    setup_cards.append(deck.draw())

  return setup_cards


# returns bottom card of infection deck
def epidemic():
  global epidemic_rate
  epidemic_rate += 1
  card = deck.epidemic()

  return card


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
  rate = infection_rate()
  return peek(rate)



