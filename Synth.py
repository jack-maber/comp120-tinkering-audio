import wave
import math
import struct

samplerate = float(44100) # Hz
SampleLength = 44100 * 4 # seconds
frequency = 440 # Hz
amplitude = 1
samples = frequency*samplerate
BitDepth = 32767

Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('noise2.wav','w')
noise_out.setparams(Soundtuple)

values = []

for i in range(0, Soundtuple[3]):
    value = math.sin(2.0 * math.pi * frequency * (i/Soundtuple[2])) * (amplitude * BitDepth)
    #print value
    packaged_value = struct.pack('h', value)

    for j in xrange(0,Soundtuple[0]):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.writeframes(value_str)

noise_out.close()

