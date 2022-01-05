from dateutil.relativedelta import relativedelta

UNITS =  {
    'd': 'days',
    'm': 'months',
    'y': 'years'
}

def parse(value):
    try:
        f_value, u_value = value[:-1], value[-1]
        factor = parse_factor(f_value)
        unit = parse_unit(u_value)
        return relativedelta(**{unit: factor})
    except:
        raise RuntimeError(f"Invalid frequency: {value}")

def parse_factor(value):
    if value.strip() == '':
        return 1

    try:
        count = int(value)
    except:
        raise RuntimeError(f"Invalid frequency factor: {value}")

    if count <= 0:
        raise RuntimeError(f"Invalid frequency factor: {value} (must be positive)")

    return count

def parse_unit(value):
    if value not in UNITS.keys():
        raise RuntimeError(f"Invalid frequency unit: {value} (must be one of (d,m,y))")

    return UNITS[value]
