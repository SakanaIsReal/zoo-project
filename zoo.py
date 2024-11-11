class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return "Error: Age can't be negative number."
        if 0 <= age <= 12:       # -1, 0, 1    | 11, 12 ,13
            return 50
        elif 13 <= age <= 20:    # 12, 13, 14  | 19, 20, 21
            return 100
        elif 21 <= age <= 60:    # 20, 21, 22  | 59, 60, 61
            return 150
        elif age > 60:         # 59, 60, 61
            return 100