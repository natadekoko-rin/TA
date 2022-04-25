from playfair import *
from pengurutanArray import *
from rsa import *
import time
import cv2
import numpy as np
import os
from skimage import data
from skimage.measure import shannon_entropy


def int2Uint8(arr):
    for i in range(len(arr)):
        arr[i] = np.uint8(arr[i])
    return arr


def uint82Int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


def splitNum(num):  # mengsplit bilangan menjadi 2 dengan operasi biner
    bi = np.binary_repr(num, width=16)
    # print("==="+bi)
    chunks = [bi[i:i+8] for i in range(0, len(bi), 8)]
    # print(chunks)
    a = int(chunks[0], 2)
    b = int(chunks[1], 2)
    return a, b


def joinNum(a, b):  # menggabungkan 2 buah bilangan melalui operasi biner
    bin = np.binary_repr(a, width=8)
    bin2 = np.binary_repr(b, width=8)
    array = [bin, bin2]
    append = (''.join(array))
    append = int(append, 2)
    return append


def splitArr2(arr1):  # split msb & lsb
    arr2 = []
    for i in range(len(arr1)):
        a, b = splitNum(arr1[i])
        arr2.append(np.uint8(a))
        arr2.append(np.uint8(b))
    return arr2


def concatArr2(arr1):  # penggabungan msb & lsb
    arr2 = []
    i = 0
    while i != int(len(arr1)):
        a = joinNum(arr1[i], arr1[i+1])
        arr2.append(a)
        i += 2
    return arr2


def joinNum(a, b):  # menggabungkan 2 buah bilangan melalui operasi biner
    bin = np.binary_repr(a, width=8)
    bin2 = np.binary_repr(b, width=8)
    array = [bin, bin2]
    append = (''.join(array))
    append = int(append, 2)
    return append


def NC(file1, file2):
    imgA = cv2.imread(file1)
    imgB = cv2.imread(file2)

    rows, cols, a = imgA.shape
    print(rows, cols, a)
    sqrAsum = sqrAsum2 = 0
    productsum = 0

    a = np.mean(imgA, axis=tuple(range(imgA.ndim-1)))
    b = np.mean(imgB, axis=tuple(range(imgB.ndim-1)))
    for i in range(rows):
        for j in range(cols):
            productsum = productsum+((imgA[i, j]-a)*(imgB[i, j]-b))
            sqrAsum = sqrAsum+(((imgA[i, j]-a))**2)
            sqrAsum2 = sqrAsum2+(((imgB[i, j]-b))**2)

    sqrAsum = np.sqrt(sqrAsum)*np.sqrt(sqrAsum2)
    nc = productsum/sqrAsum
    nc = (nc[0]+nc[1]+nc[2])/3
    return nc


def Entropy(file):
    image = cv2.imread(file)
    return shannon_entropy(image)


def finalEncmix(file, key, p, q, e, rename):  # dengan rename
    filePath = os.path.split(file)
    start_time = time.time()
    matrix = pengurutanArrayP(key, (p*q))
    data = cv2.imread(file)
    ar, hi, wi, di = matrix2array(data)
    ar = uint82Int(ar)
    enc1 = playfairEnc(ar, matrix)
    enc2, d, n = RSA_Enkrip(enc1, p, q, e)
    enc2 = splitArr2(enc2)
    enc2 = int2Uint8(enc2)
    finalEnc = np.array(enc2)
    finalEnc = finalEnc.reshape(hi*2, wi, di)
    encP = int2Uint8(enc1)
    finalEncP = np.array(encP)
    finalEncP = finalEncP.reshape(hi, wi, di)
    filePathF = filePath[0]+"/"+rename+".png"
    filePathFP = filePath[0]+"/"+rename+"_P.png"
    cv2.imwrite(filePathF, finalEnc)
    cv2.imwrite(filePathFP, finalEncP)

    return d, n, (time.time() - start_time), filePathF


def finalDecmix(file, key, d, n, rename):  # dengan rename
    filePath = os.path.split(file)
    start_time = time.time()
    matrix = pengurutanArrayP(key, n)
    data = cv2.imread(file)
    ar, hi, wi, di = matrix2array(data)
    ar = uint82Int(ar)
    dec1 = concatArr2(ar)
    dec1 = RSA_Dekrip(dec1, d, n)
    dec2 = playfairDec(dec1, matrix)
    dec2 = int2Uint8(dec2)
    finalDec = np.array(dec2)
    finalDec = finalDec.reshape(int(hi/2), wi, di)

    filePathF = filePath[0]+"/"+rename+".png"
    cv2.imwrite(filePathF, finalDec)
    return (time.time() - start_time), filePathF
