class PerMonth:

    def __init__(
        self,
        initial_day: int,
        respective_day: int,
        week_day: str,
        is_initial_day: bool,
        is_respective_day: bool,
        is_week_day: bool,
        result: int,
        month: list
    ):
        self.initial_day = initial_day
        self.respective_day = respective_day
        self.week_day = week_day
        self.is_initial_day = is_initial_day
        self.is_respective_day = is_respective_day
        self.is_week_day = is_week_day
        self.result = result
        self.month = month