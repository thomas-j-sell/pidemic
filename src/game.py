# game.py: Handles game logic stuff

from deck import Deck

epidemic_rate = 0;
deck = Deck()
print "game.py: deck: ", deck

# keep track of game state
# States:
#   Normal: navigate through discard pile
#     buttons for epidemic, end game and remove card
#   Epidemic:
#     Display city and "place 3 cubes" reminder text
#     Continue button to continue state flow
#   Infect:
#     Navigate through cities with "place one cube" reminder text
#     Last card should should have a continue button

def new_game():
  # reset variables (infection rate)
  # shuffle deck || create new deck
  # board set up, draw 3 and "place 3", draw 3 and "place 2", draw 3 and "place 1"
  global epidemic_rate
  epidemic_rate = 0
  print epidemic_rate
  print "game.py: in function new_game deck: ", deck
  deck.epidemic() # returns discard pile to deck 
  deck.shuffle()
  
  setup_cards = []
  for i in range(9):
    setup_cards.append(deck.draw())
  for i in range(9):
    print setup_cards[i]
  
  print "Game: new game"
  return setup_cards

# returns bottom card of infection deck
def epidemic():
  global epidemic_rate
  epidemic_rate += 1
  print epidemic_rate

  print "epidemic"
  card = deck.epidemic()
  print card
  return card

# returns array of cards (cities to infect)
def infect():
  global epidemic_rate

  if epidemic_rate < 3:
    infection_rate = 2
  elif epidemic_rate < 5:
    infection_rate = 3
  else:
    infection_rate = 4

  infection_cards = []

  # infection rate doesn't count from 0
  for i in range(infection_rate):
    infection_cards.append(deck.draw())

  return infection_cards

def discard_pile():
  return deck.get_discard()
