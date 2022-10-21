#List definition

list = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

print(f'This is the list: {list}')

# Print the biggest element

print('This is the biggest number:')
print(max(list))

# Print the smallest element

print('This is the smallest number:')
print(min(list))

# Print only even numbers

print('These are the even numbers in the list:')

even = []

for number in list:
    position = 0    
    if number % 2 == 0:
        even.append(number)

print (even)

# Print the number of times the first element shows up on the list

print('This is the amount of times the first item of this list appears throughout the list:')

amount_first_item = 0

for number in list:
    if number == list[0]:
        amount_first_item += 1

print(amount_first_item)

# Print the list's average

total_list_sum = 0
list_average = 0

print('This is the list\'s average: ')

for number in list:
    total_list_sum += number

list_average = total_list_sum / len(list)

print(list_average)

# Print the negative numbers sum

print('This is the sum of all negative numbers in the list: ')

negative_numbers_sum = 0

for number in list:
    if number < 0:
        negative_numbers_sum += number

print(negative_numbers_sum)
