## Runge-Kutta method (4th order)
## Equations taken from here: https://en.wikipedia.org/wiki/Runge-Kutta_methods
## not tested yet

def k1(f, t_n, y_n, h):
    return f(t_n, y_n)

def k2(f, t_n, y_n, h, k1):
    t_n = t_n + h / 2
    y_n = y_n + (h / 2) * k1    
    return f(t_n, y_n)

def k3(f, t_n, y_n, h, k2):
    t_n = t_n + h / 2
    y_n = y_n + (h / 2) * k2
    return f(t_n, y_n)

def k4(f, t_n, y_n, h, k3):
    t_n = t_n + h
    y_n = y_n + h * k3
    return f(t_n, y_n)

def update_y(y_n, h, k1, k2, k3, k4):
    y_n = y_n + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_n

def update_t(t_n, h):
    return t_n + h


def solve_ode(f, y_0, t_0, h):
    y_n = y_0   
    t_n = t_0
    for n in range(10):
        k1 = k1(f, t_n, y_n, h)
        k2 = k1(f, t_n, y_n, h)
        k3 = k1(f, t_n, y_n, h)
        k4 = k1(f, t_n, y_n, h)

        # update y and t
        y_n = update_y(y_n, h, k1, k2, k3, k4)
        t_n = update_t(t_n, h)
    return y_n
        
