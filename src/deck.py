# deck.py: Model of the infection deck

import random

class Deck:

  def __init__(self):
    self.deck = []
    self.discard = []

    lines = [line.strip() for line in open('../resources/cardlist.txt')]

    lines.remove('RED')
    lines.remove('YELLOW')
    lines.remove('BLUE')
    lines.remove('BLACK')
    lines.remove('')
    lines.remove('')
    lines.remove('')

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
  def _discardlen(self):
    return len(self.discard)


  def __getitem__(self, index):
    return self.deck[index]


  def get_discard(self):
    return self.discard


  def shuffle(self):
    shuffledDeck = _shuffle(self.deck)
    
    for card in shuffledDeck:
      self.deck.append(card)


  def draw(self):
    card = self.deck.pop()
    self.discard.append(card)
    return card


  def bottomDraw(self):
    card = self.deck[0]
    self.deck.remove(card)
    self.discard.append(card)
    return card


  def peek(self, number):
    index = len(self.deck) - 1
    cards = []

    for x in range(number):
      cards.append(self.deck[index-x])

    return cards


  def forecast_pop(self):
    cards = []

    for x in range(6):
      cards.append(self.deck.pop())

    return cards


  def forecast_append(self, cards):
    cards.reverse()
    for card in cards:
      self.deck.append(card)


  def epidemic(self):
    epidemicCard = self.bottomDraw()
    self.discard = _shuffle(self.discard)

    for row in self.discard:
      self.deck.append(row)

    del self.discard[:]  

    return epidemicCard


def _shuffle(_list):
  shuffledDeck = []
  size = len(_list)

  while size > 0:
    i = random.randint(0,size-1)
    shuffledDeck.append(_list[i])
    _list.remove(_list[i])
    size = len(_list)

  return shuffledDeck
