#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Price of wheat/kg and the average price of bread

wheat_and_bread = [[0.5, 5], [0.6, 5.5], [0.8, 6], [1.1, 6.8], [1.4, 7]]


def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        b_gradient += -(2 / N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / N) * x * (y - ((m_current * x) + b_current))

    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learning_rate)

    return [b, m]

gradient_descent_runner(wheat_and_bread, 1, 1, 0.01, 100)