import argparse

parser = argparse.ArgumentParser(description="sample argument parser")
parser.add_argument("user", nargs="?", default="viCracker")
args = parser.parse_args()
if args.user == "Admin":
    print("Hello Admin")
else:
    print("Hello Guest")
