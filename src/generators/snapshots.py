import pandas as pd
from dateutil.relativedelta import relativedelta
from config import *

def generate_months():
    return [
        START_DATE + relativedelta(months=i)
        for i in range(MONTHS)
    ]

def customer_snapshots(customers):
    months = generate_months()
    frames = []

    for m in months:
        snap = customers.copy()
        snap["ref_month"] = m
        frames.append(snap)

    return pd.concat(frames, ignore_index=True)