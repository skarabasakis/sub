from decimal import Decimal
CENT = Decimal('0.01')

def parse(value):
    try:
        return Decimal(value).quantize(CENT)
    except:
        raise RuntimeError(f"Invalid cost: {value}")
