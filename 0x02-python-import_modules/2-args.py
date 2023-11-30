#!/usr/bin/python3
import sys

if __name__ == "__main__":
argc = len(sys.argv) - 1
arg_str = "{:d} argument" + ('s.' if argc == 0 else ':' if argc == 1 else 's:')

print(arg_str.format(argc))

for i, arg in enumerate(sys.argv):
if i != 0:
print("{:d}: {:s}".format(i, arg))
