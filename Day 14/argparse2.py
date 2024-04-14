import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("-surname")
args = parser.parse_args()
print(f"My name is {args.name}", end=" ")
if args.surname:
    print(args.surname)
