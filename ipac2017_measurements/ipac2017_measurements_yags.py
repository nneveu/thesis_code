from utils import H5Reader
import h5py
import glob 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf


plotfn = 'easy_exp.pdf'
key = 'easy'
pdf = matplotlib.backends.backend_pdf.PdfPages(plotfn) 

plt.rc('text', usetex=True)
plt.rc('font',family='serif')
plt.rc('axes', axisbelow=True)

yags  = glob.glob('/home/nicole/Documents/thesis_code/ipac2017_measurements/*'+key+'*.h5')
yags.sort(key=lambda f: int(filter(str.isdigit, f)))
yags.append(yags.pop(0)) #putting CTR1 at back of file

#fn = '/home/nicole/Documents/thesis_code/data/optLinac_weight0.stat'
point = 'M=250, FWHM=1.5ps:\n' 
for fn in yags: 
    fig = plt.figure()
    plt.grid(True, zorder=0)
    legend = (fn.split('_')[2]).split('/')[1]
    #print legend
    #parser = H5Reader(fn)                                                                 
    #plt.plot(x,ymm, label=legend)
    hf = h5py.File(fn, 'r') 
    x  = np.asarray(hf.get('/Step#0'+'/x' ))*10.0**3.0 
    y  = np.asarray(hf.get('/Step#0'+'/y'))*10.0**3.0  
    plt.hist2d(x, y, bins = 200, range=[[-30.0,30.0], [-30.0,30.0]], cmin=1, zorder=3) 
    plt.colorbar()
    plt.xlabel("X [mm]")
    plt.ylabel("Y [mm]")
    plt.title(point+legend)
    pdf.savefig( fig, bbox_inches='tight', dpi=900 )

pdf.close()
