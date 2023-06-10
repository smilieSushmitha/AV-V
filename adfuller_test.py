import logging
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from multiprocessing import Pool
from datetime import datetime


start_time = datetime.now()
logging.basicConfig(filename='./adfuller_test.log', level=logging.INFO)

logging.info("start time : %s" % str(start_time))
logging.info("Reading data")


data = pd.read_csv('./all_and_classification.csv')  # load data set
data = data.drop('file_name', axis=1)
data = data.drop('run', axis=1)
data['forks'] = data['forks'].replace(['steady state'], 1)
data['forks'] = data['forks'].replace(['no steady state'], 0)
data = data.loc[data['forks'] == 1]
data = data.drop('forks', axis=1)

x_data = data.drop('steady_state_starts', axis=1)
y_data = data['steady_state_starts']
window_size = 500


def stationary_check(i):
    is_stationary = np.zeros(3000-window_size+1)
    for j in range(3000 - window_size + 1):
        # logging.info(f'i = {str(i)} ; j = {str(j)}')
        window = (x_data.iloc[[i], j:j + window_size]).squeeze()
        result = adfuller(window)
        p_value = result[1]
        if p_value < 0.05:
            is_stationary[j:j + window_size] = 1
    logging.info(f'i = {str(i)}')
    return list(is_stationary)


if __name__ == "__main__":

    processes = 2
    logging.info('utilizing %d cores\n' % processes)
    pool = Pool(processes)

    print(len(x_data))
    # Set the window size

    stationary =[]
    i = range(len(x_data))
    # Perform rolling ADF test
    rows = pool.map(stationary_check, i)

    df = pd.DataFrame(rows)
    print(df)

    df.to_csv('adfuller_test.csv', index=False)

    end_time = datetime.now()
    logging.info("end time : %s" % str(end_time))
    logging.info("total time taken : %s" % str(end_time - start_time))