MAX_ITER = 80

Mandel

#i for input

MandelDataBuffer = []

def mandelbrot(i):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + i
        MandelDataBuffer.append(z)
        n += 1
    return n