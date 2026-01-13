# router.py
from skills.general import general_summary
from skills.food import analyze_food
from skills.service import analyze_service
from skills.pricing import analyze_pricing

def route_question(question: str):
    q = question.lower()

    # FOOD
    if any(x in q for x in ["taste", "food", "flavor", "freshness", "menu"]):
        return "food", analyze_food

    # SERVICE
    if any(x in q for x in ["waiter", "service", "staff", "rude", "slow"]):
        return "service", analyze_service

    # PRICING
    if any(x in q for x in ["price", "expensive", "cheap", "overpriced", "value"]):
        return "pricing", analyze_pricing

    # DEFAULT — GENERAL REVIEW
    return "general", general_summary
