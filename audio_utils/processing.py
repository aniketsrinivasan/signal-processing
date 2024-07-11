import wavfile
import numpy as np
from scipy.fft import fft
import os


def read_wav(file_path: str, verbose=True) -> tuple:
    """
    Consumes a path to a .wav file and returns a tuple containing the signal and sampling rate.

    :param file_path:   path to .wav file.
    :param verbose:     prints debugging information.
    :return:            tuple[np.ndarray, int]
    """
    if verbose:
        print(f"Reading .wav file from {file_path}...")
    # Reading information:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} was not found.")
    wav_data = wavfile.read(file_path)
    #   signal: (signal_length, 1)
    #   rate:   int
    signal, rate = wav_data[0] , wav_data[1]
    # Converting signal into an np.array and reshaping (squeezing):
    signal = np.array(signal)
    #   (signal_length, 1) ==> (signal_length)
    signal = np.squeeze(signal, axis=-1)

    if verbose:
        print(f"File read with following information: \n"
              f"    signal shape:   {signal.shape} \n"
              f"    sample rate:    {rate}")
    return signal, rate
