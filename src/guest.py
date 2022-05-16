class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def sufficient_funds(self, room):
        return self.wallet >= room.entry_fee

    def pay_entrance_fee(self, room):
        self.wallet -= room.entry_fee
