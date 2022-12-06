from optparse import OptionParser
from collections import defaultdict
import re


def move_one_by_one(stacks, move_command):
    how_many, from_where, to_where = re.findall("\d+", move_command)
    for _ in range(int(how_many)):
        stacks[int(to_where) - 1].insert(0, stacks[int(from_where) - 1].pop(0))


def move_in_bulk(stacks, move_command):
    how_many, from_where, to_where = re.findall("\d+", move_command)
    to_append = []
    for _ in range(int(how_many)):
        to_append.append(stacks[int(from_where) - 1].pop(0))
    for value in to_append[::-1]:
        stacks[int(to_where) - 1].insert(0, value)
    

def top_of_stacks(input_path):
    stacks = defaultdict(list)
    with open(input_path) as infile:
        for line in infile:
            if "[" in line:
                stack = 0
                offset = stack * 4
                while offset < len(line):
                    values = line[offset:offset + 4]
                    if values.strip() != "":
                        value = values[1]
                        stacks[stack].append(value)
                    stack += 1
                    offset = stack * 4
            elif line.startswith("move"):
                move_in_bulk(stacks, line)

    top_o_stacks = ""
    for key in sorted(stacks.keys()):
        top_o_stacks += stacks[key][0]
    return top_o_stacks
        



if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day5_input.txt")

  (options, args) = parser.parse_args()
  print(top_of_stacks(options.input))

