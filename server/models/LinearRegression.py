import tensorflow as tf
import time


class Model(object):

    def __init__(self, x_train, y_train, learning_rate):
        self.x_train = x_train
        self.y_train = y_train

        m = len(x_train[0])
        n = len(y_train[0])

        self.x = tf.placeholder(tf.float32, [None, m])
        self.y = tf.placeholder(tf.float32, [None, n])

        self.w = tf.get_variable("Weight", [m, n], initializer=tf.random_normal_initializer())
        self.b = tf.get_variable("bias", [], initializer=tf.zeros_initializer())
        y_p = tf.add(tf.matmul(self.x, self.w), self.b)

        self.loss = tf.reduce_mean(tf.square(tf.subtract(y_p, self.y)))
        self.train = tf.train.GradientDescentOptimizer(learning_rate).minimize(self.loss)
        self.session = None

    def run(self):
        for i in range(1000):
            self.session.run(self.train, feed_dict={
                self.x: self.x_train,
                self.y: self.y_train
            })

    def start(self):
        print(
            f"[{time.asctime()}] "
            "LinearRegression > Model > start > {Starting model}"
        )

        init = tf.global_variables_initializer()
        with tf.Session() as self.session:
            self.session.run(init)
            self.run()

            return [
                self.session.run(self.w),
                self.session.run(self.b)
            ]
