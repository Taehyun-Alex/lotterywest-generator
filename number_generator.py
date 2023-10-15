import random

from data.wed_results import wed_results_list
from data.sat_results import sat_results_list

num_count_dict = {}
total_count = 0
num_of_pull = 10
num_of_random_games = 3
num_of_random_numbers = 3
powerball = 6
num_of_loop = 12
target_list = []

# This part ask for the day
answer = input("Choose between Wednesday and Saturday lotto\n=> ")
if answer == "Wednesday":
    for week_result in wed_results_list:
        for num in week_result:
            total_count += 1
            if num in num_count_dict:
                num_count_dict[num] += 1
            else:
                num_count_dict[num] = 1
elif answer == "Saturday":
    for week_result in sat_results_list:
        for num in week_result:
            total_count += 1
            if num in num_count_dict:
                num_count_dict[num] += 1
            else:
                num_count_dict[num] = 1

# ask for previous result
for _ in range(powerball):
    nums = input("type in the previous results\n=> ")
    target_list.append(int(nums))
print(target_list)

for num, count in sorted(num_count_dict.items()):
    percentage = (count / total_count * 100)
    # print(f"{num} : {round(percentage, 2)}")


sorted_items = sorted(num_count_dict.items(), key=lambda x: x[1], reverse=True)
top_items = sorted_items[:num_of_pull]

common_list = [item[0] for item in sorted(top_items, key=lambda x: x[0])]
print(f"The common numbers are {common_list}")

for i in range(num_of_loop):
    random_numbers = []
    selected_items = random.sample(common_list, num_of_random_numbers)
    random_numbers.extend(selected_items)
    while len(random_numbers) < powerball:
        random_num = random.randint(1, 45)
        if random_num not in common_list and random_num not in random_numbers:
            random_numbers.append(random_num)
    sorted_random_numbers = sorted(random_numbers)

    print(f"Generated List {i + 1}: {sorted_random_numbers}")

    common_elements = set(sorted_random_numbers).intersection(target_list)
    if len(common_elements) >= 4:
        print(f"Found a match with {len(common_elements)} common numbers at iteration {i + 1}.")
        break
# so far, it returns 20 lists of generated lotto.
# how do I match it with the result?





#Todo: make sure they don't have duplicate each games.

#Todo: run the test to see how many games it takes to get more than 4 numbers correct.