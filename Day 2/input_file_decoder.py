# To decode the text in the input file and convert it into lists of numbers
# List order: [R, G, B]]
def convert_to_list(input_file):
    RGB = ["red", "green", "blue"]
    games_list = []
    for line in open(input_file, 'r'):
        game_id_and_game = line.split(":")
        game_id = int(str(game_id_and_game[0]).replace("Game ", ""))
        rounds = game_id_and_game[1].replace("\n", "").split(";")
        rounds_list = []
        for round in rounds:
            round = round.split(",")
            colour_list = []
            for entry in RGB:
                found = 0
                for colour in round:
                    if entry in colour:
                        colour_list.insert(RGB.index(entry),colour.replace(str(entry), "").replace(" ", ""))
                    else:
                        found += 1
                if found == len(round):
                    colour_list.insert(RGB.index(entry), "0")
            rounds_list.append(colour_list)
        games_list.append([game_id, rounds_list])
    return games_list