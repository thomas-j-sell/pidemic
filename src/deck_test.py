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
    self.assertEqual(testDeck[0], ['BANGKOK', 'RED'], 'incorrect deck contents')
    self.assertEqual(testDeck[12], ['BOGOTA', 'YELLOW'], 'incorrect deck contents')
    self.assertEqual(testDeck[24], ['ATLANTA', 'BLUE'], 'incorrect deck contents')
    self.assertEqual(testDeck[47], ['TEHRAN', 'BLACK'], 'incorrect deck contents')


  def test_shuffle(self):
    testDeck = Deck()
    testDeck.shuffle()
    testDeck.shuffle()
    testDeck.shuffle()
    self.assertNotEqual(testDeck, None, "shuffle deleted deck")
    self.assertEqual(len(testDeck), 48, 'shuffle changed deck size')
    self.assertNotEqual(testDeck[0], ['BANGKOK', 'RED'], 'card was in same slot after shuffle')
    self.assertNotEqual(testDeck[12], ['BOGOTA', 'YELLOW'], 'card was in same slot after shuffle')
    self.assertNotEqual(testDeck[24], ['ATLANTA', 'BLUE'], 'card was in same slot after shuffle')
    self.assertNotEqual(testDeck[47], ['TEHRAN', 'BLACK'], 'card was in same slot after shuffle')


  def test_draw(self):
    testDeck = Deck()

    card = testDeck.draw()
    self.assertEqual(card, ['TEHRAN', 'BLACK'], 'did not draw top card')
    self.assertEqual(testDeck._discardlen(), 1, 'discard pile incorrect size')

    testDeck.shuffle()
    testDeck.draw()
    testDeck.draw()
    testDeck.draw()
    self.assertEqual(testDeck._discardlen(), 4, 'discard pile incorrect size')


  def test_bottomDraw(self):
    testDeck = Deck()

    card = testDeck.bottomDraw()
    self.assertEqual(card, ['BANGKOK', 'RED'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discardlen(), 1, 'discard pile incorrect size')

    card = testDeck.bottomDraw()
    self.assertEqual(card, ['BEIJING', 'RED'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discardlen(), 2, 'discard pile incorrect size')

    card = testDeck.bottomDraw()
    self.assertEqual(card, ['HO CHI MIN CITY', 'RED'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discardlen(), 3, 'discard pile incorrect size')


  def test_epidemic(self):
    testDeck = Deck()

    card = testDeck.draw()
    self.assertEqual(card, ['TEHRAN', 'BLACK'], 'did not draw top card')
    self.assertEqual(testDeck._discardlen(), 1, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 47, 'discard pile incorrect size')
    card = testDeck.draw()
    self.assertEqual(card, ['RIYADH', 'BLACK'], 'did not draw top card')
    self.assertEqual(testDeck._discardlen(), 2, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 46, 'discard pile incorrect size')
    card = testDeck.draw()
    self.assertEqual(card, ['MUMBAI', 'BLACK'], 'did not draw top card')
    self.assertEqual(testDeck._discardlen(), 3, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 45, 'discard pile incorrect size')

    card = testDeck.epidemic()
    self.assertEqual(card, ['BANGKOK', 'RED'], 'bottom draw returned incorrect card')
    self.assertEqual(testDeck._discardlen(), 0, 'discard pile incorrect size')
    self.assertEqual(len(testDeck), 48, 'discard pile incorrect size')


if __name__ == '__main__':
  unittest.main()
  