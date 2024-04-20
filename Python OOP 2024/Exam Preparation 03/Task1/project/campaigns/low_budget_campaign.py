#from ExamPreparation04.project.campaigns.base_campaign import BaseCampaign
from project.campaigns.base_campaign import BaseCampaign

class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2500
    REQ_ENGAGEMENT_RATE = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= (self.required_engagement * self.REQ_ENGAGEMENT_RATE):
            return True
        else:
            return False