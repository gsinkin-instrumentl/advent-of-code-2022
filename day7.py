from optparse import OptionParser
from dataclasses import dataclass


@dataclass
class LocalDirectory:
    name: str
    children: list

    def size(self) -> int:
        return sum(c.size() for c in self.children)


@dataclass
class LocalFile:
    name: str
    file_size: int

    def size(self) -> int:
        return self.file_size
    


def find_eligible_deletion(input_path):
    current_directory = None
    current_command = None
    directory_stack = []
    all_directories = []
    with open(input_path) as infile:
        for line in infile:
            line = line.strip()
            
            if line.startswith("$"):
                current_command = None
                
                if line == "$ cd ..":
                    current_directory = directory_stack.pop(-1)
                elif line.startswith("$ cd "):
                    directory_name = line.split(" ")[-1]
                    
                    if current_directory:
                        directory_stack.append(current_directory)

                        current_directory = [d for d in current_directory.children if d.name == directory_name][0]
                    else:
                        current_directory = LocalDirectory(directory_name, [])

                    all_directories.append(current_directory)
            
                elif line == "$ ls":
                    current_command = "ls"
                    
            elif current_command == "ls":
                if line.startswith("dir "):
                    current_directory.children.append(LocalDirectory(line.split(" ")[-1], []))
                else:
                    size, name = line.split(" ")
                    current_directory.children.append(LocalFile(name, int(size)))

    used_space = all_directories[0].size()
    need = 30000000
    total_size = 70000000
    unused_space = total_size - used_space
    needed = need - unused_space
    return sorted([d.size() for d in all_directories if d.size() >= needed])[0]
                



if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day7_input.txt")

  (options, args) = parser.parse_args()
  print(find_eligible_deletion(options.input))

