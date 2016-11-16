import wave
import math
import struct

duration = 4 # seconds
samplerate = 44100 # Hz
samples = duration*samplerate
frequency = 200 # Hz

Soundtuple = (2, duration, samplerate, samples, 'NONE', 'Not compressed')
noise_out = wave.open('noise2.wav','w')
noise_out.setparams(Soundtuple)

values = []

for i in range(0, Soundtuple[3]):
    value = math.sin(samples*math.pi * frequency * (i/float(Soundtuple[1]))) * (frequency * samplerate)
    print value
    packaged_value = struct.pack('h', value)

    for j in xrange(0,Soundtuple[0]):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.writeframes(value_str)

noise_out.close()


