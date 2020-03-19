import json

def load_option_from_config(op: str):
    with open('config.json', 'r') as conf:
        data = json.load(conf)
        return data[op]

def write_option_to_config(op: str, value: str):
    with open('config.json', 'r') as conf:
        update = json.load(conf)
    update[op] = value
    with open('config.json', 'w+') as conf:
        json.dump(update, conf)
    return update
