from . import Subscription

class SubscriptionList:
    def __init__(self, subscriptions = []):
        self.subscriptions = subscriptions

    def has(self, name):
        # implicitly relies on Subscription.__eq__
        return name in self.subscriptions

    def get(self, name):
        if not self.has(name):
            raise RuntimeError(f"Subscription not found: {name}")

        # index(name) implicitly relies on Subscription.__eq__
        return self.subscriptions[self.subscriptions.index(name)]

    def items(self):
        return sorted(
            self.subscriptions,
            key = lambda subscription: subscription.starts_on
        )

    def add(self, name, options):
        if self.has(name):
            raise RuntimeError(f"Subscription already exists: {name}")

        subscription = Subscription(name, options)
        self.subscriptions.append(subscription)

    def delete(self, name):
        self.subscriptions.remove(name)

    def payments(self, start=None, end=None):
        return sorted(
           [payment for subscription in self.subscriptions for payment in subscription.payments(start, end)],
           key = lambda payment: payment.paid_on
        )

    def total(self, start=None, end=None):
        return sum([s.total(start, end) for s in self.subscriptions])
