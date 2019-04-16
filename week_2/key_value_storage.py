import os
import json
import tempfile
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

file_exists = os.path.isfile('/tmp/storage.data')
if not file_exists:
    open(storage_path, 'w+')

with open(storage_path, 'r') as storage_file:
    try:
        key_value_storage = json.load(storage_file)
    except ValueError:
        key_value_storage = {}

parser = argparse.ArgumentParser()
parser.add_argument("--key", action='store', help="key of the value")
parser.add_argument("--value", action='store', help="value corresponding to a key")

def add_key_value(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]

args = parser.parse_args()
if args.key and not args.value:
    print(key_value_storage.get(args.key, None))
elif args.key and args.value:
    add_key_value(key_value_storage, args.key, args.value)
    with open(storage_path, 'w') as storage_file:
        json.dump(key_value_storage, storage_file)
