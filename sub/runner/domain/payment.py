class Payment:
    def __init__(self, name, cost, paid_on):
        self.name = name
        self.cost = cost
        self.paid_on = paid_on

    def __str__(self):
        f_name = self.name
        f_cost = str(self.cost).rjust(9)
        f_paid_on = self.paid_on.strftime('%Y-%m-%d')

        return f"{f_paid_on} {f_cost} {f_name}"
