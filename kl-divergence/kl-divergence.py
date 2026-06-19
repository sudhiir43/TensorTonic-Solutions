import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    kl = 0 

    for P,Q in zip(p,q):
        kl += P*np.log(P/Q)

    return kl