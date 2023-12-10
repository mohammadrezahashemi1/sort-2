import time
import random
import matplotlib.pyplot as plt

# Given data
data = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]


# Sorts a list of dictionaries based on 'First Name' and 'Last Name'.
def sort(data):
    sorted_data = sorted(data, key=lambda x: (x['First Name'], x['Last Name']))
    return sorted_data

# Testing the sort function
print(sort(data))

data_to_check = sort(data)


# Generates random data with the specified size.
def generate_random_data(size):
    first_names = ['Raj', 'Suraj', 'Karan', 'Jade', 'Kiran', 'Armaan', 'Jaya', 'Ingrid', 'Aahana', 'Kumar', 'Seth', 'Canary', 'Galore', 'Thakur']
    last_names = ['Nayyar', 'Sharma', 'Kumar', 'Canary', 'Thakur', 'Sharma', 'Kamla', 'Kumar', 'Sharma', 'Galore', 'Seth', 'Dadra', 'Maverick', 'Arora']

    data = [{'First Name': random.choice(first_names), 'Last Name': random.choice(last_names)} for _ in range(size)]
    return data

data_sizes = [20, 600, 1000]

# Record execution times for each data size
execution_times = []

for size in data_sizes:
    random_data = generate_random_data(size)
    start_time = time.time()
    sort(random_data)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plot the results
plt.plot(data_sizes, execution_times, marker='o')
plt.xlabel('Data Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.grid(True)
plt.show()

# Mohammadreza hashemi fard / محدرضا هاشمی فرد
