import doctest
import numpy as np


def convert_freq_to_tone_index(freq: float) -> int:
    """Converts a frequency to a tone index.
    
    Parameters
    ----------
    freq : float
        The frequency in Hertz (Hz).
        
    Returns
    -------
    int
        The tone index.
        
    Examples
    --------
    >>> convert_freq_to_tone_index(440.0)
    49
    """
    return int(12 * np.log(freq / 440) / np.log(2) + 49)


def convert_tone_index_to_tone(index: int) -> str:
    """This method takes a tone index and converts it to a tone.
    
    Parameters
    ----------
    index : int
        The tone index.
        
    Returns
    -------
    str
        The tone.
        
    Examples
    --------
    >>> convert_tone_index_to_tone(49)
    'A'
    """
    normed_index = int(np.floor(index)) % 12
    return ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B'][normed_index - 4]


def convert_freq_to_tone(freq: float) -> str:
    """Converts a frequency to a tone.
    
    Parameters
    ----------
    freq : float
        The frequency to convert to a tone.
        
    Returns
    -------
    str
        The tone.
    
    Examples
    --------
    >>> convert_freq_to_tone(440.0)
    'A'
    """
    tone_index = convert_freq_to_tone_index(freq)
    return convert_tone_index_to_tone(tone_index)


if __name__ == '__main__':
    doctest.testmod()
