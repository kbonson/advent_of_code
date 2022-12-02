

def main(infile):
	new_snack_collection = False
	snack_bag = []
	calorie_totals = []

	with open(infile, 'r', encoding='utf-8-sig') as fin:
		for line in fin:
			line = line.strip('\n')
			if line == '':
				collection_total = sum(snack_bag)
				calorie_totals.append(collection_total)
				snack_bag.clear()

			else:
				snack_bag.append(int(line))

	if len(snack_bag) > 1:
		collection_total = sum(snack_bag)
		calorie_totals.append(collection_total)


	calorie_totals.sort(reverse=True)

	most_calories = calorie_totals[0]
	second_most_calories = calorie_totals[1]
	third_most_calories = calorie_totals[2]

	total_of_top_three = sum([most_calories, second_most_calories, third_most_calories])
	print(f'Total from top 3: {total_of_top_three}')

if __name__=="__main__":
	infile = 'calories_list.csv'
	main(infile)
