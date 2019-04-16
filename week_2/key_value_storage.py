import os
import json
import tempfile
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'r') as storage_file:
    try:
        key_value_storage = json.load(storage_file)
    except ValueError:
        key_value_storage = {}

parser = argparse.ArgumentParser()
parser.add_argument("--key", action='store', help="key of the value")
parser.add_argument("--value", action='store', help="value corresponding to a key")

args = parser.parse_args()
if args.key and not args.value:
    print(key_value_storage.get(args.key, None))
elif args.key and args.value:
    key_value_storage[args.key] = args.value
    with open(storage_path, 'w') as storage_file:
        json.dump(key_value_storage, storage_file)
