from numpy import asarray
from math import log10, sqrt
import cv2
import numpy as np
import time
from skimage.feature import greycomatrix
import os


def matrix2array(data):  # data wujud matriks
    array = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data[i][j])):
                # print(data3[i][j][k])
                array.append(data[i][j][k])
    # W, H, dimensi array
    return array, len(data), len(data[i]), len(data[i][j])


def dec2asci(array):
    for l in range(len(array)):
        array[l] = chr(array[l])
    return array


def asci2dec(array):
    for l in range(len(array)):
        array[l] = chr(array[l])
    return array


def fpb(x, y):  # gcd
    while(y):
        x, y = y, x % y
    return x


def isPrime(n):
    n = int(n)
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


def private(e, m):
    return pow(e, -1, m)


def join2(num, num2):
    bin = np.binary_repr(num, width=8)
    bin2 = np.binary_repr(num2, width=8)
    array = [bin, bin2]
    append = (''.join(array))
    append = int(append, 2)
    return append


def doublerow(array):
    a = len(array)
    for i in range(a):
        array.append(array[i])
    # array = array + array2
    return array


def RSA_Enkrip(l, p, q, e):
    # p = 71
    # q = 31
    # e = 1139
    n = p*q
    m = (p-1)*(q-1)
    private_key = private(e, m)
    for i in range(len(l)):
        l[i] = pow(l[i], e) % n

    return l, private_key, n


def RSA_Dekrip(l, d, n):
    for i in range(len(l)):
        l[i] = pow(l[i], d) % n
    return l


def ch2asc(l):
    arr = [ord(c)for c in l]
    return arr


def asc2ch(l):
    arr = ''.join(chr(i)for i in l)
    # arr = [chr(i)for i in l]
    return arr


def uint82Int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr
