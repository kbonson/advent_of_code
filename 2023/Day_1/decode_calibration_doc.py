import re

# ---------- Part I ----------
def get_p1_calibration_value(line):
    first_digit, last_digit = re.findall("\d+", line)[0], re.findall("\d+", line)[-1]
    if (len(first_digit) > 1):
        first_digit = first_digit[0]

    if (len(last_digit) > 1):
        last_digit = last_digit[-1]

    return int(first_digit + last_digit)

# ---------- Part II ----------

word_numbers_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def format_chosen_values(string_value, first_target):
    try:
        int(string_value)
        if (len(string_value) > 1):
            if first_target:
                return string_value[0]

            return string_value[-1]
        
        return string_value

    except ValueError:
        formatted_value = word_numbers_map[string_value]

    return formatted_value

def get_p2_calibration_value(line):
    numbers_with_index = []
    all_numbers = re.findall("\d+", line)
    for target_number in list(set(all_numbers)):
        all_indices_of_number = [x.start() for x in re.finditer(target_number, line)]
        numbers_with_index = numbers_with_index + [(x, target_number) for x in all_indices_of_number]

    words_with_index = []
    all_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for target_word in all_words:
        if target_word in line:
            all_indices_of_word = [x.start() for x in re.finditer(target_word, line)]
            words_with_index = words_with_index + [(x, target_word) for x in all_indices_of_word]

    all_values_to_consider = numbers_with_index + words_with_index
    all_values_to_consider.sort()
    first_value_tuple, last_value_tuple = all_values_to_consider[0], all_values_to_consider[-1]

    formatted_first_value = format_chosen_values(first_value_tuple[1], True)
    formatted_last_value = format_chosen_values(last_value_tuple[1], False)

    return int(formatted_first_value + formatted_last_value)

# --------------------

def find_answer(input_file, get_calibration_value):
    total_value_sum = 0
    with open(input_file, 'r') as fin:
        for line in fin:
            current_calibration_value = get_calibration_value(line)
            total_value_sum += current_calibration_value
            print(f'Current line: {line}, Line Value: {current_calibration_value}, Total Sum: {total_value_sum}')

    return total_value_sum

calibration_document_name = "calibration_input.txt"
sum_of_calibration_values = find_answer(calibration_document_name, get_p2_calibration_value)
print(f'Answer: {sum_of_calibration_values}')
