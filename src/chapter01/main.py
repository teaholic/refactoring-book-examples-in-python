import math

def get_statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"
    usd_amount = "${:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0
        if(play['type'] == "tragedy"):
            this_amount = 40000
            if(perf['audience'] > 30):
                this_amount += 1000 * (perf['audience'] - 30)
        elif(play['type'] == "comedy"):
            this_amount = 30000
            if (perf['audience'] > 20):
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            this_amount += 300 * perf['audience']
        else:
            raise Exception(f"unknown type: {play['type']}")

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if ("comedy"==play['type']):
            volume_credits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += f"  {play['name']}: {usd_amount.format(this_amount/100)} ({perf['audience']} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is {usd_amount.format(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result
