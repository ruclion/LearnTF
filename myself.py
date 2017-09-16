#
#

'code mnist by myself'

__author__ = 'hjkruclion'

import tensorflow as tf
import numpy as np
import csv
import random

def cnnGraph():
    x = tf.placeholder(tf.float32, [None, 784])

    #resharp [-1, 784] => [-1, 28, 28, 1]
    x_img = tf.reshape(x, [-1, 28, 28, 1])

    #cov1 [-1, 28, 28, 1] => [-1, 28, 28, 32]
    w_cov1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32]))
    b_cov1 = tf.Variable(tf.truncated_normal([32]))
    x_cov1 = tf.nn.conv2d(x_img, w_cov1, [1, 1, 1, 1], padding='SAME') + b_cov1
    #pooling1 [-1, 28, 28, 32] => [-1, 14, 14, 32]
    x_pool1 = tf.nn.max_pool(x_cov1, [1, 2, 2, 1], [1, 2, 2, 1], padding='SAME')

    #cov2 [-1, 14, 14, 32] => [-1, 14, 14, 64]
    w_cov2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64]))
    b_cov2 = tf.Variable(tf.truncated_normal([64]))
    x_cov2 = tf.nn.conv2d(x_pool1, w_cov2, [1, 1, 1, 1], padding='SAME') + b_cov2
    #pooling2 [-1, 14, 14, 64] => [-1, 7, 7, 64]
    x_pool2 = tf.nn.max_pool(x_cov2, [1, 2, 2, 1], [1, 2, 2, 1], padding='SAME')

    #resharp [-1, 7, 7, 64] => [-1, 7 * 7 * 64]
    x_afcov = tf.reshape(x_pool2, [-1, 7 * 7 * 64])

    #all mult1 [-1, 7 * 7 * 64] => [-1, 1024]
    w1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1024]))
    b1 = tf.Variable(tf.truncated_normal([1024]))
    x_all1 = tf.matmul(x_afcov, w1) + b1

    #dropout [-1, 1024]
    keep_prob = tf.placeholder(tf.float32)
    x_drop = tf.nn.dropout(x_all1, keep_prob=keep_prob)

    #all mult2 [-1, 1024] => [-1, 10]
    w2 = tf.Variable(tf.truncated_normal([1024, 10]))
    b2 = tf.Variable(tf.truncated_normal([10]))
    x_all2 = tf.matmul(x_drop, w2) + b2

    return x, x_all2, keep_prob


def solve(inputData):
    trainData = inputData.train
    testData = inputData.test

    #def graph and get input and output
    x, x_all2, keep_prb = cnnGraph()

    #def opt and give label y_
    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=x_all2)
    cross_entropy = tf.reduce_mean(cross_entropy)
    train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        trainData_batch = [random.sample(trainData[0], 50),random.sample(trainData[1], 50)]
        loss, _ = sess.run([cross_entropy, train_step], feed_dict={x : trainData_batch[0], y_ : trainData_batch[1], keep_prb : 0.5})
        cmp = tf.equal(tf.arg_max(x_all2, 1), tf.arg_max(y_, 1))
        cmp = tf.cast(cmp, tf.float32)
        mean = tf.reduce_mean(cmp)
        trainData_batch = [random.sample(trainData[0], 50), random.sample(trainData[1], 50)]
        print('time:', i, 'accuracy:', sess.run(mean, feed_dict={x : trainData_batch[0], y_ : trainData_batch[1], keep_prb : 1.0}))


class Data(object):
    def __init__(self, _train, _test):
        self.train = _train
        self.test = _test


if __name__ == '__main__':
    train_label = []
    train_data = []
    with open("mnist_test.csv", "r") as csvFile:
        reader = csv.reader(csvFile)

        for item in reader:
            x = np.zeros([10], np.float32)
            x[int(item[0])] = 100.0
            train_label.append(x)
            train_data.append(list(map(float, item[1:])))
    # print(train_label[0], train_data[0], len(train_data[0]))
    tmp = [train_data, train_label]
    inputData = Data(tmp, tmp)
    inputData.train = tmp
    inputData.test = tmp
    solve(inputData=inputData)





