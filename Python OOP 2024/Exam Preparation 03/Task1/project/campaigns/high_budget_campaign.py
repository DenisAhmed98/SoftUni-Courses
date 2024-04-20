#from ExamPreparation04.project.campaigns.base_campaign import BaseCampaign
from project.campaigns.base_campaign import BaseCampaign

class HighBudgetCampaign(BaseCampaign):
    BUDGET = 5000
    REQ_ENGAGEMENT_RATE = 1.2

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= (self.required_engagement * self.REQ_ENGAGEMENT_RATE):
            return True
        else:
            return False

