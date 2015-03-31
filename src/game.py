# game.py: Handles game logic stuff

from deck import Deck

infection_rate = 2;
deck = Deck()

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

def newGame():
  # reset variables (infection rate)
  # shuffle deck || create new deck
  # board set up, draw 3 and "place 3", draw 3 and "place 2", draw 3 and "place 1"
  global infection_rate
  infection_rate = 2
  print infection_rate

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
  global infection_rate
  infection_rate += 1
  print infection_rate
  
  print "epidemic"
  card = deck.epidemic()
  print card
  return card


# returns array of cards (cities to infect)
def infect():
  print "infect"