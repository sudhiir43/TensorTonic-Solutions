import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    pos = np.arange(seq_len)[:, np.newaxis]
    dim = (d_model+1)//2
    cos_dim = d_model//2
    dims = np.arange(dim)[np.newaxis, :]

    angle_rates = 1/(np.power(base, (2*dims)/d_model))

    angles = pos*angle_rates

    pe = np.zeros((seq_len, d_model))

    pe[:, 0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:,:cos_dim])

    return pe