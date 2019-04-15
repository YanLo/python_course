import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=any , help="key of the value")
parser.add_argument("--value", type=any, help="value corresponding to key")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'w') as storage_file:
    pass

with open(storage_path, 'r') as storage_file:
    key_value_storage = json.load(storage_file)
    print(key_value_storage)

if args.key and not args.value:
    print(key_value_storage.get(str(args.key), None))
elif args.key and args.value:
    key_value_storage[str(args.key)] = args.value
    with open(storage_path, 'w') as storage_file:
        json.dump(key_value_storage, storage_file)
