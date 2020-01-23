from datas import control as cl
from models.LinearRegression import Model
from re import sub

import api
import os
import tensorflow.compat.v1 as tf
import threading
import time

tf.disable_v2_behavior()

PWD = sub("([^/\.]+\.[^/\.]+)", "", os.path.realpath(__file__))


class Prediction(Model):

    def __init__(self, x_train, y_train, learning_rate):
        super().__init__(x_train, y_train, learning_rate)

    def run(self):
        for i in range(5000):
            self.session.run(
                self.train,
                feed_dict={
                    self.x: self.x_train,
                    self.y: self.y_train
                }
            )


def train():
    print(
        f"[{time.asctime()}] "
        "main > train > {Predicting value}"
    )

    cl.Data().reload()
    for i in cl.DATA['status'][0]:
        ctr = cl.Controller()
        ctr.key = i

        data_set = cl.DATA[i][:2]
        pred = Prediction(data_set[0], data_set[1], 0.3)

        temp = ctr.get_value()
        pred.w = tf.Variable([[temp[0]]], shape=(1,1), dtype=tf.float32)
        pred.b = tf.Variable(temp[1], shape=(), dtype=tf.float32)
        
        weight, bias = pred.start()
        print("weight and bias:", weight, bias)

        if str(bias) != "nan":
            ctr.insert_w_b(weight[0][0], bias)
        else:
            ctr.insert_w_b(1, 1)

        tf.reset_default_graph()


def main():
    threading.Thread(
        target=api.run_server, 
        args=()
    ).start()

    while True:
        train()
        time.sleep(10)


if __name__ == '__main__':
    main()
