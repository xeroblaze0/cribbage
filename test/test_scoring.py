import unittest
from cribbage import scoring
import cribbage.playingcards as pc

class TestPairScoring_InHand(unittest.TestCase):
    def test_pair(self):
        
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['seven']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        s_card = pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['three'])
        
        s = scoring.HasPairTripleQuad_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 2)
        
    def test_two_pair(self):
        
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['seven']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        s_card = pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two'])
        s = scoring.HasPairTripleQuad_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 4)
        
    def test_three(self):
        
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        s_card = pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two'])
        s = scoring.HasPairTripleQuad_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 6)
        
    def test_four(self):
        
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        s_card = pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['nine'])
        s = scoring.HasPairTripleQuad_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 12)

class TestPairScoring_DuringPlay(unittest.TestCase):
    def setUp(self):
        pass

    def test_pair(self):
        s = scoring.HasPairTripleQuad_DuringPlay()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_pair_old(self):
        s = scoring.HasPairTripleQuad_DuringPlay()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_pair_triple(self):
        s = scoring.HasPairTripleQuad_DuringPlay()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)

    def test_pair_quadruple(self):
        s = scoring.HasPairTripleQuad_DuringPlay()
        hand = []
        for i in range(6):
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 12)

    def test_pair_nothing(self):
        s = scoring.HasPairTripleQuad_DuringPlay()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['eight'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_pair_minimumcards(self):
        s = scoring.HasPairTripleQuad_DuringPlay()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 6)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 12)


class TestExactlyEqualsN(unittest.TestCase):
    def setUp(self):
        pass

    def test_ExactlyEqualsN15_count_is_equal(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_ExactlyEqualsN15_count_is_less_than(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN15_count_is_greater_than(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN15_one_card(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN31_count_is_equal(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_ExactlyEqualsN31_count_is_less_than(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN31_count_is_greater_than(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)


class TestHasStraight_DuringPlay(unittest.TestCase):

    def setUp(self):
        self.s = scoring.HasStraight_DuringPlay()

    def test_HasStraight_DuringPlay_2card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_DuringPlay_3card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_DuringPlay_4card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 4)

    def test_HasStraight_DuringPlay_3card_after_broken(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_DuringPlay_6card_outoforder(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['three'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 6)

    def test_HasStraight_DuringPlay_4card_broken(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['two'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_DuringPlay_12card(self):
        hand = []
        for rank in pc.Deck.RANKS:
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[rank]))
        score, _ = self.s.check(hand)
        self.assertEqual(score, 13)


class TestHasStraight_InHand(unittest.TestCase):

    def test_HasStraight_InHand_3card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['ace'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['king'])
        s = scoring.HasStraight_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 3)
        
    def test_HasStraight_InHand_5card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['three'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven'])
        s = scoring.HasStraight_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 5)
        
    def test_HasStraight_InHand_double3(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['four'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['king'])
        s = scoring.HasStraight_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 6)
        
    def test_HasStraight_InHand_tripple3(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['four'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['four'])
        s = scoring.HasStraight_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 9)

    def test_HasStraight_InHand_double4(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['three']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['four'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['four'])
        s = scoring.HasStraight_InHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 8)

class TestCountCombinationsEqualToN(unittest.TestCase):
    def setUp(self):
        pass

    def test_CountCombinationsEqualToN_one(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_CountCombinationsEqualToN_two_overlapping(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_CountCombinationsEqualToN_two_nonoverlapping(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['eight'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 4)


class TestHasFlush(unittest.TestCase):
    def setUp(self):
        pass

    def test_noflush_four_card_crib(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['nine'])
        s = scoring.HasFlush(hand,s_card,True)
        score, _ = s.check()
        self.assertEqual(score, 0)

    def test_flush_crib(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four'])
        s = scoring.HasFlush(hand,s_card,True)
        score, _ = s.check()
        self.assertEqual(score, 5)

    def test_flush_four_card_hand(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['nine'])
        s = scoring.HasFlush(hand,s_card,False)
        score, _ = s.check()
        self.assertEqual(score, 4)
        
    def test_flush_five_card_hand(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four'])
        s = scoring.HasFlush(hand,s_card,False)
        score, _ = s.check()
        self.assertEqual(score, 5)
        
    def test_noflush_hand(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['jack'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four'])
        s = scoring.HasFlush(hand,s_card,False)
        score, _ = s.check()
        self.assertEqual(score, 0)

class test_15_hand(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_no_15(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['ace'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['three'])
        s = scoring.NinHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 0)
    
    def test_single_15(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['three']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['jack'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['three'])
        s = scoring.NinHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 2)
        
    def test_multiple_15(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['queen']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ten']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five'])]
        s_card = pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five'])
        s = scoring.NinHand(hand,s_card)
        score, _ = s.check()
        self.assertEqual(score, 12)

if __name__ == '__main__':
    unittest.main()
