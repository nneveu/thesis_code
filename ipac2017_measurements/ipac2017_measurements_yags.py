from utils import H5Reader
import h5py
import glob 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf


plotfn = 'weight7_YAGS.pdf'
pdf = matplotlib.backends.backend_pdf.PdfPages(plotfn) 

plt.rc('text', usetex=True)
plt.rc('font',family='serif')

yags  = glob.glob('/home/nicole/Documents/thesis_code/ipac2017_measurements/*w7.h5')
yags.sort(key=lambda f: int(filter(str.isdigit, f)))
yags.append(yags.pop(1)) #putting CTR1 at back of file

#fn = '/home/nicole/Documents/thesis_code/data/optLinac_weight0.stat'
point = 'Optimized Mostly Emittance, w7:\n' 
for fn in yags: 
    fig = plt.figure()
    legend = (fn.split('_')[2]).split('/')[1]
    #print legend
    #parser = H5Reader(fn)                                                                 
    #plt.plot(x,ymm, label=legend)
    plt.grid('on')
    hf = h5py.File(fn, 'r') 
    x  = np.asarray(hf.get('/Step#0'+'/x' ))*10.0**3.0 
    y  = np.asarray(hf.get('/Step#0'+'/y'))*10.0**3.0  
    plt.hist2d(x, y, bins = 200, range=[[-30.0,30.0], [-30.0,30.0]], cmin=1) 
    plt.colorbar()
    plt.xlabel("X [mm]")
    plt.ylabel("Y [mm]")
    plt.title(point+legend)
    pdf.savefig( fig, bbox_inches='tight', dpi=900 )

pdf.close()
