import json
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
        expected = (f"Statement for BigCo\n"
                    f"  Hamlet: $650.00 (55 seats)\n"
                    f"  As You Like It: $580.00 (35 seats)\n"
                    f"  Othello: $500.00 (40 seats)\n"
                    "Amount owed is $1,730.00\n"
                    "You earned 47 credits\n")
        actual = get_bill(invoice=json.loads(self.invoice)[0], plays=json.loads(self.plays))
        self.assertEqual(actual, expected)
