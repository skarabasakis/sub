from .datatypes import cost, date, frequency

def parse_rate(value):
    try:
        cost_value, frequency_value = value.split('/')
    except ValueError:
        raise RuntimeError(f"Invalid rate: {value}")

    return {
        "cost": cost.parse(cost_value),
        "frequency": frequency.parse(frequency_value)
    }

def parse_start_date(value):
    return {
        "starts_on": date.parse(value)
    }

def parse_end_date(value):
    return {
        "ends_on": date.parse(value, prefer_future=True)
    }


PARSERS = {
    'for': parse_rate,
    'since': parse_start_date,
    'until': parse_end_date,
    'on': parse_end_date
}

def parse(options):
    parsed = dict()
    for option, value in options.items():
        parsed.update(parse_option(option, value))

    return parsed

def parse_option(option, value):
    if option not in PARSERS.keys():
        raise RuntimeError(f"Invalid option: {option}")

    return PARSERS[option](value)
