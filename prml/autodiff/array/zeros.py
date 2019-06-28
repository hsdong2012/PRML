import numpy as np

from prml.autodiff.core.array import Array
from prml.autodiff.core.config import config


def zeros(size):
    """
    return array filled with zeros

    Parameters
    ----------
    size : int, tuple, list
        size of array to return

    Returns
    -------
    Array
        Array filled with zeros
    """
    return Array(np.zeros(size, dtype=config.dtype))
