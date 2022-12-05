from optparse import OptionParser

def win_multiple(player1_score, player2_score):
    if player1_score == player2_score:
        return 3
    elif player1_score == 1:
        if player2_score == 2:
            return 6
        return 0
    elif player1_score == 2:
        if player2_score == 1:
            return 0
        return 6
    else:
        # player1_score == 3
        if player2_score == 1:
            return 6
        return 0


def get_move(player1_move, result_score):
    if result_score == 3:
        return player1_move
    if result_score == 0:
        if player1_move == "A":
            return "C"
        elif player1_move == "B":
            return "A"
        else:
            # player1_move == "C":
            return "B"
    else:
        # Win
        if player1_move == "A":
            return "B"
        elif player1_move == "B":
            return "C"
        else:
            # player1_move == "C":
            return "A"
            


def find_rps_score(input_path):
    total_score = 0
    shapes = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    with open(input_path) as infile:
        for line in infile:
            player1_move, player2_move = line.strip().split(" ")
            player1_score = shapes[player1_move]
            result_score = shapes[player2_move]
            player2_score = shapes[get_move(player1_move, result_score)]
            total_score += player2_score + result_score
    return total_score


if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="input",
                    help="input file", metavar="INPUT", default="day2_input.txt")

  (options, args) = parser.parse_args()
  print(find_rps_score(options.input))
    
