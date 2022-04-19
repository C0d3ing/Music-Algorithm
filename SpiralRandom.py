from main import c, i, r
from FractalEquation import mandelbrot, MAX_ITER, MandelDataBuffer
import numpy as np

J = complex(0, 1)
k=0.1
RandomArray = []

class Spiralizer:
    def __init__(self, seed):
        self.seed = seed

    def InitialSpiral(self):
        for x in np.range(0.2, 10, 0.01):
            s = J ** x + k*x + k*x*J + self.seed
            RandomArray.append(s)

#Complex number is assigned as a seed value and the equation iterates through the random spiral points

SP = Spiralizer(c)

SP.InitialSpiral()

#If the point is part of the set the iteration count and max iter must be the same so it must equal 1 when divided

SetData = []

for y in RandomArray:
    m = mandelbrot(y)/MAX_ITER
    if m == 1:
        SetData.append(1)
    else:
        SetData.append(0)

FinalInsertList = []

for g in range(0,MAX_ITER):
    if SetData[g]=1:
        FinalInsertList.append(RandomArray[g])

    else:
        print("No Data Produced (Step: Spiralizer Final List)")

PreInterpolationlist=[]

for v in range(0,MAX_ITER):
    Q=mandelbrot(FinalInsertList[v]
    NoteList = np.array(np.mat(MandelDataBuffer))
    PreInterpolationlist.append(NoteList)

