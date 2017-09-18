from utils import SddsReader
import statPlots as pl
import glob 
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

plt.rc('text', usetex=True)
plt.rc('font',family='serif')

runs =[0,1,5,7,9,10] 


for w in runs:
    #before = glob.glob('/home/nicole/Documents/thesis_code/ipac2017_measurements/*w1_*.stat')
    before = glob.glob('/home/nicole/Documents/thesis_code/ipac2017_measurements/*_w'+str(w)+'_*.stat')
    #after  = glob.glob('/home/nicole/Documents/thesis_code/data/ipac2017/*weight*.stat')
    #fn = '/home/nicole/Documents/thesis_code/data/optLinac_weight0.stat'
    plotfn = './beamsizes_weight'+str(w)+'.pdf'
    '''
    plt.axvline(x=3.1)
    plt.axvline(x=6.377)
    plt.axvline(x=8.76)
    plt.axvline(x=11.477)
    plt.axvline(x=14.848)
    '''
    pdf = matplotlib.backends.backend_pdf.PdfPages(plotfn) 

    fig1, ax1 = plt.subplots()
    plt.title("Beam Sizes")
    plt.xlabel("z [m]")
    plt.grid('on')
    

    fig2, ax2 = plt.subplots()
    plt.title("Emittance")
    plt.xlabel("z [m]")
    plt.ylabel("xemit [um]")
    if int(w) < 7:
        plt.axis([0.0,20.0,0.0,450])
    else:
        plt.axis([0.0,20.0,0.0,100])
    plt.grid('on')

    fig3, ax3 = plt.subplots()
    plt.title('Bunch Length')
    plt.xlabel('z [m]')
    plt.ylabel('zrms [mm]')
    plt.grid('on')

    fig4, ax4 = plt.subplots()
    plt.title('Energy')
    plt.xlabel('z [m]')
    plt.ylabel('E [MeV]')
    plt.grid('on')

    for fn in before: 
        print(fn)
        legend = (fn.split('_')[4]).split('.')[0]
        #print legend
        parser = SddsReader(fn)                                                                                  
        #x = []
        z = parser.getColumn("s")
        xrms = parser.getColumn("rms_x")
        yrms = parser.getColumn("rms_y")
        zrms = parser.getColumn("rms_s")
        xemit = parser.getColumn("emit_x")
        energy = parser.getColumn("energy")
                  
        rmsymm = [l*10**3 for l in yrms]
        rmsxmm = [m*10**3 for m in xrms]
        rmszmm = [n*10**3 for n in zrms]
        xemitum = [o*10**6 for o in xemit]

        ax1.plot(z, rmsxmm, label=legend)
        ax2.plot(z, xemitum, label=legend)
        ax3.plot(z, rmszmm, label=legend)
        ax4.plot(z, energy, label=legend)

    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    pdf.savefig(fig1, dpi=1000, bbox_inches='tight')
    pdf.savefig(fig2, dpi=1000, bbox_inches='tight')
    pdf.savefig(fig3, dpi=1000, bbox_inches='tight')
    pdf.savefig(fig4, dpi=1000, bbox_inches='tight')
    pdf.close()

'''
for fn2 in after:
    legend2 = (fn2.split('_')[2]).split('.')[0] + ' grad 2'
    #print legend2
    parser = SddsReader(fn2)
    x = parser.getColumn("s")
    y = parser.getColumn("rms_x")
                      
    ymm = [l*10**3 for l in y]
    plt.plot(x,ymm, '.', markevery=800, label=legend2)
'''
#plt.legend(bbox_to_anchor=(1.5, 1.0))
#plt.xlabel("Z [m]")
#plt.ylabel("xrms [mm]")
#plt.title("Beam Sizes")
#plt.savefig(plotfn, bbox_inches='tight', dpi=900)
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
