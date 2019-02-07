from progressbar import *
import time


progess = ProgressBar()
for i in progess(range(80)):
    time.sleep(0.01)

widgets = ['Loading:', Percentage(), '', Bar(),
            '', ETA(), '', FileTransferSpeed()]

pbar = ProgressBar(widgets=widgets, maxval=20000).start()

for i in range(20000):
    pbar.update(i)
    time.sleep(.005)
pbar.finish()
