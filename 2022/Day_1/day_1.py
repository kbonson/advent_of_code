def main(infile):
    snack_bag = []
    calorie_totals = []
    with open(infile, "r", encoding="utf-8-sig") as fin:
        for line in fin:
            line = line.strip("\n")
            if line == "":
                calorie_totals.append(sum(snack_bag))
                snack_bag.clear()

            else:
                snack_bag.append(int(line))

    if len(snack_bag) > 1:
        calorie_totals.append(sum(snack_bag))

    calorie_totals.sort(reverse=True)

    most_calories = calorie_totals[0]
    second_most_calories = calorie_totals[1]
    third_most_calories = calorie_totals[2]
    print(f"Max number of calories: {most_calories}")
    total_of_top_three = sum([most_calories, second_most_calories, third_most_calories])
    print(f"Total from top 3: {total_of_top_three}")


if __name__ == "__main__":
    infile = "calories_list.txt"
    main(infile)
