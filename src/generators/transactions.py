import numpy as np
import pandas as pd

def generate_transactions(cards, ref_month):
    active_cards = cards[cards["is_active"]]

    rows = []

    for _, card in active_cards.iterrows():
        n_tx = np.random.poisson(3)

        for _ in range(n_tx):
            rows.append({
                "card_id": card["card_id"],
                "ref_month": ref_month,
                "amount": round(np.random.lognormal(4.5, 0.9), 2),
                "installments": np.random.choice(
                    [1, 2, 3, 4, 6, 9, 12],
                    p=[0.55, 0.15, 0.10, 0.08, 0.07, 0.03, 0.02]
                )
            })

    return pd.DataFrame(rows)