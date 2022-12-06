from optparse import OptionParser


def fully_contained(input_path):
    overlapping = 0
    with open(input_path) as infile:
        for line in infile:
            elf_1_range, elf_2_range = line.strip().split(",")
            elf_1_min, elf_1_max = elf_1_range.split("-")
            elf_1_range = range(int(elf_1_min), int(elf_1_max) + 1)
            elf_2_min, elf_2_max = elf_2_range.split("-")
            elf_2_range = range(int(elf_2_min), int(elf_2_max) + 1)
            overlap = range(
                max(int(elf_1_min), int(elf_2_min)),
                min(int(elf_1_max), int(elf_2_max)) + 1
            )
            if overlap == elf_1_range or overlap == elf_2_range:
                overlapping += 1            
    return overlapping


def partially_overlapping(input_path):
    overlapping = 0
    with open(input_path) as infile:
        for line in infile:
            elf_1_range, elf_2_range = line.strip().split(",")
            elf_1_min, elf_1_max = elf_1_range.split("-")
            elf_1_range = range(int(elf_1_min), int(elf_1_max) + 1)
            elf_2_min, elf_2_max = elf_2_range.split("-")
            elf_2_range = range(int(elf_2_min), int(elf_2_max) + 1)
            overlap = range(
                max(int(elf_1_min), int(elf_2_min)),
                min(int(elf_1_max), int(elf_2_max)) + 1
            )
            if len(overlap) > 0:
                overlapping += 1            
    return overlapping



if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day4_input.txt")

  (options, args) = parser.parse_args()
  print(partially_overlapping(options.input))

