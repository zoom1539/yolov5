import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--evolve', type=int, nargs='?', const=300, help='evolve hyperparameters for x generations')
opt = parser.parse_args()

print(opt)
