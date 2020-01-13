import numpy as np

max_no_of_notification = 500
time = 1440


def set_lead_time(amount):
    lead_time = np.random.normal(90, 30, amount)
    for i in range(amount):
        lead_time[i] = round(lead_time[i], 2)
        if lead_time[i] < 0:
            lead_time[i] *= -1
    return lead_time


def set_priority(amount):
    return np.random.randint(1, 4, amount)


def collect_in_order(array):
    array = array[array[:, 3].argsort(kind='mergesort')]
    array = array[array[:, 2].argsort(kind='mergesort')]
    return array


def print_values_by_index(index, array):
    print('- no', array[index][0], '\ttime:', array[index][1], '\tpriority:', array[index][2], '\tquality rate:',
          array[index][3])


def main():
    lead_time = set_lead_time(max_no_of_notification)
    priority = set_priority(max_no_of_notification)
    time_left = time

    array, tasks_executed, index = [], [], []
    for i in range(max_no_of_notification):
        tasks_executed.append([0, 0])
        array.append([i + 1, lead_time[i], priority[i], round(lead_time[i] * priority[i], 2)])
    array, tasks_executed = np.array(array), np.array(tasks_executed)

    print('\nExample:')
    for i in range(10, 200, 60):
        print_values_by_index(i, array)
    print('\nTask matrix:\n', array)

    array = collect_in_order(array)
    for i in range(max_no_of_notification):
        tasks_executed[i][0] = array[i][0]
        tasks_executed[i][1] = 0

    print('\nTask sequence matrix:\n', array)

    for i in range(max_no_of_notification):
        if time_left > 0 and time_left > array[i][1]:
            time_left -= array[i][1]
            tasks_executed[i][1] = 1
            index.append(array[i][0])
        else:
            break

    print('\nDecision matrix:\n', tasks_executed[tasks_executed[:, 0].argsort(kind='mergesort')])
    print('\nSummary\n----------------------------------\nThe following tasks were completed:')
    index = sorted(index)
    for task in index:
        print(' - ', task)
    print('\nCompleted:', len(index),
          'tasks (', round(len(index) / max_no_of_notification, 2) * 100, '%)',
          '\nTime left:', round(time_left, 2), 'min')


if __name__ == "__main__":
    main()
