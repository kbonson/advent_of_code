def main(infile)
    calorie_totals = []
    snack_bag = []	
    data = File.readlines(infile).map(&:chomp)
    data.each {
        |line| 
        if line.eql? ""
            calorie_totals << snack_bag.sum
            snack_bag.clear()
        else
            snack_bag << line.to_i
        end	
    }
    if snack_bag.length > 1
        calorie_totals << snack_bag.sum
    end	
    sorted_calories = calorie_totals.sort()	
    most_calories = sorted_calories[-1]
    second_most_calories = sorted_calories[-2]
    third_most_calories = sorted_calories[-3]
    puts "Max number of calories: #{most_calories}"
    total_of_top_three = [most_calories, second_most_calories, third_most_calories].sum
    puts "Total from top 3: #{total_of_top_three}"    
end


infile = 'calories_list.txt'
main(infile)
