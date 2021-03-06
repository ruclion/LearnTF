#coding=utf-8

import tensorflow as tf
import numpy as np

def readMyFileFormat(fileNameQueue):
    reader = tf.TextLineReader()
    key, value = reader.read(fileNameQueue)
    # print(tf.Session.run(key))
    # print('value:', value)
    record_defaults = [[1], [1], [1]]
    col1, col2, col3 = tf.decode_csv(value, record_defaults = record_defaults)
    # print(col1)
    features = tf.stack([col1, col2])
    label = col3
    return features, label

def inputPipeLine(fileNames = ["file0.csv", "file1.csv"], batchSize = 4, numEpochs = None):
    fileNameQueue = tf.train.string_input_producer(fileNames, num_epochs = numEpochs)
    example, label = readMyFileFormat(fileNameQueue)
    min_after_dequeue = 8
    capacity = min_after_dequeue + 3 * batchSize
    exampleBatch, labelBatch = tf.train.shuffle_batch([example, label], batch_size = batchSize, num_threads = 3,  capacity = capacity, min_after_dequeue = min_after_dequeue)
    return exampleBatch, labelBatch
# fileNameQueue = tf.train.string_input_producer(["file0.csv", "file1.csv"], num_epochs = None)
# readMyFileFormat(fileNameQueue)
featureBatch, labelBatch = inputPipeLine(["file0.csv", "file1.csv"], batchSize = 4)
with tf.Session() as sess:
    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

   # Retrieve a single instance:
    try:
        #while not coord.should_stop():
        while True:
            example, label = sess.run([featureBatch, labelBatch])
            print(example)
    except tf.errors.OutOfRangeError:
        print('Done reading')
    finally:
        coord.request_stop()

coord.join(threads)
sess.close()