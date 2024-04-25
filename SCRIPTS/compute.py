import subprocess
import pandas as pd

class Energy:
    def __init__(self, int_=0, pot=0, vdw=0, ele=0, pol=0):
        self.int = int_
        self.pot = pot
        self.vdw = vdw
        self.ele = ele
        self.pol = pol
    
    def __sub__(self, other):
        int_diff = self.int - other.int
        pot_diff = self.pot - other.pot
        vdw_diff = self.vdw - other.vdw
        ele_diff = self.ele - other.ele
        pol_diff = self.pol - other.pol
        return Energy(int_diff,pot_diff,vdw_diff,ele_diff,pol_diff)
    
    def __isub__(self, other):
        self.int -= other.int
        self.pot -= other.pot
        self.vdw -= other.vdw
        self.ele -= other.ele
        self.pol -= other.pol
        return self
    
    def __add__(self, other):
        int_diff = self.int + other.int
        pot_diff = self.pot + other.pot
        vdw_diff = self.vdw + other.vdw
        ele_diff = self.ele + other.ele
        pol_diff = self.pol + other.pol
        return Energy(int_diff,pot_diff,vdw_diff,ele_diff,pol_diff)
    
    def __iadd__(self, other):
        self.int += other.int
        self.pot += other.pot
        self.vdw += other.vdw
        self.ele += other.ele
        self.pol += other.pol
        return self

def analyze(exe, key, xyz):
    # Command to run
    command = f"{exe} -k {key} {xyz} e"
    
    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Get the output and error
    output, error = process.communicate()
    
    # Split the output into a list of strings
    lines = output.decode().splitlines()
    
    energy = Energy()
    
    # Read lines
    for line in lines:
        if " Intermolecular Energy : " in line:
            energy.int = float(line.split()[-2])
        elif " Total Potential Energy : " in line:
            energy.pot = float(line.split()[-2])
        elif " Van der Waals " in line:
            energy.vdw = float(line.split()[-2])
        elif " Atomic Multipoles " in line:
            energy.ele = float(line.split()[-2])
        elif " Polarization " in line:
            energy.pol = float(line.split()[-2])
    
    return energy

def computeAddSub(exe, key, xyz, add, sub):
    energy = analyze(exe, key, xyz)
    fn = xyz.split(".xyz")[0]
    for A in add:
        xyzA = fn + f"_{A}.xyz"
        energyA = analyze(exe, key, xyzA)
        energy += energyA
    for A in sub:
        xyzA = fn + f"_{A}.xyz"
        energyA = analyze(exe, key, xyzA)
        energy -= energyA
    
    return energy

def compute(exe, key, xyz, ctype):
    add = []
    if ctype in [1, 2, 5, 7, 8]:
        sub = []
    elif ctype == 3:
        sub = ["12"]
    elif ctype == 4:
        sub = ["B"]
    elif ctype == 6:
        sub = ["01"]
    elif ctype == 9:
        sub = ["0", "12"]
    elif ctype == 10:
        sub = ["B"]
    else:
        raise Exception()
    energy = computeAddSub(exe, key, xyz, add, sub)

    return energy

def computeTB(exe, key, xyz, ctype):
    if ctype == 3:
        sub = ["01","02","12"]
        add = ["1","2"]
    elif ctype == 6:
        sub = ["01","02","12"]
        add = []
    elif ctype == 9:
        sub = ["01","02","12"]
        add = ["0"]
    else:
        raise Exception()
    
    energy = computeAddSub(exe, key, xyz, add, sub)
    
    return energy

