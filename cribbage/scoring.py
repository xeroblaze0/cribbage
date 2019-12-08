"""Cribbage score conditions used during and after rounds."""
from itertools import combinations
from abc import ABCMeta, abstractmethod
from collections import namedtuple


class ScoreCondition(metaclass=ABCMeta):
    """Abstract Base Class"""

    def __init__(self):
        pass

    @abstractmethod
    def check(self, hand):
        raise NotImplementedError

class HandScoring:
    score = None
    description = ""
    def __init__(self, hand_cards, starter_card):
        self.hand_cards = hand_cards
        self.starter_card = starter_card
        #self.is_crib = is_crib
        self.all_cards = hand_cards.copy()
        self.all_cards.append(starter_card)

class NinHand(HandScoring):
    def check(self):
        ncounter = CountCombinationsEqualToN(n=15)
        s,description =  ncounter.check(self.all_cards)
        return s, description

class HasPairTripleQuad_DuringPlay(ScoreCondition):
    def check(self, cards):
        description = None
        pair_rank = ""
        same, score = 0, 0
        if len(cards) > 1:
            last = cards[-4:][::-1]
            while same == 0 and last:
                if all(card.rank['name'] == last[0].rank['name'] for card in last):
                    same = len(last)
                    pair_rank = last[0].rank['symbol']
                last.pop()
            if same == 2:
                score = 2
                description = "Pair (%s)" % pair_rank
            elif same == 3:
                score = 6
                description = "Pair Royal (%s)" % pair_rank
            elif same == 4:
                score = 12
                description = "Double Pair Royal (%s)" % pair_rank
        return score, description

class HasPairTripleQuad_InHand(HandScoring):
    def check(self):
        description = ""
        score = 0
        if len(self.all_cards) > 1:
            ranks = [card.rank['rank'] for card in self.all_cards]
            pos_pair = {x:ranks.count(x) for x in ranks}
            for k,v in pos_pair.items():
                if v == 2:
                    #found a pair
                    score += 2
                    description += "Pair (%s)" % k
                elif v == 3:
                    #found three of a kind
                    score += 6
                    description += "Three of a kind (%s)" % k
                elif v == 4:
                    #found four of a kind
                    score += 12
                    description += "Four of a kind (%s)" % k
        return score, description

class ExactlyEqualsN(ScoreCondition):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def check(self, cards):
        value = sum(i.get_value() for i in cards)
        score = 2 if value == self.n else 0
        description = "%d count" % self.n if score else ""
        return score, description


class HasStraight_InHand(HandScoring):

    @staticmethod
    def _enumerate_straights(cards):
        potential_straights = []
        straights = []
        straights_deduped = []
        if cards:
            for i in range(3,len(cards)+1):
                potential_straights += list(combinations(cards, i))
            for p in potential_straights:
                rank_set = set([card.rank['rank'] for card in p])
                if ((max(rank_set) - min(rank_set) + 1) == len(p) == len(rank_set)):
                    straights.append(set(p))
            for s in straights:
                subset = False
                for o in straights:
                    if s.issubset(o) and s is not o:
                        subset = True
                if not subset:
                    straights_deduped.append(s)
        return straights_deduped
        
    def check(self):
        description = ""
        points = 0
        #cards = self.all_cards
        straights = self._enumerate_straights(self.all_cards)
        for s in straights:
            assert len(s) >= 3, "Straights must be 3 or more cards."
            description += "%d-card straight " % len(s)
            points += len(s)
        return points, description


class HasStraight_DuringPlay(ScoreCondition):

    @staticmethod
    def _is_straight(cards):
        rank_set = set([card.rank['rank'] for card in cards])
        return ((max(rank_set) - min(rank_set) + 1) == len(cards) == len(rank_set)) if len(cards) > 2 else False

    @classmethod
    def check(cls, cards):
        description = ""
        card_set = cards[:]
        while card_set:
            if cls._is_straight(card_set):
                description = "%d-card straight" % len(card_set)
                return len(card_set), description
            card_set.pop(0)
        return 0, description

class CountCombinationsEqualToN(ScoreCondition):
    def __init__(self, n):
        self.n = n
        super().__init__()

    def check(self, cards):
        n_counts, score = 0, 0
        cmb_list = []
        card_values = [card.get_value() for card in cards]
        for i in range(len(card_values)):
            cmb_list += list(combinations(card_values, i + 1))
        for i in cmb_list:
            n_counts += 1 if sum(i) == self.n else 0
        description = "%d unique %d-counts" % (n_counts, self.n) if n_counts else ""
        score = n_counts * 2
        return score, description


class HasFlush(HandScoring):
    def __init__(self,hand_cards,starter_card,is_crib):
        self.is_crib = is_crib
        super().__init__(hand_cards,starter_card)
    
    def check(self):
        if self.is_crib:
            card_suits = [card.get_suit() for card in self.hand_cards]
            card_suits.append(self.starter_card.get_suit())
            d = {x:card_suits.count(x) for x in card_suits}
            if max(d.values()) == 5:
                self.score = 5
                self.description = "5-card flush, 5 score"
            else:
                self.score = 0
        elif not(self.is_crib):
            card_suits = [card.get_suit() for card in self.hand_cards]
            d = {x:card_suits.count(x) for x in card_suits}
            if max(d.values()) == 4:
                v = list(d.values())
                k=list(d.keys())
                flush_suit = k[v.index(max(v))]
                if flush_suit == self.starter_card.get_suit():
                    self.score = 5
                    self.description = "5-card flush, 5 score"
                else:
                    self.score = 4
                    self.description = "4-card flush, 4 score"
            else:
                self.score = 0
        else:
            raise Exception("Crib or hand not specified")
        return self.score, self.description    
        
        #card_suits = [card.get_suit() for card in cards]
        #suit_count = card_suits.count(cards[-1].get_suit())
        #score = suit_count if suit_count >= 4 else 0
        #assert score < 6, "Flush score exceeded 5"
        #description = "" if score < 4 else ("%d-card flush" % score)
        
