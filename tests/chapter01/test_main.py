import json
from unittest import TestCase

from parameterized import parameterized

from src.chapter01.main import get_statement


class TestStatement(TestCase):
    plays = """
    {
      "hamlet": {"name": "Hamlet", "type": "tragedy"},
      "as-like": {"name": "As You Like It", "type": "comedy"},
      "othello": {"name": "Othello", "type": "tragedy"}
    }
    """
    unsupported_plays = """
        {
          "hamlet": {"name": "abc", "type": "foo"},
          "as-like": {"name": "bcd", "type": "bar"},
          "othello": {"name": "cde", "type": "baz"}
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
          },
          {
            "customer": "SmallCo",
            "performances": [
              {
                "playID": "hamlet",
                "audience": 25
              },
              {
                "playID": "as-like",
                "audience": 15
              },
              {
                "playID": "othello",
                "audience": 30
              }
            ]
          }
        ]
        """
    expected_bigco_statement = (
        f"Statement for BigCo\n"
        f"  Hamlet: $650.00 (55 seats)\n"
        f"  As You Like It: $580.00 (35 seats)\n"
        f"  Othello: $500.00 (40 seats)\n"
        "Amount owed is $1,730.00\n"
        "You earned 47 credits\n"
    )
    expected_smallco_statement = (
        f"Statement for SmallCo\n"
        f"  Hamlet: $400.00 (25 seats)\n"
        f"  As You Like It: $345.00 (15 seats)\n"
        f"  Othello: $400.00 (30 seats)\n"
        "Amount owed is $1,145.00\n"
        "You earned 3 credits\n"
    )

    @parameterized.expand(
        [
            (json.loads(invoice)[0], json.loads(plays), expected_bigco_statement),
            (json.loads(invoice)[1], json.loads(plays), expected_smallco_statement),
        ]
    )
    def test_get_statement(self, invoice, plays, expected):

        actual = get_statement(invoice=invoice, plays=plays)
        self.assertEqual(actual, expected)

    def test_get_statement_exception(self):
        self.assertRaises(Exception, get_statement, json.loads(self.invoice)[0], json.loads(self.unsupported_plays))


