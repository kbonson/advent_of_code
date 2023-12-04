
initial_bag_load = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# ---------- Part I ----------
def assess_game_possibility(game_data):
    individual_draws = game_data.split(';')
    for draw in individual_draws:
        cube_counts_per_draw = draw.split(',')
        for cube in cube_counts_per_draw:
            [number, color] = cube.split()
            if int(number) > initial_bag_load[color]:
                return False

    return True

def solve_part_1(infile):
    total_value_sum = 0
    with open(infile, 'r') as fin:
        for line in fin:
            [game_id, game_details] = line.split(":")
            [_, game_id_no] = game_id.split()
            game_is_possible = assess_game_possibility(game_details)
            if game_is_possible:
                total_value_sum += int(game_id_no)

            # print(f'Current line: {line}, Game ID: {game_id_no}, Is Possible: {game_is_possible}')

    return total_value_sum

# ---------- Part II ----------

def get_draw_totals(draw_data):
    totals = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    cube_counts_per_draw = draw_data.split(',')
    for cube in cube_counts_per_draw:
        [number, color] = cube.split()
        totals[color] = int(number)

    return (totals['red'], totals['green'], totals['blue'])


def assess_game_power(game_data):
    individual_draws = game_data.split(';')
    # totals always given in order (red, green, blue)
    draw_totals = [get_draw_totals(x) for x in individual_draws]
    red_required = max([red_draw_total for red_draw_total, _, _ in draw_totals])
    green_required = max(green_draw_total for _, green_draw_total, _ in draw_totals)
    blue_required = max(blue_draw_total for _, _, blue_draw_total in draw_totals)
    print(f'red max: {red_required}, green max: {green_required}, blue max: {blue_required}')

    game_power = red_required * green_required * blue_required
        
    return game_power


def solve_part_2(infile):
    total_value_sum = 0
    with open(infile, 'r') as fin:
        for line in fin:
            [_, game_details] = line.split(":")
            game_power = assess_game_power(game_details)
            total_value_sum += int(game_power)
            # print(f'Current line: {line}, Game Power: {game_power}, Current Total: {total_value_sum}')

    return total_value_sum

game_history_doc = "game_history.txt"
answer = solve_part_2(game_history_doc)
print(f'Answer: {answer}')