from ctypes import *
from contextlib import contextmanager
import pyaudio
import wave

class Microphone(object):
    def __init__(self):
        # error handling
        ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

        def py_error_handler(filename, line, function, err, fmt):
            pass

        c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

        @contextmanager
        def noalsaerr():
            asound = cdll.LoadLibrary('libasound.so')
            asound.snd_lib_error_set_handler(c_error_handler)
            yield
            asound.snd_lib_error_set_handler(None)

        # set values
        self.form_1 = pyaudio.paInt16 
        self.samp_rate = 48000
        self.chans = 1 
        self.dev_index = 2        
        self.chunk = 2048
        self.bits_per_sample = 16
        
        # create the wav header
        self.wav_header = self.get_header(self.samp_rate, self.bits_per_sample, self.chans)
        
        # create the pyaudio instance
        with noalsaerr():
            self.audio = pyaudio.PyAudio()
        
        # create the stream
        self.stream = self.audio.open(format = self.form_1,
                                 rate = self.samp_rate,
                                 channels = self.chans,
                                 input_device_index = self.dev_index,
                                 input = True,
                                 frames_per_buffer = self.chunk)

    def __del__(self):
        if self.stream:
            self.stream.close()
        if self.audio:
            self.audio.terminate()
    
    # get a chunk of audio
    def get_audio(self):
        return self.stream.read(self.chunk, exception_on_overflow = False)
    
    # create the header
    def get_header(self, sampleRate, bitsPerSample, channels):
        datasize = 2000*10**6
        o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
        o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
        o += bytes("WAVE",'ascii')                                              # (4byte) File type
        o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
        o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
        o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
        o += (channels).to_bytes(2,'little')                                    # (2byte)
        o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
        o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
        o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
        o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
        o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
        o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
        return o
    
    # get the wav header
    def get_wav_header(self):
        return self.wav_header
        
