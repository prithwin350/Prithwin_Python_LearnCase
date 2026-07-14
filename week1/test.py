class CashPayment:
    def process(self):
        print("Collecting cash")


class CardPayment:
    def process(self):
        print("Charging card")


class UPIPayment:
    def process(self):
        print("Sending UPI request")

cash = CardPayment()
cash.process()