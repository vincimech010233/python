"""
You have been speeding on a motorway and a police car had to stop you. The policeman is a funny guy that likes to play games. Before issuing penalty charge notice he gives you a choice to change your penalty.

Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of the police car chasing you, the number of police cars involved, etc. So, your task is to combine the given numbers and make the penalty charge to be as small as possible.

For example, if you are given numbers [45, 30, 50, 1] your best choice is 1304550

Examples:
['45', '30', '50', '1'] => '1304550'
['100', '10', '1'] => '100101'
['32', '3'] => '323'
"""

def penalty(a_list):
    # Convert numbers to strings and sort in reverse lexicographical order
    sorted_numbers = sorted(map(str, a_list), key=lambda x: x + x[::-1])
    # Combine the sorted numbers into a string and return it
    return ''.join(sorted_numbers)

# Examples
list1 = [45, 30, 50, 1]
list2 = [100, 10, 1]
list3 = [32, 3]

result1 = penalty(list1)
result2 = penalty(list2)
result3 = penalty(list3)

print(result1)  # Should print '1304550'
print(result2)  # Should print '100101'
print(result3)  # Should print '323'
