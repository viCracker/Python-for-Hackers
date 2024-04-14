import argparse

parser = argparse.ArgumentParser()
parser.add_argument("attack", choices=["XSS", "DDOS", "RCE"])
args = parser.parse_args()
print("type of attack: ", args.attack)
