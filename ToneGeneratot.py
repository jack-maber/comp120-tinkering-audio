import wave
import struct


noise_out = wave.open('noise2.WAV', 'w')
noise_out.getparams()


#values = []

#for i in range(0, SAMPLE_LENGTH):
   # value = sin(
       # 2.0 * PI *
       # FREQUENCY *
        #( i / SAMPLE_RATE)
       # )*                  \
        #(VOLUME * BIT_DEPTH)

   # packaged_value =package(FORMAT, value)

   # for j in xrange(0, CHANNELS):
        #values.append(packaged_value)

#value_str = ''.join(values)
#noise_out.write(value_str)

#noise_out.close()


#clip = wave.open('noise2.WAV')
#frames = clip.getnframes()

#for i in range(0, frames):
       # soundinfo = clip.readframes(1)
       # clipstruct = struct.unpack("<h", soundinfo)
       # print(int(clipstruct[0]))