
def initDeck():

  lines = [line.strip() for line in open('../resources/cardlist.txt')]

  lines.remove('RED')
  lines.remove('YELLOW')
  lines.remove('BLUE')
  lines.remove('BLACK')
  lines.remove('')
  lines.remove('')
  lines.remove('')

  # red = lines[0:12]
  # yellow = lines[12:24]
  # blue = lines[24:36]
  # black = lines[36:48]
  # print red
  # print yellow
  # print blue
  # print black

  decklist = []

  for row in lines:
    x = lines.index(row)
    if x < 12:
      decklist.append([row,'RED',0])
    elif x > 12 and x < 24:
      decklist.append([row,'YELLOW',0])
    elif x > 24 and x < 36:
      decklist.append([row,'BLUE',0])
    elif x > 36 and x < 48:
      decklist.append([row,'BLACK',0])

  # for row in decklist:
    # print row
  return decklist