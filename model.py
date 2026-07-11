# Simplified model for MHS Predictor

def predict(data):
    """
    Simple heuristic model:
    - If awareness >= 50 and income >= 3000 and age between 18 and 35 => predict usage (1)
    - Otherwise predict 0
    """
    age = data.get('age', 0)
    awareness = data.get('awareness', 0)
    income = data.get('income', 0)
    if 18 <= age <= 35 and awareness >= 50 and income >= 3000:
        return 1
    return 0
