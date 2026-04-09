import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", type=int)
args = parser.parse_args()
result = args.num * args.num

print("Square:", result)