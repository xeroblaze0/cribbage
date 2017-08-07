import unittest
import scoring
import playingcards as pc


class TestPairScoring(unittest.TestCase):

    def setUp(self):
        pass

    def test_pair_pair(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_pair_triple(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)

    def test_pair_quadruple(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        for i in range(6):
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 12)

    def test_pair_nothing(self):
        s = scoring.HasPairTripleQuad()
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
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['eight']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_pair_minimumcards(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 12)


class TestExactlyEqualsN(unittest.TestCase):

    def setUp(self):
        pass

    def test_ExactlyEqualsN15_count_is_equal(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_ExactlyEqualsN15_count_is_less_than(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN15_count_is_greater_than(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN15_one_card(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN31_count_is_equal(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_ExactlyEqualsN31_count_is_less_than(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN31_count_is_greater_than(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)


class TestHasStraight(unittest.TestCase):

    def setUp(self):
        pass

    def test_HasStraight_2card(self):
        s = scoring.HasStraight()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_3card(self):
        s = scoring.HasStraight()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']))
        score, _ = s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_4card(self):
        s = scoring.HasStraight()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']))
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_HasStraight_3card_after_broken(self):
        s = scoring.HasStraight()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_6card_outoforder(self):
        s = scoring.HasStraight()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['three']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)

    def test_HasStraight_4card_broken(self):
        s = scoring.HasStraight()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_12card(self):
        s = scoring.HasStraight()
        hand = []
        for rank in pc.Deck.RANKS:
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[rank]))
        score, _ = s.check(hand)
        self.assertEqual(score, 13)


class TestCountCombinationsEqualToN(unittest.TestCase):

    def setUp(self):
        pass

    def test_CountCombinationsEqualToN_one(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_CountCombinationsEqualToN_two_overlapping(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_CountCombinationsEqualToN_two_nonoverlapping(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['eight']))
        score, _ = s.check(hand)
        self.assertEqual(score, 4)


class TestHasFlush(unittest.TestCase):

    def setUp(self):
        pass

    def test_HasFlush_four_card_flush(self):
        s = scoring.HasFlush()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_HasFlush_five_card_flush(self):
        s = scoring.HasFlush()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 5)

    def test_HasFlush_three_card_non_flush(self):
        s = scoring.HasFlush()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_HasFlush_four_card_old_flush(self):
        """Tests to make sure latest card must be part of flush"""
        s = scoring.HasFlush()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_HasFlush_four_card_split_flush(self):
        s = scoring.HasFlush()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_HasFlush_four_card_split_flush(self):
        s = scoring.HasFlush()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['king']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['two']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        score, _ = s.check(hand)
        self.assertEqual(score, 5)


if __name__ == '__main__':
    unittest.main()