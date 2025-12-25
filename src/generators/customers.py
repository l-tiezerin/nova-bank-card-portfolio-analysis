import pandas as pd
import numpy as np
from faker import Faker
from config import *

fake = Faker()

def generate_customers(n):
    return pd.DataFrame({
        "customer_id": range(1, n + 1),
        "customer_since": [fake.date_between("-10y", "-1y") for _ in range(n)],
        "segment": np.random.choice(
            ["mass", "affluent", "private"],
            size=n,
            p=[0.75, 0.20, 0.05]
        )
    })