def getQMMethods(QM):
    QM_methods = {}

    if "ALMO" in QM.keys():
        ALMO = pd.read_csv('ions.ALMO.dat', delim_whitespace=True)
        ALMO = ALMO.rename(columns={'ALMO/TZVPPD': 'Total'})
        ALMO['Induction'] = ALMO['Polarization'] + ALMO['ChargeTransfer']
        ALMO['VdW'] = ALMO['Exchange'] + ALMO['Dispersion']
        QM_methods["ALMO"] = ALMO

    if "SAPT" in QM.keys():
        SAPT = pd.read_csv('ions.SAPT.dat', delim_whitespace=True)
        SAPT = SAPT.rename(columns={'SAPT2+/aVTZ': 'Total'})
        SAPT['VdW'] = SAPT['Exchange'] + SAPT['Dispersion']
        QM_methods["SAPT"] = SAPT

    if "MP2" in QM.keys():
        MP2 = pd.read_csv('ions.MP2.dat', delim_whitespace=True)
        MP2 = MP2.rename(columns={'MP2/aVTZ': 'Total'})
        QM_methods["MP2"] = MP2

    if "MP2CLS" in QM.keys():
        MP2CLS = pd.read_csv('ions.MP2CLS.dat', delim_whitespace=True)
        MP2CLS = MP2CLS.rename(columns={'MP2/aVTZ': 'Total'})
        QM_methods["MP2CLS"] = MP2CLS

    if "MP2TB" in QM.keys():
        MP2TB = pd.read_csv('ions.MP2TB.dat', delim_whitespace=True)
        MP2TB = MP2TB.rename(columns={'ThreeBodyMP2/aVTZ': 'Total'})
        MP2TB = MP2TB.drop('TwoBodyMP2/aVTZ', axis=1)
        QM_methods["MP2TB"] = MP2TB
    
    return QM_methods

def getFFMethods(FF):
    FF_methods = {}

    if "AMOEBA" in FF.keys():
        AMOEBA = pd.read_csv('ions.AMOEBA.dat', delim_whitespace=True)
        AMOEBA = AMOEBA.rename(columns={
            'Polarization': 'Induction',
            'AMOEBA': 'Total'
        })
        FF_methods["AMOEBA"] = AMOEBA

    if "AMOEBACLS" in FF.keys():
        AMOEBACLS = pd.read_csv('ions.AMOEBACLS.dat', delim_whitespace=True)
        AMOEBACLS = AMOEBACLS.rename(columns={'AMOEBA': 'Total'})
        FF_methods["AMOEBACLS"] = AMOEBACLS

    if "AMOEBATB" in FF.keys():
        AMOEBATB = pd.read_csv('ions.AMOEBATB.dat', delim_whitespace=True)
        AMOEBATB = AMOEBATB.rename(columns={'AMOEBA': 'Total'})
        FF_methods["AMOEBATB"] = AMOEBATB

    if "AMOEBAF" in FF.keys():
        AMOEBAF = pd.read_csv('ions.AMOEBAF.dat', delim_whitespace=True)
        AMOEBAF = AMOEBAF.rename(columns={
            'Polarization': 'Induction',
            'AMOEBA': 'Total'
        })
        FF_methods["AMOEBAF"] = AMOEBAF

    if "AMOEBAFCLS" in FF.keys():
        AMOEBAFCLS = pd.read_csv('ions.AMOEBAFCLS.dat', delim_whitespace=True)
        AMOEBAFCLS = AMOEBAFCLS.rename(columns={'AMOEBA': 'Total'})
        FF_methods["AMOEBAFCLS"] = AMOEBAFCLS

    if "AMOEBAFTB" in FF.keys():
        AMOEBAFTB = pd.read_csv('ions.AMOEBAFTB.dat', delim_whitespace=True)
        AMOEBAFTB = AMOEBAFTB.rename(columns={'AMOEBA': 'Total'})
        FF_methods["AMOEBAFTB"] = AMOEBAFTB
    
    return FF_methods

