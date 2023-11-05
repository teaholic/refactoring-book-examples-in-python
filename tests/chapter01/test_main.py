from unittest import TestCase

from src.chapter01.main import get_bill


class Test(TestCase):
    plays = """
    {
      "hamlet": {"name": "Hamlet", "type": "tragedy"},
      "as-like": {"name": "As You Like It", "type": "comedy"},
      "othello": {"name": "Othello", "type": "tragedy"}
    }
    """
    invoice = """
        [
          {
            "customer": "BigCo",
            "performances": [
              {
                "playID": "hamlet",
                "audience": 55
              },
              {
                "playID": "as-like",
                "audience": 35
              },
              {
                "playID": "othello",
                "audience": 40
              }
            ]
          }
        ]
        """

    def test_get_bill(self):
        expected = """
        Statement for BigCo
          Hamlet: $650.00 (55 seats)
          As You Like It: $580.00 (35 seats)
          Othello: $500.00 (40 seats)
        Amount owed is $1,730.00
        You earned 47 credits
        """
        actual = get_bill(invoice=self.invoice, plays=self.plays)
        self.assertEqual(actual, expected)
