from optparse import OptionParser


def find_start_packet(input_path):
    with open(input_path) as infile:
        prev = []
        index = 1
        while True:
            current = infile.read(1)
            if not current:
                break
            if len(prev) < 13:
                prev.append(current)
                index += 1
            elif len(set([current] + prev)) == 14:
                return index
            else:
                prev.append(current)
                prev.pop(0)
                index += 1


if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day6_input.txt")

  (options, args) = parser.parse_args()
  print(find_start_packet(options.input))

