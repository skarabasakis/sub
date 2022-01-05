from .analyzer import analyze
from .parser import parse
from .runner import run

import sys

def main():
    try:
        command, name, args = analyze(sys.argv[1:])
        options = parse(args)
        run(command, name, options)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)

main()
