from utils import H5Reader
import glob 
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font',family='serif')

yags  = glob.glob('/home/nicole/Documents/thesis_code/data/ipac2017/grad2/*w0*.stat')
#fn = '/home/nicole/Documents/thesis_code/data/optLinac_weight0.stat'
plotfn = 'weight0_YAGS.pdf'

 
for fn in yags: 
    legend = (fn.split('_')[2]).split('.')[0]
    #print legend
    parser = H5Reader(fn)                                                                 
    #plt.plot(x,ymm, label=legend)

plt.xlabel("X [mm]")                                                                                                               
plt.ylabel("Y [mm]")                                                                                 
plt.title("Beam Sizes")
plt.savefig(plotfn, bbox_inches='tight', dpi=900)
