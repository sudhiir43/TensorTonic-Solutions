import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    entropy = 0
    keys = set(y)

    for key in keys:
        p = y.count(key)/len(y)
        entropy -= p*np.log2(p)
        # print(p, key)
    return float(entropy)