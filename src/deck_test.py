import unittest
from deck import Deck

class deckTest(unittest.TestCase):
  
  def test_init(self):
    testDeck = Deck()
    self.assertNotEqual(testDeck, None, "deck wasn't initialized")


  def test_size(self):
    testDeck = Deck()
    self.assertEqual(len(testDeck), 48, 'incorrect deck size')


  def test_contents(self):
    testDeck = Deck()
    self.assertEqual(testDeck[0], ['BANGKOK', 'red'], 'incorrect deck contents')
    self.assertEqual(testDeck[13], ['BUENOS AIRES', 'yellow'], 'incorrect deck contents')
    self.assertEqual(testDeck[24], ['ATLANTA', 'blue'], 'incorrect deck contents')
    self.assertEqual(testDeck[47], ['TEHRAN', 'black'], 'incorrect deck contents')


  def test_shuffle(self):
    testDeck = Deck()
    testDeck.shuffle()
    testDeck.shuffle()
    testDeck.shuffle()
    self.assertNotEqual(testDeck, None, "shuffle deleted deck")
    self.assertEqual(len(testDeck), 48, 'shuffle changed deck size')
    self.assertNotEqual(testDeck[0], ['BANGKOK', 'red'], 'card was in same slot after shuffle')
    self.assertNotEqual(testDeck[12], ['BOGOTA', 'yellow'], 'card was in same slot after shuffle')
    self.assertNotEqual(testDeck[24], ['ATLANTA', 'blue'], 'card was in same slot after shuffle')
    self.assertNotEqual(testDeck[47], ['TEHRAN', 'black'], 'card was in same slot after shuffle')


  def test_draw(self):
    testDeck = Deck()

    card = testDeck.draw()
    self.assertEqual(card, ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 1, 'discard pile incorrect size')

    testDeck.shuffle()
    testDeck.draw()
    testDeck.draw()
    testDeck.draw()
    self.assertEqual(testDeck._discard_len(), 4, 'discard pile incorrect size')


  def test_bottom_draw(self):
    testDeck = Deck()

    card = testDeck.bottom_draw()
    self.assertEqual(card, ['BANGKOK', 'red'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discard_len(), 1, 'discard pile incorrect size')

    card = testDeck.bottom_draw()
    self.assertEqual(card, ['BEIJING', 'red'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discard_len(), 2, 'discard pile incorrect size')

    card = testDeck.bottom_draw()
    self.assertEqual(card, ['HO CHI MIN CITY', 'red'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discard_len(), 3, 'discard pile incorrect size')


  def test_peek(self):
    testDeck = Deck()

    cards = testDeck.peek(1)
    self.assertEqual(cards[0], ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 0, 'discard pile incorrect size')

    cards = testDeck.peek(2)
    self.assertEqual(cards[0], ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(cards[1], ['RIYADH', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 0, 'discard pile incorrect size')

    cards = testDeck.peek(4)
    self.assertEqual(cards[0], ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(cards[1], ['RIYADH', 'black'], 'did not draw top card')
    self.assertEqual(cards[2], ['MUMBAI', 'black'], 'did not draw top card')
    self.assertEqual(cards[3], ['MOSCOW', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 0, 'discard pile incorrect size')


  def test_forecast(self):
    testDeck = Deck()

    cards = testDeck.forecast_pop()
    self.assertEqual(len(testDeck), 42, 'incorrect deck size')
    self.assertEqual(cards[0], ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(cards[1], ['RIYADH', 'black'], 'did not draw top card')
    self.assertEqual(cards[2], ['MUMBAI', 'black'], 'did not draw top card')
    self.assertEqual(cards[3], ['MOSCOW', 'black'], 'did not draw top card')
    self.assertEqual(cards[4], ['KOLKATA', 'black'], 'did not draw top card')
    self.assertEqual(cards[5], ['KARACHI', 'black'], 'did not draw top card')

    cards.reverse()
    self.assertEqual(cards[5], ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(cards[4], ['RIYADH', 'black'], 'did not draw top card')
    self.assertEqual(cards[3], ['MUMBAI', 'black'], 'did not draw top card')
    self.assertEqual(cards[2], ['MOSCOW', 'black'], 'did not draw top card')
    self.assertEqual(cards[1], ['KOLKATA', 'black'], 'did not draw top card')
    self.assertEqual(cards[0], ['KARACHI', 'black'], 'did not draw top card')

    self.assertEqual(len(testDeck), 42, 'incorrect deck size')
    testDeck.forecast_append(cards)
    self.assertEqual(len(testDeck), 48, 'incorrect deck size')

    cards = []
    for x in range(6):
      cards.append(testDeck.draw())

    self.assertEqual(cards[5], ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(cards[4], ['RIYADH', 'black'], 'did not draw top card')
    self.assertEqual(cards[3], ['MUMBAI', 'black'], 'did not draw top card')
    self.assertEqual(cards[2], ['MOSCOW', 'black'], 'did not draw top card')
    self.assertEqual(cards[1], ['KOLKATA', 'black'], 'did not draw top card')
    self.assertEqual(cards[0], ['KARACHI', 'black'], 'did not draw top card')


  def test_remove_card(self):
    testDeck = Deck()

    card = testDeck.draw()
    self.assertEqual(card, ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 1, 'discard pile incorrect size')

    testDeck.remove_card(card)
    self.assertEqual(testDeck._discard_len(), 0, 'discard pile incorrect size')

  def test_epidemic(self):
    testDeck = Deck()

    card = testDeck.draw()
    self.assertEqual(card, ['TEHRAN', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 1, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 47, 'deck incorrect size')
    card = testDeck.draw()
    self.assertEqual(card, ['RIYADH', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 2, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 46, 'deck incorrect size')
    card = testDeck.draw()
    self.assertEqual(card, ['MUMBAI', 'black'], 'did not draw top card')
    self.assertEqual(testDeck._discard_len(), 3, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 45, 'deck incorrect size')

    card = testDeck.bottom_draw()
    self.assertEqual(card, ['BANGKOK', 'red'], 'bottom draw returned incorrect card')
    testDeck.shuffle_discard_onto_deck()
    self.assertEqual(testDeck._discard_len(), 0, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 48, 'deck incorrect size')


if __name__ == '__main__':
  unittest.main()
  