import wave
import struct
import math

noise_out = wave.open('noise2.wav', 'w')

SAMPLE_RATE = float(44100) # Hz
SAMPLE_LENGTH = 44100 * 4 # seconds
FREQUENCY = 440 # Hz
VOLUME = 1
samples = FREQUENCY*SAMPLE_RATE
BIT_DEPTH = 32767

Soundtuple = (1, 4, 44100, (44100*4), 'NONE', 'Not compressed')
noise_out.setparams(Soundtuple)

values = []

for i in range(0, SAMPLE_LENGTH):
   value = math.sin(
       2.0 *math.pi *
       FREQUENCY *
        ( i / SAMPLE_RATE)
       )*                  \
        (VOLUME * BIT_DEPTH)
   packaged_value = struct.pack('<h', value)
   for j in xrange(0, 1):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.writeframes(value_str)

noise_out.close()


clip = wave.open('noise2.WAV')
frames = clip.getnframes()

