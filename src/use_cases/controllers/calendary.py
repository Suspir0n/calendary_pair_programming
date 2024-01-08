from src.repositorys.utils import Utils

class Starting:
    def __init__(self):
        result = Utils.popular_days_of_week()
        print(result)