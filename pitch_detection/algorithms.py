import numpy as np


def compute_freq_from_zerocrossings(buffer: bytes, frames_per_second: int) -> float:
    """Compute the frequency based on zero-crossings.
    
    Parameters
    ----------
    buffer : bytes
        A sequence of bytes containing the audio.
    frames_per_second : int
        The frames per second.
        
    Returns
    -------
    float
        The estimated fundamental frequency.
    """
    chunk_data = np.frombuffer(buffer, np.int16)
    frames_per_buffer = chunk_data.size
    zc1 = (((chunk_data[:-1] < 0).astype(int) * (chunk_data[1:] > 0).astype(int)) > 0).astype(int)
    zc2 = (((chunk_data[:-1] > 0).astype(int) * (chunk_data[1:] < 0).astype(int)) > 0).astype(int)
    zc = zc1 + zc2
    num_periods = zc.sum() / 2
    freq = num_periods * frames_per_second / float(frames_per_buffer)
    return freq
