from scipy.io import wavfile
from re import sub

import os
import time

DATA = {}


def pretreatment(wav_file, array2_output):  # for api server
    print(
        f"[{time.asctime()}] "
        "control > pretreatment > {Converting value}"
    )

    _, array1_input = wavfile.read(wav_file)

    os.remove(wav_file)

    n = int(len(array1_input) / len(array2_output))

    return (
        [[array1_input[i][0]/1000] for i in range(0, len(array1_input), n+1)],
        [[i] for i in array2_output]
    )


class Data(object):

    def __init__(self):
        self.link = sub("([^/\.]+\.[^/\.]+)", "data.pydat", os.path.realpath(__file__))

    def reload(self):
        global DATA

        with open(self.link) as file:
            DATA = eval(file.read())

    def save(self):
        with open(self.link, 'w') as file:
            file.write((str(DATA)))


Data().reload()


def check_id(i):  # for api server
    return i in DATA.keys()


class Controller(object):

    def __init__(self):
        self.key = None

    def insert_new_data(self, array):  # for api server
        print(
            f"[{time.asctime()}] "
            "control > Controller > {Inserting data from server}"
        )

        global DATA
        self.__check_and_create_status_key()

        if self.key not in DATA.keys():
            DATA[self.key] = [array[0], array[1], 0, 0]
        else:
            DATA[self.key][0] = DATA[self.key][0] + array[0]
            DATA[self.key][1] = DATA[self.key][1] + array[1]

        self.__not_yet()
        Data().save()

    def insert_w_b(self, weight, bias):  # for prediction model
        print(
            f"[{time.asctime()}] "
            "control > Controller > {Inserting data from model}"
        )

        self.__check_and_create_status_key()

        DATA[self.key][2] = weight
        DATA[self.key][3] = bias

        self.__yet()
        Data().save()

    def get_value(self):  # for api server
        print(
            f"[{time.asctime()}] "
            "control > Controller > {Server getting data}"
        )

        Data().reload()

        try:
            return [
                DATA[self.key][2] != 0,
                DATA[self.key][2],
                DATA[self.key][3]
            ]
        except KeyError:
            return [False]

    def __check_and_create_status_key(self):  # for prediction model check updated weight and bias
        if 'status' not in DATA.keys():
            DATA['status'] = {0: []}
            DATA['status'][0].append(self.key)

            Data().save()

    def __not_yet(self):
        if self.key in DATA['status'][0]:
            return None

        DATA['status'][0].append(self.key)
        return None

    def __yet(self):
        if self.key not in DATA['status'][0]:
            return None

        DATA['status'][0].pop(
            DATA['status'][0].index(self.key)
        )
