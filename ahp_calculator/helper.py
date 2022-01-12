import pandas as pd
import numpy as np
import os
from .constants import random_index

from importlib import resources
import io


def total(matrix, num_of_params):
    '''total function sums the column of matrix and returns a 1d-array

    Args:
    matrix: It is the pairwise comparison matrix after taking user input
    num_of_params: Number of factors taken for comparison'''
    tot = np.full((num_of_params), 0, dtype=float)
    for i in range(num_of_params):
        for j in range(num_of_params):
            tot[i] = tot[i] + matrix[j, i]
    return(tot)


def normalization(sum_of_column, matrix, num_of_params):
    ''''normalization function computes the matrix with ouput from total function and returns matrix

    Args:
    sum_of_column: It is the sum of each column of pariwise comparison matrix and also a output from total function
    matrix: It is the pariwise comparison matrix after taking user input
    num_of_params: Number of factors taken for comparison'''
    norm = np.full((num_of_params, num_of_params), 1, dtype=float)
    for i in range(num_of_params):
        for j in range(num_of_params):
            norm[i, j] = matrix[j, i]/sum_of_column[i]
    norm_t = norm.transpose()
    return (norm_t)


def weight(normalized_matrix, num_of_params):
    '''weight function computes the weight of each factor

    Args:
    normalized_matrix: It is the matrix from normalization function which has normalized value computed from sum of column
    num_of_params: Number of factors taken for comparison'''
    li = []
    for i in range(num_of_params):
        wt = np.sum(normalized_matrix[[i]])/num_of_params
        li.append(round(wt, 3))
    return(li)


def consistency_check(total, weight, num_of_params):
    '''consistency_check function checks the set of judgements to determine their reliability

    total: It is the sum of each column of pariwise comparison matrix and also a output from total function
    weight: Weight of each factors derived from the weight function
    num_of_params: Number of factors taken for comparison '''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Lambda value
    lmda = 0
    for i in range(num_of_params):
        lmda = lmda + total[i] * weight[i]

    # Consistency Index
    CI = (lmda-num_of_params)/(num_of_params-1)

    # Random Index
    #df = pd.read_csv(os.path.join(dir_path, 'random_index.csv'))
    # with resources.open_binary(os.path.join(dir_path, 'random_index.csv')) as fp:
    #     df = fp.read()
    # df = pd.read_csv(io.Bytes)
    for x in random_index:
        if (x==str(num_of_params)):
            RI = random_index[x]

    # Consistency Ratio
    CR = CI/RI
    to_return = {
        "Consistency Index: ": CI,
        "Random Index: ": RI,
        "Consistency Ratio: ": CR
    }
    if(CR < 0.1):
        to_return["Consistency: "] = True
    else:
        to_return["Consistency: "] = False

    return (to_return)

#     "The data is consistent"
# "The data is inconsistent. Iterate the process by changing comparison value"
