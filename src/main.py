import numpy as np
from generators.customers import generate_customers
from generators.cards import generate_cards
from generators.snapshots import customer_snapshots
from generators.transactions import generate_transactions
from generators.snapshots import generate_months

np.random.seed(42)

customers = generate_customers(500_000)
cards = generate_cards(customers)

customer_monthly = customer_snapshots(customers)

transactions = []
for m in generate_months():
    transactions.append(generate_transactions(cards, m))

transactions = pd.concat(transactions, ignore_index=True)