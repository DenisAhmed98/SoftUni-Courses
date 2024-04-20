from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign,
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        try:
            influencer = self.VALID_INFLUENCERS[influencer_type](username,followers,engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."
        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."
        if [c for c in self.campaigns if c.campaign_id == campaign_id]:
            return f"Campaign ID {campaign_id} has already been created."

        campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = [i for i in self.influencers if i.username == influencer_username]
        if not influencer:
            return f"Influencer '{influencer_username}' not found."
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."
        if not campaign[0].check_eligibility(influencer[0].engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        payment = influencer[0].calculate_payment(campaign[0])
        if payment > 0.0:
            campaign[0].approved_influencers.append(influencer[0])
            campaign[0].budget -= payment
            influencer[0].campaigns_participated.append(campaign[0])
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total = {}
        for campaign in self.campaigns:
            if campaign.approved_influencers:
                total[campaign] = 0
                for influencer in campaign.approved_influencers:
                    if campaign in influencer.campaigns_participated:
                        total[campaign] += influencer.reached_followers(campaign.__class__.__name__)
        return total

    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username]
        if influencer:
            return influencer[0].display_campaigns_participated()

    def campaign_statistics(self):
        campaigns_sorted = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        statistics = ["$$ Campaign Statistics $$"]
        for campaign in campaigns_sorted:
            total_followers = self.calculate_total_reached_followers()
            total_campaign_followers = total_followers[campaign]
            statistics.append(f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
                              f"Total budget: ${campaign.budget:.2f}, "
                              f"Total reached followers: {total_campaign_followers}")
        return "\n".join(statistics)

