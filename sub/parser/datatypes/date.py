import dateparser

def parse(value, prefer_future=False):
    dt = dateparser.parse(value, settings={
        'PREFER_DATES_FROM': 'future' if prefer_future else 'past'
    })

    if dt is None:
        raise RuntimeError(f"Invalid date: {value}")

    return dt.date()
