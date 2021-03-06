from sys import path

path.append('../')
import configparser
import pandas as pd
import datetime
from sklearn.metrics import mean_squared_error
import math


def plt_encoding_error():
    # coding:utf-8
    import matplotlib
    # matplotlib.use('qt4agg')
    # 指定默认字体
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    # 解决负号'-'显示为方块的问题
    matplotlib.rcParams['axes.unicode_minus'] = False


def normal(feature, value, height=1):
    """
    Determine whether the value is normal or missing
    :param feature:
    :param value: feature's value
    :param height: 1 means over the value is abnormal, 0 means under the value is abnormal
    :return: if normal return 0, abnormal return 1, missing return -1
    """
    if math.isnan(feature):
        return -1
    elif (height == 1 and feature > value) or (height == 0 and feature < value):
        return 1
    else:
        return 0


def get_url():
    conf = configparser.ConfigParser()
    conf.read("./dia.conf")

    root_dir = conf.get("local", "data_dir")
    train_url = conf.get("local", "train_url")
    feature_url = conf.get("local", "feature_url")
    return root_dir, train_url, feature_url


def read_data():
    root_dir, train_url, feature_url = get_url()

    train = pd.read_csv(root_dir + 'd_train_20180102.csv', encoding='gb2312')
    test_A = pd.read_csv(root_dir + 'd_test_A_20180102.csv', encoding='gb2312')
    sample = pd.read_csv(root_dir + 'd_sample_20180102.csv', encoding='gb2312')
    return train, test_A, sample


def error(y_train, predict):
    result = mean_squared_error(y_train, predict) / 2
    print("1/2 Mean squared error: %.6f" % result)
    return result


def save(result, name):
    now = datetime.datetime.now()
    my_time = now.strftime('%m_%d_%H_%M')
    result.to_csv("result/" + name + '_' + my_time + '.csv', header=None, index=False, encoding="utf-8")


if __name__ == '__main__':
    pass