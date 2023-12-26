import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("double", help="display a double of a given number", type=int)
args = parser.parse_args()
print("square:", args.square**2)
print("double:", args.double*2)

