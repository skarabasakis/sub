from datetime import date
from . import Payment

def stringify_count(count, singular, plural):
    if count == 0:
        return ''
    elif count == 1:
        return singular
    else:
        return f"{count} {plural}"

class Subscription:
    def __init__(self, name, options):
        try:
            self.name = name
            self.cost = options['cost']
            self.frequency = options['frequency']
            self.starts_on = options.get('starts_on', date.today())
            self.ends_on = options.get('ends_on', None)
        except KeyError as e:
            raise RuntimeError(f"Required option: {str(e)}")

    def is_active(self):
        if self.ends_on:
            return self.starts_on <= date.today() < self.ends_on
        else:
            return self.starts_on <= date.today()

    def cancel(self, ends_on = None):
        self.ends_on = ends_on or date.today()

    def payments(self, start = None, end = None):
        # Set date range from options, then truncate the range within
        # the bounds of the period where the subscription is active
        start = max(start or date.min, self.starts_on)
        end = min(end or date.today(), self.ends_on or date.max)

        # Skip all payment dates until start
        payment_date = self.starts_on
        while payment_date < start:
            payment_date += self.frequency

        # Take all payment dates until end
        payment_dates = []
        while payment_date < end:
            payment_dates.append(payment_date)
            payment_date += self.frequency

        return [Payment(self.name, self.cost, payment_date) for payment_date in payment_dates]

    def total(self, start=None, end=None):
        return sum([payment.cost for payment in self.payments(start, end)])


    def __eq__(self, obj):
        if isinstance(obj, str):
            return self.name == obj
        elif isinstance(obj, Subscription):
            return self.name == obj.name
        else:
            return False

    def __str__(self):
        f_active = '●' if self.is_active() else '○'
        f_name = self.name.ljust(24)
        f_cost = str(self.cost).rjust(9)
        f_frequency = ''.join([
            stringify_count(self.frequency.years, 'year', 'years'),
            stringify_count(self.frequency.months, 'month', 'months'),
            stringify_count(self.frequency.days, 'day', 'days'),
        ]).ljust(10)
        f_rate = f"{f_cost} / {f_frequency}"
        f_starts_on = self.starts_on.strftime('%Y-%m-%d')
        f_ends_on = self.ends_on.strftime('%Y-%m-%d') if self.ends_on else ''

        return f"{f_active} {f_name} {f_rate} {f_starts_on} - {f_ends_on}"
