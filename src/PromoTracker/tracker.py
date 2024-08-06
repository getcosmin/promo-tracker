class PromotionTracker:
    def __init__(self, database, promotions: list):
        self.datase = detabase
        self.promotions = promotions
    
    def find_regions(self, promotion, column: str):
        return self.database[column].apply(
            lambda region: region in promotion.regions
        )
    
    def find_code(self, code, column):
        return self.database[column].str.contains(
            code, case = False, na = False
        )
    
    def apply_promotions(self):
        DatabaseManager.create_column(self.database, 'Promotion Name')
        for promotion in self.promotions:
            print(f'Searching for {promotion.name}...')
            for code in promotion.tracking_codes:
                has_promo_code = self.find_code(code, 'Promo Code')
                is_region_valid = self.find_regions(promotion, 'Region POS')
                final_filtering = has_promo_code & is_region_valid
                self.database.loc[final_filtering, 'Promotion Name'] = promotion.get_name()



class DatabaseManager:
    @classmethod
    def create_column(cls, database, column: str):
        if column not in database.columns:
            database[column] = None