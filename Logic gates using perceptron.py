# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:40:22 2018

@author: LAB-I
"""

import numpy as np
from functools import reduce


def perceptron(weight, bias, x):
    model = np.add(np.dot(x, weight), bias)
    print('model: {}'.format(model))
    logit = 1/(1+np.exp(-model))
    print('Type: {}'.format(logit))
    return np.round(logit)

def compute(logictype, weightdict, dataset):
    weights = np.array([ weightdict[logictype][w] for w in list(weightdict[logictype].keys())[::-1]])
    output = np.array([ perceptron(weights, weightdict['bias'][logictype], val) for val in dataset])
    print(logictype)
    return logictype, output

def main():
    logic = {
        'logic_or': {
            'w0': -0.1,
            'w1': 0.7,
            'w2': 0.7
        },
        'bias': {
            'logic_or': -0.1,
        }
    }
    dataset = np.array([
        [0,0,0],
        [1,0,1],
        [1,1,0],
        [1,1,1]
    ])

    logic_or = compute('logic_or', logic, dataset)

    def template(dataset, name, data):
        # act = name[6:]
        print("Logic Function: {}".format(name[6:].upper()))
        print("X0\tX1\tX2\tY")
        toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, data)]
        for i in toPrint:
            print(i)

    gates = [logic_or]

    for i in gates:
        template(dataset, *i)

if __name__ == '__main__':
    main()