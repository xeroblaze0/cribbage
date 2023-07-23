"""Agents that interact with the CribbageGame."""
import random
from abc import ABCMeta, abstractmethod
from cribbage import scoring
from cribbage.playingcards import Deck, Card
import itertools
from itertools import combinations, permutations

import numpy as np
import matplotlib.pyplot as plt

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


class CPU_Player(Player):

    def score_hand(self, hand, s_card, is_crib):
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
    
    def deck_without_hand(self, hand):
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

        return deck

    def graph_stuff(self,hand, crib_permus, probs_tops, score_book, score_aves, score_tops):
    
        fig = plt.figure()
        
        # syntax for 3-D projection
        ax = fig.add_subplot(131,projection ='3d')
        
        # defining all 3 axis
        x=[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
        y=[1,2,3,4,5,0,2,3,4,5,0,1,3,4,5,0,1,2,4,5,0,1,2,3,5,0,1,2,3,4]
        # z = score_tops
        z=np.zeros(len(score_tops))


        # plotting
        dx=np.ones(len(crib_permus))
        dy=np.ones(len(crib_permus))
        dz=np.ones(len(score_tops))*score_tops

        ax.bar3d(x, y, z,dx,dy,dz)
        ax.set_title('3D plot of Top Scores')

        ax.set_xlabel('1st card')
        ax.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5])
        x_tick_labels = []
        for i in range(len(hand)):
            x_tick_labels.append(hand[i].__str__())
        ax.set_xticklabels(x_tick_labels)

        ax.set_ylabel('2nd card')
        ax.set_yticks([0.5,1.5,2.5,3.5,4.5,5.5])
        y_tick_labels = []
        for j in range(len(hand)):
            y_tick_labels.append(hand[j].__str__())
        ax.set_yticklabels(y_tick_labels)

        ax.set_zlabel('Points')

        ax = fig.add_subplot(132,projection ='3d')
        z=np.zeros(len(score_aves))

        # plotting
        dx=np.ones(len(crib_permus))
        dy=np.ones(len(crib_permus))
        dz=np.ones(len(score_aves))*score_aves

        ax.bar3d(x, y, z,dx,dy,dz)
        ax.set_title('3D plot of Average Scores')

        ax.set_xlabel('1st card')
        ax.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5])
        x_tick_labels = []
        for i in range(len(hand)):
            x_tick_labels.append(hand[i].__str__())
        ax.set_xticklabels(x_tick_labels)

        ax.set_ylabel('2nd card')
        ax.set_yticks([0.5,1.5,2.5,3.5,4.5,5.5])
        y_tick_labels = []
        for j in range(len(hand)):
            y_tick_labels.append(hand[j].__str__())
        ax.set_yticklabels(y_tick_labels)

        ax.set_zlabel('Points')

        ax = fig.add_subplot(133,projection ='3d')
        z=np.zeros(len(probs_tops))

        # plotting
        dx=np.ones(len(crib_permus))
        dy=np.ones(len(crib_permus))
        dz=np.ones(len(probs_tops))*probs_tops

        ax.bar3d(x, y, z,dx,dy,dz)
        ax.set_title('3D plot of Most Likely Scores')

        ax.set_xlabel('1st card')
        ax.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5])
        x_tick_labels = []
        for i in range(len(hand)):
            x_tick_labels.append(hand[i].__str__())
        ax.set_xticklabels(x_tick_labels)

        ax.set_ylabel('2nd card')
        ax.set_yticks([0.5,1.5,2.5,3.5,4.5,5.5])
        y_tick_labels = []
        for j in range(len(hand)):
            y_tick_labels.append(hand[j].__str__())
        ax.set_yticklabels(y_tick_labels)

        ax.set_zlabel('Points')
        plt.show()
    
    def _optimistic(self, hand):
        
        # deck = self.deck_without_hand(hand)
        crib_permus = list(permutations(hand,2))

        probs_book = []
        score_book = []
        score_aves = []
        score_tops = []
        probs_tops = []

        top_hand = []
        top_score = 0
        
        for i in range(len(crib_permus)):

            deck = self.deck_without_hand(hand)
            
            hand.remove(crib_permus[i][0])
            hand.remove(crib_permus[i][1])

            score_list = []
            count_list = []
            temp_top_score = 0
            
            while deck.cards:
                draw = deck.draw()
                score = self.score_hand(hand, draw, is_crib=False)
                score_list.append(score)
                # print("crib: " + str(crib_permus[i]) + "draw: " + str(draw), "score: " + str(score))

                if score > temp_top_score:
                    temp_top_score = score

                if score > top_score:
                    top_score = score
                    # top_hand = crib_permus[i]

            temp_top_count_score = 0
            temp_top_count = 0

            for j in range(len(score_list)):
                score = score_list[j]
                score_count = score_list.count(score)
                # print(str(crib_permus[i]) + ": score:" + str(score_list[j]) + "count:" + str(score_count))

                # find score most often scored, bias for higher score if tie
                if score_count >= temp_top_count and score >= temp_top_count_score:
                    temp_top_count = score_count
                    temp_top_count_score = score

                # attach times-score-was-scored to list
                count_list.append(score_count)

            probs_book.append(count_list)
            score_book.append(score_list)
            probs_tops.append(temp_top_count_score)
            score_tops.append(temp_top_score)
            score_aves.append(np.mean(score_list))

            # goes at end, do calcs first
            hand.append(crib_permus[i][0])
            hand.append(crib_permus[i][1])
            # deck.trash_card(draw)

        self.graph_stuff(hand, crib_permus, probs_tops, score_book, score_aves, score_tops)

    def select_crib_cards(self, hand):

        # self._get_priori(hand)
        self._optimistic(hand)
        # play_hand = self._get_priori(hand)
            
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
