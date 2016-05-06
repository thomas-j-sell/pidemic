# deck.py: supplies a model of the infection deck from board game Pandemic
# for information about the rules of Pandemic and the mechanics of the infection deck
#  consult the game's rulebook.

import random

class Deck:

  # initializes the deck from a file containing a list of cards
  def __init__(self):
    self.deck = []
    self.discard = []

    lines = [line.strip() for line in open('resources/cardlist.txt')]

    # remove parts of the file that aren't card names
    lines.remove('RED')
    lines.remove('YELLOW')
    lines.remove('BLUE')
    lines.remove('BLACK')
    lines.remove('')
    lines.remove('')
    lines.remove('')

    # each city is assigned a corresponding color
    for row in lines:
      x = lines.index(row)
      if x < 12:
        self.deck.append([row,'red'])
      elif x >= 12 and x < 24:
        self.deck.append([row,'yellow'])
      elif x >= 24 and x < 36:
        self.deck.append([row,'blue'])
      elif x >= 36 and x < 48:
        self.deck.append([row,'black'])


  def __len__(self):
    return len(self.deck)


  # used just for testing
  def _discard_len(self):
    return len(self.discard)


  def __getitem__(self, index):
    return self.deck[index]


  def get_discard(self):
    return self.discard


  def shuffle(self):
    random.shuffle(self.deck)


  def draw(self):
    card = self.deck.pop()
    self.discard.append(card)
    return card


  def bottom_draw(self):
    card = self.deck[0]
    self.deck.remove(card)
    self.discard.append(card)
    return card


  # reveals the top x cards without altering their order
  def peek(self, number):
    index = len(self.deck) - 1
    cards = []

    for x in range(number):
      cards.append(self.deck[index-x])

    return cards


  # removes top 6 cards so they can be rearranged
  # should always be used with forecast_pop
  def forecast_pop(self):
    cards = []

    for x in range(6):
      cards.append(self.deck.pop())

    return cards


  # returns cards back onto the deck
  # should always be used with forecast_pop
  def forecast_append(self, cards):
    cards.reverse()
    for card in cards:
      self.deck.append(card)


  def remove_card(self, card):
    self.discard.remove(card)


  def shuffle_discard_onto_deck(self):
    random.shuffle(self.discard)

    for row in self.discard:
      self.deck.append(row)

    del self.discard[:]  

