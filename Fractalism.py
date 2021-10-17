import math
import time


rem = []


class Fractalism () :
    def __init__ (self, scr_x, scr_y, zoom, x, y, fractal, num_of_iter) :
        self.scr_x = scr_x
        self.scr_y = scr_y
        self.zoom = zoom
        self.pos_x = x
        self.pos_y = y
        self.num_of_iterations = num_of_iter
        self.const = (0 + 0j)
        self.fractal = "Mandelbrot Set"
        self.formules = {
            "Mandelbrot Set" : "Z**2 + M",
            "Julia Set" : "Z**2 + J"
        }
        if fractal == "Mandelbrot Set" :
            self.fractal = fractal
        elif fractal[0] == "Julia Set" :
            self.fractal = fractal[0]
            self.const = fractal[1]
        for i in range(int(self.scr_x)):
            rem.append([])
            for ii in range(int(self.scr_y)):
                rem[i].append(0)


    def full_redraw (self, type) :
        t = time.time()
        global rem
        for i in range (int(self.scr_x)) :
            for ii in range(int(self.scr_y)) :
                rem[i][ii] = 0
        if type == "Full in one" :
            for i in range (int(self.scr_x)) :
                for ii in range (int(self.scr_y)) :
                    global Z, iii
                    Z = complex (
                        (i - round(self.scr_x / 2)) / self.zoom + self.pos_x,
                        (ii - round(self.scr_y / 2)) / self.zoom + self.pos_y
                    )
                    M = Z
                    for iii in range(self.num_of_iterations) :
                        if self.fractal == "Mandelbrot Set" :
                            Zcopy = Z**2 + M
                        if self.fractal == "Julia Set" :
                            Zcopy = Z**2 + self.const
                        if math.dist((Zcopy.real, Zcopy.imag), (0, 0)) > 2 :
                            break
                        Z = Zcopy
                    if iii == self.num_of_iterations :
                        iii = 30
                    rem[i][ii] = iii
        self.time = time.time() - t
        return rem


    def pixel (self, x, y) :
        global Z_
        Z_ = complex(
            (x - round(self.scr_x / 2)) / self.zoom + self.pos_x,
            (y - round(self.scr_y / 2)) / self.zoom + self.pos_y
        )
        M = Z_
        for iii in range(self.num_of_iterations):
            if self.fractal == "Mandelbrot Set":
                Zcopy = Z_ ** 2 + M
            if self.fractal == "Julia Set":
                Zcopy = Z_ ** 2 + self.const
            if math.dist((Zcopy.real, Zcopy.imag), (0, 0)) > 2:
                break
            Z_ = Zcopy
        if iii == self.num_of_iterations - 1:
            iii = 30
        return iii