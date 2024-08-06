## Promo Tracker - v. 0.10

import pandas as pandas
from src import promotion
from src.promo_tracker.tracker import PromotionTracker


# Display all table columns
pandas.set_option('display.max_columns', None)

database = pandas.read_excel('promo_db.xlsx')

