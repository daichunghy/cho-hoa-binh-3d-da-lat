import numpy as np
sr=16000
x=np.fromfile('yt1_16k.raw',dtype=np.float32)
print('samples',len(x),'dur_s',len(x)/sr)
# per 30s window: RMS dB + band energy shares via FFT
def bandshare(seg):
    w=np.hanning(len(seg)); X=np.abs(np.fft.rfft(seg*w))**2
    f=np.fft.rfftfreq(len(seg),1/sr)
    tot=X.sum()+1e-12
    def b(a,b2): return X[(f>=a)&(f<b2)].sum()/tot
    return b(80,250),b(250,800),b(800,2500),b(2500,6000),b(6000,8000)
W=30*sr
for i in range(0,len(x)-W+1,W):
    seg=x[i:i+W]; rms=np.sqrt((seg**2).mean()+1e-12)
    lo,mid,hi,sh,air=bandshare(seg)
    print(f'{i//sr:4d}s RMS {20*np.log10(rms):6.1f}dB  <250:{lo*100:4.0f}% 250-800:{mid*100:4.0f}% 0.8-2.5k:{hi*100:4.0f}% 2.5-6k:{sh*100:4.0f}% >6k:{air*100:4.0f}%')
# loudest 1s peaks (bike/pass-by candidates): max |x| per 5s
for i in range(0,len(x),5*sr):
    seg=x[i:i+5*sr]
    if len(seg)==0: continue
    pk=np.abs(seg).max()
    if pk>0.5: print(f'PEAK {i//sr:4d}s peak {pk:.2f}')
