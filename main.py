import numpy as np
import matplotlib.pyplot as plt

max_no_of_notification = 500


def set_lead_time(amount):
    lead_time = np.random.randn(amount)
    for i in range(lead_time.size):
        if lead_time[i] < 0:
            lead_time[i] *= -1
    return lead_time



