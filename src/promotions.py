class Promotion:
    def __init__(self, name: str, promotion_type: str, regions: list):
        self.name = name
        self.promotion_type = promotion_type
        self.regions = regions

    def get_name(self):
        return self.name
    
    def get_regions(self):
        return self.regions
    
    def get_promotion_type(self):
        return self.promotion_type

class PromotionWithTrackingCode(Promotion):
    def __init__(self, tracking_codes: list):
        self.tracking_codes = tracking_codes
    
    def get_tracking_codes(self):
        return self.tracking_codes