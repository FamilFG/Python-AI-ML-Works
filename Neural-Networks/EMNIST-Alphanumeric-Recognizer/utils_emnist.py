import struct
import numpy as np

def load_images(path):
    with open(path, "rb") as f:
        _, n, r, c = struct.unpack(">IIII", f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(n, r, c, 1)

def load_labels(path):
    with open(path, "rb") as f:
        _, n = struct.unpack(">II", f.read(8))
        return np.frombuffer(f.read(), dtype=np.uint8)

def fix_orientation(X):
    # EMNIST fix
    X = np.transpose(X, (0, 2, 1, 3))
    X = np.flip(X, axis=2)
    return X
