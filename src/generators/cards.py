import numpy as np
import pandas as pd

def generate_cards(customers):
    customers_with_card = customers.sample(
        frac=0.65, random_state=42
    )

    card_rows = []
    card_id = 1

    for _, row in customers_with_card.iterrows():
        n_cards = min(np.random.poisson(1.3) + 1, 3)

        for _ in range(n_cards):
            card_rows.append({
                "card_id": card_id,
                "customer_id": row["customer_id"],
                "limit": round(np.random.lognormal(8.5, 0.6), 2),
                "modality": np.random.choice(
                    ["credit", "hybrid", "debit"],
                    p=[0.6, 0.3, 0.1]
                ),
                "is_active": np.random.rand() < 0.85
            })
            card_id += 1

    return pd.DataFrame(card_rows)