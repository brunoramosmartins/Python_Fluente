import collections

Card = collections.namedtuple('Card', ['rank','suit'])
# .namedtuple cria subclasses de tupla com campos nomeados

class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # str.split(sep = None, maxsplit = -1) Retorna uma lista das palavras na sequência
    # usando sep como sequencia delimitadora.
    # maxplit = -1 => numero ilimitado de divisoes
    # maxplit = Especif => numero Especif de divisoes

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# Para escolher uma carta aleatoria
# from random import choice
# choice(deck)
