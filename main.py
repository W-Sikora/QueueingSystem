import numpy as np
import matplotlib.pyplot as plt

max_no_of_notification = 500
time = 1440


def set_lead_time(amount):
    lead_time = np.random.randn(amount)
    for i in range(lead_time.size):
        if lead_time[i] < 0:
            lead_time[i] *= -1
        lead_time[i] *= 60
        lead_time[i] = round(lead_time[i], 2)
    return lead_time


def set_priority(amount):
    return np.random.randint(1, 5, amount)


def print_values_by_index(index, array):
    print('no', array[index][0], '\ttime:', array[index][1], 'priority:', array[index][2])


def main():
    lead_time = set_lead_time(max_no_of_notification)
    priority = set_priority(max_no_of_notification)
    array = []
    for i in range(max_no_of_notification):
        array.append([i + 1, lead_time[i], priority[i]])
    array = np.array(array)

    print('\nExample:')
    print_values_by_index(0, array)

    print(array)


if __name__ == "__main__":
    main()
