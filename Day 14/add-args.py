import sys
import argparse

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# total = num1 + num2
# print(f"total is: {total}")

parser = argparse.ArgumentParser()
parser.add_argument("-num1")
parser.add_argument("-num2")
args = parser.parse_args()
total = int(args.num1) + int(args.num2)
print(f"total is {args.num1}")
