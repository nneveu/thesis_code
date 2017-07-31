from utils import SddsReader
import statPlots as pl
import glob 
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font',family='serif')

before = glob.glob('/home/nicole/Documents/thesis_code/data/ipac2017/grad1/*weight*.stat')
after  = glob.glob('/home/nicole/Documents/thesis_code/data/ipac2017/grad2/*weight*.stat')
#fn = '/home/nicole/Documents/thesis_code/data/optLinac_weight0.stat'
plotfn = 'beamsizes_weight0-10.pdf'

plt.axvline(x=3.1)
plt.axvline(x=6.377)
plt.axvline(x=8.76)
plt.axvline(x=11.477)
plt.axvline(x=14.848)

 
for fn in before: 
    legend = (fn.split('_')[2]).split('.')[0]
    #print legend
    parser = SddsReader(fn)                                                                                  
    #x = []
    x = parser.getColumn("s")    
    #y = []                                                                                                                                       
    y = parser.getColumn("rms_x")
                      
    ymm = [l*10**3 for l in y]
    plt.plot(x,ymm, label=legend)

for fn2 in after:
    legend2 = (fn2.split('_')[2]).split('.')[0] + ' grad 2'
    #print legend2
    parser = SddsReader(fn2)
    x = parser.getColumn("s")
    y = parser.getColumn("rms_x")
                      
    ymm = [l*10**3 for l in y]
    plt.plot(x,ymm, '.', markevery=800, label=legend2)

plt.legend(bbox_to_anchor=(1.5, 1.0))
plt.xlabel("Z [m]")                                                                                                               
plt.ylabel("xrms [mm]")                                                                                 
plt.title("Beam Sizes")
plt.savefig(plotfn, bbox_inches='tight', dpi=900)
#pl.opalStatPlot(x,y,legend,xlabel,ylabel,title,plotfn)
'''
y.append(parser.getColumn("rms_y"))                                                                                                           
y.append(parser.getColumn("rms_s"))                                                                                                             
ylegend = []                                                                                                                                      
ylegend.append("rmsx")                                                                                                                         
ylegend.append("rmsy")                                                                                                                    
ylegend.append("rmss")                                                                                                                   
xlabel = "s (m)"                                                                                                               
ylabel = "Beamsize (m)"                                                                                 
title  = "My Plot"
pl.opalStatPlot(x,y,ylegend,xlabel,ylabel,title,plotfn)
'''
