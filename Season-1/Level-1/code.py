'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import *

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

# DEFINE CONSTANTS
PAYMENT_LIMIT = Decimal(1e+6)

def validorder(order: Order):
    paid = Decimal(0.0)
    eps = 1e-3
    to_pay = Decimal(0.0)
    
    for item in order.items:
        
        if item.type == 'payment':
            paid += Decimal(item.amount)
            
        elif item.type == 'product':
            to_pay += Decimal(item.amount * item.quantity)
            if to_pay >= PAYMENT_LIMIT:
                return "Total amount payable for an order exceeded"   
        else:
            return "Invalid item type: %s" % item.type
    
    net = Decimal(paid - to_pay)

    if net >= 0.0 + eps or net <= 0.0 - eps:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
    

