def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    # ax**2 + bx + c
    #d/dx = 2ax + b

    for i in range(steps):
        x0 -= lr*(2*x0*a + b) 
    return x0 
        