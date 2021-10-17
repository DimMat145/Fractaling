from arcade import *
from arcade import key
import Fractalism as fr
import math
import time


screen_width = 800
screen_height = 400
r = 2
screen_title = "title"
d = 1
g = 1
Fract = fr.Fractalism(screen_width / 4 / d, screen_height / 4 / d, 10, 0, 0, ["Mandelbrot Set", (0 + 0.5j)], 30)


class Win (Window) :
    def __init__ (self, width, height, title) :
        super().__init__(width, height, title, resizable=True)


    def setup (self) :
        self.adding_of_iter = 1
        self.adding_of_const = 1
        self.render = Fract.full_redraw("Full in one")
        self.color_palette = [
            (9,   1,   47),
            (7,   3,   60),
            (4,   4,   73),
            (2,   5,   86),
            (0,   7,   100),
            (6,   28,  119),
            (12,  44,  138),
            (18,  63,  152),
            (24,  82,  177),
            (32,  103, 193),
            (57,  125, 209),
            (95,  152, 219),
            (134, 181, 229),
            (172, 208, 239),
            (211, 236, 248),
            (226, 235, 220),
            (241, 233, 191),
            (245, 216, 140),
            (248, 201, 95),
            (251, 185, 70),
            (255, 170, 35),
            (229, 154, 12),
            (204, 128, 0),
            (175, 107, 0),
            (153, 87,  0),
            (130, 66,  1),
            (106, 52,  3),
            (86,  40,  7),
            (66,  30,  15),
            (30, 15, 7),
            (0, 0, 0),
            (12, 4, 13),
            (25, 7, 26),
            (17, 4, 37)
        ]
        self.draw_line = 0
        self.zoom = 100
        self.ren = 16
        self.const = False


    def on_resize(self, width, height):
        global screen_width, screen_height

        width = self.width * r
        height = self.height * r

        super().on_resize(width * r, height * r)
        screen_width = width
        screen_height = height
        Fract.scr_x = int(screen_width / 16 * r / d)
        Fract.scr_y = int(screen_height / 16 * r / d)


    def on_draw (self) :
        h = screen_height * r
        t = 50 / (2 / r)
        w = 20 / (2 / r)
        s = r / 2
        draw_text(f"Zoom: {Fract.zoom}", w, h - 80 * s, (255, 255, 255), t)
        draw_text(f"Fractal Calculation Time: {Fract.time}", w, h - 160 * s, (255, 255, 255), t)
        draw_text(f"Iteration: {Fract.num_of_iterations}", w, h - 240 * s, (255, 255, 255), t)
        draw_text(f"Position: ({Fract.pos_x} + {Fract.pos_y}i)", w, h - 320 * s, (255, 255, 255), t)
        draw_text(f"Fractal: {Fract.fractal} - {Fract.formules[f'{Fract.fractal}']}", w, h - 400 * s,
                  (255, 255, 255), t)
        draw_text(f"Const: {Fract.const}", w, h - 480 * s, (255, 255, 255), t)


    def update (self, delta_time = 0.01) :
        t = time.time()
        for i in range(self.draw_line % int(Fract.scr_x), (self.draw_line + self.ren)):
            for ii in range(int(Fract.scr_y)):
                draw_point((i % Fract.scr_x) * 16 * d, ii * 16 * d,
                    self.color_palette[Fract.pixel(i % Fract.scr_x, ii) % 34], 16 * d)
        draw_rectangle_filled(((i + 2) % Fract.scr_x) * 16 * d, screen_height, 8 * d, screen_height * 2,
                              (255, 0, 0))
        self.draw_line = (self.draw_line + self.ren) % Fract.scr_x
        Fract.time = time.time() - t

    def on_key_press(self, symbol: int, modifiers: int):
        global d, g

        if symbol == key.EQUAL :
            self.zoom *= 1.25
        if symbol == key.MINUS :
            self.zoom /= 1.25

        if symbol == key.A :
            Fract.pos_x -= 1 / self.zoom * 10 * d
        if symbol == key.D :
            Fract.pos_x += 1 / self.zoom * 10 * d
        if symbol == key.W :
            Fract.pos_y += 1 / self.zoom * 10 * d
        if symbol == key.S :
            Fract.pos_y -= 1 / self.zoom * 10 * d

        if symbol == key.UP :
            Fract.num_of_iterations += 1
        if symbol == key.DOWN :
            Fract.num_of_iterations -= 1
        if symbol == key.LEFT :
            Fract.num_of_iterations -= 10
        if symbol == key.RIGHT :
            Fract.num_of_iterations += 10

        if symbol == key.R :
            self.adding_of_const /= 2
        if symbol == key.Y :
            self.adding_of_const *= 2

        if symbol == key.F :
            Fract.const -= self.adding_of_const
        if symbol == key.H :
            Fract.const += self.adding_of_const
        if symbol == key.T :
            Fract.const = complex(Fract.const.real, (Fract.const.imag + self.adding_of_const))
        if symbol == key.G :
            Fract.const = complex(Fract.const.real, (Fract.const.imag - self.adding_of_const))

        self.const = False

        if symbol == key.M :
            Fract.fractal = "Mandelbrot Set"
        if symbol == key.J :
            Fract.fractal = "Julia Set"
        if symbol == key.C :
            self.const = True


        if symbol == key.Z :
            d = 8
            g = 1
        if symbol == key.X :
            d = 4
            g = 0.888888
        if symbol == key.V :
            d = 2
            g = 0.7
        if symbol == key.B :
            d = 1
            g = 0.5
        if symbol == key.N :
            d = 0.5
            g = 0.125
        if symbol == key.COMMA :
            d = 0.25
            g = 0.125
        if symbol == key.PERIOD :
            d = 0.125
            g = 0.06325
        if symbol == key.SLASH :
            d = 0.06325
            g = 0.06325

        self.ren = round(8 * g)

        #def b () :
        #    self.render = Fract.full_redraw("Full in one")
        #a = lambda : b()
        #a()
        Fract.zoom = self.zoom / d

        Fract.scr_x = int(screen_width / 16 * r / d)
        Fract.scr_y = int(screen_height / 16 * r / d)


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.const :
            Fract.const = complex (
                    (round(x / r) - round(screen_width * r / 2)) / Fract.zoom + Fract.pos_x,
                    (round(y / r) - round(screen_height * r / 2)) / Fract.zoom + Fract.pos_y
                ) / 15

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.const = False


Win_ = Win(screen_width, screen_height, screen_title)
Win_.setup()
run()