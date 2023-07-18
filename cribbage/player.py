"""Agents that interact with the CribbageGame."""
import random
from abc import ABCMeta, abstractmethod
from cribbage import scoring
from cribbage.playingcards import Deck, Card

class Player(metaclass=ABCMeta):
    """Abstract Base Class"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    @abstractmethod
    def select_crib_cards(self, hand):
        """Select cards to place in crib.

        :param hand: list containing the cards in the player's hand
        :return: list of cards to place in crib
        """
        raise NotImplementedError

    @abstractmethod
    def select_card_to_play(self, hand, table, crib):
        """Select next card to play.

        :param hand: list containing the cards in the player's hand
        :param table: list of all cards that have been played so far during the current round (by all players)
        :param crib: list of cards that the player has placed in the crib
        :return: card to play
        """
        raise NotImplementedError


class RandomPlayer(Player):
    """A player that makes random decisions."""

    def select_crib_cards(self, hand):
        return random.sample(hand, 2)

    def select_card_to_play(self, hand, table, crib):
        return random.choice(hand)


class MaxPoints(Player):

    def _score_hand(self, hand, s_card, is_crib):
        """Score a hand at the end of a round.

        :param cards: Cards in a single player's hand.
        :return: Points earned by player.
        """
        score = 0
        score_scenarios = [scoring.NinHand(hand, s_card),
                           scoring.HasPairTripleQuad_InHand(hand, s_card), scoring.HasStraight_InHand(hand, s_card), scoring.HasFlush(hand, s_card, is_crib)]
        for scenario in score_scenarios:
            s, desc = scenario.check()
            score += s
            # print("[EOR SCORING] " + desc) if desc else None
        
        return score
    
    # def _get_priori(self,hand):
    def _get_assumption(self,hand):
        # imagine a deck
        deck=Deck()
        
        # find your cards in the deck
        hand_index=[]
        for i in range(len(deck.cards)):
            for ii in range(len(hand)):
                # print(i, ii)
                if deck.cards[i].rank == hand[ii].rank and deck.cards[i].suit == hand[ii].suit:
                    print(i, deck.cards[i], hand[ii])
                    hand_index.append(i)

        # remove and/or clone your hand from the deck
        clone=[]
        for x in range(len(hand_index)):
            clone.append(deck.cards.pop(hand_index[x]-x))

    # def _get_assumption(self,hand):

        num_ace=0
        num_two=0
        num_three=0
        num_four=0
        num_five=0
        num_six=0
        num_seven=0
        num_eight=0
        num_nine=0
        num_ten=0
        num_jack=0
        num_queen=0
        num_king=0

        num_spades=0
        num_hearts=0
        num_clubs=0
        num_diamonds=0

        print(hand)
        for i in range(len(deck)):
            # print(card.rank["name"], card.suit["name"])

            if deck.cards[i].rank["name"] == 'ace':
                num_ace+=1
            elif deck.cards[i].rank["name"] == 'two':
                num_two+=1
            elif deck.cards[i].rank["name"] == 'three':
                num_three+=1
            elif deck.cards[i].rank["name"] == 'four':
                num_four+=1
            elif deck.cards[i].rank["name"] == 'five':
                num_five+=1
            elif deck.cards[i].rank["name"] == 'six':
                num_six+=1
            elif deck.cards[i].rank["name"] == 'seven':
                num_seven+=1
            elif deck.cards[i].rank["name"] == 'eight':
                num_eight+=1
            elif deck.cards[i].rank["name"] == 'nine':
                num_nine+=1
            elif deck.cards[i].rank["name"] == 'ten':
                num_ten+=1
            elif deck.cards[i].rank["name"] == 'jack':
                num_jack+=1
            elif deck.cards[i].rank["name"] == 'queen':
                num_queen+=1
            elif deck.cards[i].rank["name"] == 'king':
                num_king+=1
            
            if deck.cards[i].suit["name"] == 'spades':
                num_spades+=1
            elif deck.cards[i].suit["name"] == 'hearts':
                num_hearts+=1
            elif deck.cards[i].suit["name"] == 'clubs':
                num_clubs+=1
            elif deck.cards[i].suit["name"] == 'diamonds':
                num_diamonds+=1
        
        print(num_ace, num_two, num_three, num_four, num_five, num_six, num_seven, num_eight, num_nine, num_ten, num_jack, num_queen, num_king, num_spades, num_hearts, num_clubs, num_diamonds)

    def _optimistic(self, hand):
        
        # imagine a deck
        deck=Deck()
        
        # find your cards in the deck
        hand_index=[]
        for i in range(len(deck.cards)):
            for ii in range(len(hand)):
                # print(i, ii)
                if deck.cards[i].rank == hand[ii].rank and deck.cards[i].suit == hand[ii].suit:
                    # print(i, deck.cards[i], hand[ii])
                    hand_index.append(i)

        # remove and/or clone your hand from the deck
        # clone=[]
        for x in range(len(hand_index)):
            # clone.append(deck.cards.pop(hand_index[x]-x))
            deck.cards.pop(hand_index[x]-x)

        # draw card, score the potential hands
        # returns hand based on highest possible score
        top_points = 0
        top_hand = []

        for i in range(len(hand)):
            temp_hand = hand
            first_removal=temp_hand.pop(i)
            for ii in range(len(temp_hand)):
                temp_temp_hand = temp_hand
                second_removal=temp_temp_hand.pop(ii)

                draw = deck.draw()
                score = self._score_hand(temp_temp_hand, draw, is_crib=False)
                
                if score > top_points:
                    top_points = score
                    # top_card = draw
                    top_hand = [first_removal, second_removal]

                temp_temp_hand.insert(ii, second_removal)
            temp_hand.insert(i, first_removal)

        # print(top_points, top_hand, top_card)
        return top_hand

    def select_crib_cards(self, hand):

        play_hand = self._optimistic(hand)
            
        # print(play_hand)        
        return play_hand

    def select_card_to_play(self, hand, table, crib):
        return random.choice(hand)
    
class HumanPlayer(Player):
    """Interface for a human user to play."""

    def present_cards_for_selection(self, cards, n_cards=1):
        """Presents a text-based representation of the game via stdout and prompts a human user for decisions.

        :param cards: list of cards in player's hand
        :param n_cards: number of cards that player must select
        :return: list of n_cards cards selected from player's hand
        """
        cards_selected = []
        while len(cards_selected) < n_cards:
            s = ""
            for idx, card in enumerate(cards):
                s += "(" + str(idx + 1) + ") " + str(card)
                if card != cards[-1]:
                    s += ","
                s += " "
            msg = "Select a card: " if n_cards == 1 else "Select %d cards: " % n_cards
            print(s)
            selection = input(msg)
            card_indices = [int(s) for s in selection.split() if s.isdigit()]
            for idx in card_indices:
                if idx < 1 or idx > len(cards):
                    print("%d is an invalid selection." % idx)
                else:
                    cards_selected.append(cards[idx-1])
        return cards_selected

    def select_crib_cards(self, hand):
        return self.present_cards_for_selection(cards=hand, n_cards=2)

    def select_card_to_play(self, hand, table, crib):
        return self.present_cards_for_selection(cards=hand, n_cards=1)[0]
