import pickle
from .domain import SubscriptionList

DEFAULT_PATH = 'sub.dat'

def run(command, name = None, options = {}):
    subscription_list = load() or SubscriptionList()
    run_command(command, name, options, subscription_list)
    save(subscription_list)

def load(path = DEFAULT_PATH):
    try:
        with open(path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

def save(subscription_list, path = DEFAULT_PATH):
    with open(path, 'wb') as file:
        pickle.dump(subscription_list, file)

def run_command(command, name, options, subscription_list):
    if command == 'to':
        subscription_list.add(name, options)

    elif command == 'cancel':
        subscription_list.get(name).cancel()

    elif command == 'delete':
        subscription_list.delete(name)

    elif command == 'payments':
        start = options.get("starts_on")
        end = options.get("ends_on")

        if name:
            payments = subscription_list.get(name).payments(start,end)
        else:
            payments = subscription_list.payments(start, end)

        for payment in payments:
            print(payment)

    elif command == 'total':
        start = options.get("starts_on")
        end = options.get("ends_on")

        if name:
            total = subscription_list.get(name).total(start,end)
        else:
            total = subscription_list.total(start, end)

        print(total)

    elif command == 'list':
        for subscription in subscription_list.items():
            print(subscription)

    else:
        raise RuntimeError(f"Unsupported command: {command}")