intClass = {
    # 1
    "Li-F":  1,
    "Li-Cl": 1,
    "Li-Br": 1,
    "Na-F":  1,
    "Na-Cl": 1,
    "Na-Br": 1,
    "K-F":   1,
    "K-Cl":  1,
    "K-Br":  1,

    # 2
    "Li-Water": 2,
    "Na-Water": 2,
    "K-Water":  2,
    "F-Water":  2,
    "Cl-Water": 2,
    "Br-Water": 2,

    # 3
    "Li-2Water": 3,
    "Na-2Water": 3,
    "K-2Water":  3,
    "F-2Water":  3,
    "Cl-2Water": 3,
    "Br-2Water": 3,

    # 4
    "Li-3Water": 4,
    "Li-4Water": 4,
    "Li-5Water": 4,
    "Li-6Water": 4,
    "Na-3Water": 4,
    "Na-4Water": 4,
    "Na-5Water": 4,
    "Na-6Water": 4,
    "K-3Water":  4,
    "K-4Water":  4,
    "K-5Water":  4,
    "K-6Water":  4,
    "F-3Water":  4,
    "F-4Water":  4,
    "F-5Water":  4,
    "F-6Water":  4,
    "Cl-3Water": 4,
    "Cl-4Water": 4,
    "Cl-5Water": 4,
    "Cl-6Water": 4,
    "Br-3Water": 4,
    "Br-4Water": 4,
    "Br-5Water": 4,
    "Br-6Water": 4,

    # 5
    "Li-Water_Deg00": 5,
    "Na-Water_Deg00": 5,
    "K-Water_Deg00":  5,
    "F-Water_Deg00":  5,
    "Cl-Water_Deg00": 5,
    "Br-Water_Deg00": 5,
    "Li-Water_Deg15": 5,
    "Na-Water_Deg15": 5,
    "K-Water_Deg15":  5,
    "F-Water_Deg15":  5,
    "Cl-Water_Deg15": 5,
    "Br-Water_Deg15": 5,
    "Li-Water_Deg30": 5,
    "Na-Water_Deg30": 5,
    "K-Water_Deg30":  5,
    "F-Water_Deg30":  5,
    "Cl-Water_Deg30": 5,
    "Br-Water_Deg30": 5,
    "Li-Water_Deg45": 5,
    "Na-Water_Deg45": 5,
    "K-Water_Deg45":  5,
    "F-Water_Deg45":  5,
    "Cl-Water_Deg45": 5,
    "Br-Water_Deg45": 5,
    "Li-Water_Deg60": 5,
    "Na-Water_Deg60": 5,
    "K-Water_Deg60":  5,
    "F-Water_Deg60":  5,
    "Cl-Water_Deg60": 5,
    "Br-Water_Deg60": 5,

    # 6
    "LiF-Li":  6,
    "LiF-F":   6,
    "LiCl-Li": 6,
    "LiCl-Cl": 6,
    "LiBr-Li": 6,
    "LiBr-Br": 6,
    "NaF-Na":  6,
    "NaF-F":   6,
    "NaCl-Na": 6,
    "NaCl-Cl": 6,
    "NaBr-Na": 6,
    "NaBr-Br": 6,
    "KF-K":    6,
    "KF-F":    6,
    "KCl-K":   6,
    "KCl-Cl":  6,
    "KBr-K":   6,
    "KBr-Br":  6,

    # 7
    "Li-Li": 7,
    "Li-Na": 7,
    "Li-K":  7,
    "Na-Na": 7,
    "Na-K":  7,
    "K-K":   7,
    "F-F":   7,
    "F-Cl":  7,
    "F-Br":  7,
    "Cl-Cl": 7,
    "Cl-Br": 7,
    "Br-Br": 7,

    # 8
    "Li-Water_neq": 8,
    "Na-Water_neq": 8,
    "K-Water_neq":  8,
    "F-Water_neq":  8,
    "Cl-Water_neq": 8,
    "Br-Water_neq": 8,

    # 9
    "2Li-Water_neq": 9,
    "2Na-Water_neq": 9,
    "2K-Water_neq":  9,
    "2F-Water_neq":  9,
    "2Cl-Water_neq": 9,
    "2Br-Water_neq": 9,
    
    # 10
    "Li-Water_Cls": 10,
    "Na-Water_Cls": 10,
    "K-Water_Cls":  10,
    "F-Water_Cls":  10,
    "Cl-Water_Cls": 10,
    "Br-Water_Cls": 10,
}
