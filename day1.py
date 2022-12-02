from optparse import OptionParser
from collections import defaultdict



def find_max_calories(input_path):
    calories_by_elf = defaultdict(int)
    elf_index = 0
    with open(input_path) as infile:
        for line in infile:
            try: 
                calories_by_elf[elf_index] += int(line)
            except ValueError:
                elf_index += 1

    return sum(sorted(calories_by_elf.values())[-3:])


if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day1_input.txt")

  (options, args) = parser.parse_args()
  print(find_max_calories(options.input))
    



