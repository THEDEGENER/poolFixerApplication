from tkinter import *
from tkinter import ttk





root = Tk()
root.title("Pool Fixer")
s = ttk.Style()
s.theme_use('aqua')

# Configure mainframe and grid
mainframe = ttk.Frame(root, padding='10 10 10 10')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Define string variables
pool_width = IntVar()
pool_height = IntVar()
pool_depth = IntVar()
fcl = IntVar()
tcl = IntVar()
ta = IntVar()
ph = IntVar()
th = IntVar()
cya = IntVar()
total_pool_volume = StringVar()

def poolVolume(*args):
    pool_width_value = pool_width.get()
    pool_height_value = pool_height.get()
    pool_depth_value = pool_depth.get()
    pool_volume = pool_width_value * pool_height_value * pool_depth_value
    total_pool_volume.set(pool_volume)

def chemicals(*args):
    fcl_value = fcl.get()
    tcl_value = tcl.get()
    ta_value = ta.get()
    ph_value = ph.get()
    th_value = th.get()
    cya_value = cya.get()

    # fix logic error, especially for ph at some point #

    if fcl_value >= 0 and fcl_value <= 0.5:
        fcl_text = 'Use granular chlorine'
        fcl.set(fcl_text)
    elif fcl_value > 0.5:
        fcl_text = 'Chlorine levels are good!'
        fcl.set(fcl_text)
    else: 
        fcl_text = 'Invalid input'
        fcl.set(fcl_text)

    if tcl_value >= 0 and tcl_value <= 0.5:
        tcl_text = 'Use Xtreme shock'
        tcl.set(tcl_text)
    elif tcl_value > 0.5:
        tcl_text = 'Total chlorine level is good'
        tcl.set(tcl_text)
    else:
        tcl_text = 'Invalid input'
        tcl.set(tcl_text)

    if ta_value >= 0 and ta_value <= 40:
        ta_text = 'Use Buffer'
        ta.set(ta_text)
    elif ta_value > 40 and ta_value < 180:
        ta_text = 'Total Alkalinity level is good'
        ta.set(ta_text)
    else:
        ta_text = 'Invalid input'
        ta.set(ta_text)

    if ph_value >= 6.2 and ph_value <= 6.8:
        ph_text = 'Use Soda Ash'
        ph.set(ph_text)
    elif ph_value >= 8.4 and ph_value <= 9.0:
        ph_text = 'Use Dry Acid'
        ph.set(ph_text)
    else:
        ph_text = 'Invalid input'
        ph.set(ph_text)

    if th_value >= 0 and th_value <= 100:
        th_text = 'Use Calcium Increaser'
        th.set(th_text)
    elif th_value > 100:
        th_text = 'Calcium levels are good'
        th.set(th_text)
    else:
        th_text = 'Invalid input'
        th.set(th_text)

    if cya_value >= 0 and cya_value < 40:
        cya_text = 'Use UV Shield'
        cya.set(cya_text)
    elif cya_value < 0:
        cya_text = 'Invalid Input'
        cya.set(cya_text)
    else:
        cya_text = 'Levels are Good'
        cya.set(cya_text)

ttk.Label(mainframe, text="Input Pool dimensions").grid(columnspan=3, row=1, sticky=(W, E))

# POOL DIMENSIONS #

ttk.Label(mainframe, text="Width").grid(column=1, row=2, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=pool_width).grid(column=2, row=2, sticky=(W, E), pady=5)

ttk.Label(mainframe, text="Height").grid(column=1, row=3, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=pool_height).grid(column=2, row=3, sticky=(W, E), pady=5)

ttk.Label(mainframe, text="Depth").grid(column=1, row=4, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=pool_depth).grid(column=2, row=4, sticky=(W, E), pady=5)

ttk.Label(mainframe, text="Pool Volume is:").grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=total_pool_volume).grid(column=2, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Calculate Pool Volume", command=poolVolume).grid(column=1, row=6, columnspan=2, pady=10)

# POOL READINGS #

ttk.Label(mainframe, text="Input Pool Readings").grid(columnspan=3, row=7, sticky=(W, E))

ttk.Label(mainframe, text="FCL").grid(column=1, row=8, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=fcl).grid(column=2, row=8, sticky=(W, E), pady=5)
# ttk.Label(mainframe, textvariable=fcl).grid(column=3, row=8, sticky=(W, E))

ttk.Label(mainframe, text="TCL").grid(column=1, row=9, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=tcl).grid(column=2, row=9, sticky=(W, E), pady=5)
# ttk.Label(mainframe, textvariable=tcl).grid(column=3, row=9, sticky=(W, E))

ttk.Label(mainframe, text="TA").grid(column=1, row=10, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=ta).grid(column=2, row=10, sticky=(W, E), pady=5)
# ttk.Label(mainframe, textvariable=ta).grid(column=3, row=10, sticky=(W, E))

ttk.Label(mainframe, text="pH").grid(column=1, row=11, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=ph).grid(column=2, row=11, sticky=(W, E), pady=5)
# ttk.Label(mainframe, textvariable=ph).grid(column=3, row=11, sticky=(W, E))

ttk.Label(mainframe, text="TH").grid(column=1, row=12, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=th).grid(column=2, row=12, sticky=(W, E), pady=5)
# ttk.Label(mainframe, textvariable=th).grid(column=3, row=12, sticky=(W, E))

ttk.Label(mainframe, text="CYA").grid(column=1, row=13, sticky=(W, E))
ttk.Entry(mainframe, width=25, textvariable=cya).grid(column=2, row=13, sticky=(W, E), pady=5)
# ttk.Label(mainframe, textvariable=cya).grid(column=3, row=13, sticky=(W, E))

ttk.Button(mainframe, text="Determine required chemicals", command=chemicals).grid(column=1, row=14, columnspan=2, pady=10)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()


    