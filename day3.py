from optparse import OptionParser
import string


def find_loadout(file_path):
    total_priority = 0
    with open(file_path) as infile:
        for line in infile:
            line = line.strip()
            half = int(len(line) / 2)
            first_half = set(line[:half])
            second_half = set(line[half:])
            both = first_half & second_half
            total_priority += sum([string.ascii_letters.find(letter) + 1 for letter in both])
    return total_priority


def find_loadout_2(file_path):
    total_priority = 0
    with open(file_path) as infile:
        elves = []
        for line in infile:
            elves.append(set(line.strip()))
            if len(elves) == 3:
                common_item = elves[0] & elves[1] & elves[2]
                total_priority += sum([string.ascii_letters.find(letter) + 1 for letter in common_item])
                elves = []
    return total_priority
                


if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day3_input.txt")

  (options, args) = parser.parse_args()
  print(find_loadout_2(options.input))

