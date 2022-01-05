OPTIONS = {
    'to': ['for', 'since', 'until'],
    'list': [],
    'delete': [],
    'cancel': ['on'],
    'payments': ['since', 'until'],
    'total': ['since', 'until'],
}
COMMANDS = OPTIONS.keys()


def analyze(argv):
    if len(argv) == 0:
        raise RuntimeError("Usage: sub <command> <options>")

    command, *options_argv = argv
    if command not in COMMANDS:
        raise RuntimeError(f"Invalid command: {command}")

    options = analyze_options(options_argv, OPTIONS[command])

    return (command, *options)


def analyze_options(argv, keywords):
    # argv = ["netflix.com", "for", "14/m", "since", "last", "week", "until", "today"]
    keyword_indexes = sorted([i for i, arg in enumerate(argv) if arg in keywords])
    # keyword_indexes = [1,3,6]
    slice_indexes =  zip([None, *keyword_indexes], [*keyword_indexes, None])
    # slice_indexes [(None, 1), (1,3), (3,6), (6,None)]
    slices = [argv[start:end] for start, end in slice_indexes]
    # keyword_slices = [['netflix.com'], ['for', '14/m'], ['since', 'last', 'week'], ['until', 'today']]
    name_slice, *option_slices = slices
    # name_slice = ['netflix.com']
    # option_slices = ['for', '14/m'], ['since', 'last', 'week'], ['until', 'today']

    name = None if len(name_slice) == 0 else ' '.join(name_slice)
    options = {option: ' '.join(values) for option, *values in option_slices}

    return (name, options)
