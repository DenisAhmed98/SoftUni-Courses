from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INIT_PAYMENT_PERCENTAGE = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * self.INIT_PAYMENT_PERCENTAGE

        return payment

    def reached_followers(self, campaign_type: str):
        reached_followers_value = 0
        if campaign_type == "HighBudgetCampaign":
            reached_followers_value = self.followers * self.engagement_rate * 1.2
        elif campaign_type == "LowBudgetCampaign":
            reached_followers_value = self.followers * self.engagement_rate * 0.9

        return int(reached_followers_value)
