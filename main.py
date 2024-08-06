## Promo Tracker - v. 0.10

import pandas as pandas
from src import promotion
from src.promo_tracker.tracker import PromotionTracker
from src.TextLogger.text_logger import TextLogger


# Display all table columns
pandas.set_option('display.max_columns', None)

# Reading database
database = pandas.read_excel('promo_db.xlsx')

# Building promotions for mapping
TopRunner = promotion.PromotionWithTrackingCode(
    name = 'Top Runner',
    regions = ['US & Canada'],
    tracking_codes = ['TopRunner'],
    promotion_type = 'Revenue'
)

promotions_list = [
    TopRunner
]

# Applying promotions mapping to database
PromotionTracker = PromotionTracker(database, promotions_list)
PromotionTracker.apply_promotions()

# Saving changes to database
TextLogger.log_text(text = 'STATUS: Getting ready for export.')
database.to_excel('export.xlsx')
TextLogger.log_text(text = 'Export Completed.')
