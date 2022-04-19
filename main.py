import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from SpiralRandom import RandomArray

r = input("Enter the real component of a complex number on the Mandelbrot:")
i = input("Enter the imaginary component of the same complex number on the Mandelbrot (number only):")

r = float(r)
i = float(i)

c = complex(r,i)

# Complex number is sent to SpiralRandom.py to create a randomized Tensor of points

# Tensor is sent to Interpolate.py to be converted into sinusoidal wave

print(c)