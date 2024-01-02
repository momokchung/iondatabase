list1 = [
    0.80,
    0.90,
    0.95,
    1.00,
    1.05,
    1.10,
    1.20,
    1.30,
    1.40,
    1.50,
    2.00,
]

list2 = [
    0.90,
    0.95,
    1.00,
    1.05,
    1.10,
    1.20,
    1.30,
    1.40,
    1.50,
    2.00,
]

list3 = [
    1.00,
]


list4 = [
    1.00,
    1.10,
    1.20,
    1.30,
    1.40,
    1.50,
    2.00
]

list5 = [
    -60,
    -45,
    -30,
    -15,
    0,
    15,
    30,
    45,
    60,
    
]

allTwoBody = {
    # 1
    "Li-F":  list1,
    "Li-Cl": list1,
    "Li-Br": list1,
    "Na-F":  list1,
    "Na-Cl": list1,
    "Na-Br": list1,
    "K-F":   list1,
    "K-Cl":  list1,
    "K-Br":  list1,

    # 2
    "Li-Water": list1,
    "Na-Water": list1,
    "K-Water":  list1,
    "F-Water":  list1,
    "Cl-Water": list1,
    "Br-Water": list1,

    # 3
    "Li-2Water": list2,
    "Na-2Water": list2,
    "K-2Water":  list2,
    "F-2Water":  list2,
    "Cl-2Water": list2,
    "Br-2Water": list2,

    # 4
    "Li-3Water": list3,
    "Li-4Water": list3,
    "Li-5Water": list3,
    "Li-6Water": list3,
    "Na-3Water": list3,
    "Na-4Water": list3,
    "Na-5Water": list3,
    "Na-6Water": list3,
    "K-3Water":  list3,
    "K-4Water":  list3,
    "K-5Water":  list3,
    "K-6Water":  list3,
    "F-3Water":  list3,
    "F-4Water":  list3,
    "F-5Water":  list3,
    "F-6Water":  list3,
    "Cl-3Water": list3,
    "Cl-4Water": list3,
    "Cl-5Water": list3,
    "Cl-6Water": list3,
    "Br-3Water": list3,
    "Br-4Water": list3,
    "Br-5Water": list3,
    "Br-6Water": list3,

    # 5
    "Li-Water_Deg00": list5,
    "Na-Water_Deg00": list5,
    "K-Water_Deg00":  list5,
    "F-Water_Deg00":  list5,
    "Cl-Water_Deg00": list5,
    "Br-Water_Deg00": list5,
    "Li-Water_Deg15": list5,
    "Na-Water_Deg15": list5,
    "K-Water_Deg15":  list5,
    "F-Water_Deg15":  list5,
    "Cl-Water_Deg15": list5,
    "Br-Water_Deg15": list5,
    "Li-Water_Deg30": list5,
    "Na-Water_Deg30": list5,
    "K-Water_Deg30":  list5,
    "F-Water_Deg30":  list5,
    "Cl-Water_Deg30": list5,
    "Br-Water_Deg30": list5,
    "Li-Water_Deg45": list5,
    "Na-Water_Deg45": list5,
    "K-Water_Deg45":  list5,
    "F-Water_Deg45":  list5,
    "Cl-Water_Deg45": list5,
    "Br-Water_Deg45": list5,
    "Li-Water_Deg60": list5,
    "Na-Water_Deg60": list5,
    "K-Water_Deg60":  list5,
    "F-Water_Deg60":  list5,
    "Cl-Water_Deg60": list5,
    "Br-Water_Deg60": list5,

    # 6
    "LiF-Li":  list4,
    "LiF-F":   list4,
    "LiCl-Li": list4,
    "LiCl-Cl": list4,
    "LiBr-Li": list4,
    "LiBr-Br": list4,
    "NaF-Na":  list4,
    "NaF-F":   list4,
    "NaCl-Na": list4,
    "NaCl-Cl": list4,
    "NaBr-Na": list4,
    "NaBr-Br": list4,
    "KF-K":    list4,
    "KF-F":    list4,
    "KCl-K":   list4,
    "KCl-Cl":  list4,
    "KBr-K":   list4,
    "KBr-Br":  list4,

    # 7
    "Li-Li": list4,
    "Li-Na": list4,
    "Li-K":  list4,
    "Na-Na": list4,
    "Na-K":  list4,
    "K-K":   list4,
    "F-F":   list4,
    "F-Cl":  list4,
    "F-Br":  list4,
    "Cl-Cl": list4,
    "Cl-Br": list4,
    "Br-Br": list4,

    # 8
    "Li-Water_neq": list4,
    "Na-Water_neq": list4,
    "K-Water_neq":  list4,
    "F-Water_neq":  list4,
    "Cl-Water_neq": list4,
    "Br-Water_neq": list4,

    # 9
    "Li-2Water_neq": list4,
    "Na-2Water_neq": list4,
    "K-2Water_neq":  list4,
    "F-2Water_neq":  list4,
    "Cl-2Water_neq": list4,
    "Br-2Water_neq": list4,
}

allThreeBody = {
    # tb3
    "Li-2Water": list2,
    "Na-2Water": list2,
    "K-2Water":  list2,
    "F-2Water":  list2,
    "Cl-2Water": list2,
    "Br-2Water": list2,

    # tb6
    "LiF-Li":  list4,
    "LiF-F":   list4,
    "LiCl-Li": list4,
    "LiCl-Cl": list4,
    "LiBr-Li": list4,
    "LiBr-Br": list4,
    "NaF-Na":  list4,
    "NaF-F":   list4,
    "NaCl-Na": list4,
    "NaCl-Cl": list4,
    "NaBr-Na": list4,
    "NaBr-Br": list4,
    "KF-K":    list4,
    "KF-F":    list4,
    "KCl-K":   list4,
    "KCl-Cl":  list4,
    "KBr-K":   list4,
    "KBr-Br":  list4,

    # tb9
    "Li-2Water_neq": list4,
    "Na-2Water_neq": list4,
    "K-2Water_neq":  list4,
    "F-2Water_neq":  list4,
    "Cl-2Water_neq": list4,
    "Br-2Water_neq": list4,
}

catAnEquil = {
    "Li-F":  1.584155,
    "Li-Cl": 2.029797,
    "Li-Br": 2.170734,
    "Na-F":  1.939580,
    "Na-Cl": 2.370103,
    "Na-Br": 2.514159,
    "K-F":   2.175180,
    "K-Cl":  2.633546,
    "K-Br":  2.788700,
}

ionWaterEquil = {
    "Li-Water": 1.828878,
    "Na-Water": 2.158940,
    "K-Water":  2.466222,
    "F-Water":  2.426389,
    "Cl-Water": 3.070352,
    "Br-Water": 3.212066,
}

ion2WaterEquil = {
    "Li-2Water": 1.855757,
    "Na-2Water": 2.235038,
    "K-2Water":  2.525195,
    "F-2Water":  1.741108,
    "Cl-2Water": 2.677578,
    "Br-2Water": 2.832825,
}

ionManyWater = [
    "Li-3Water", "Li-4Water", "Li-5Water", "Li-6Water",
    "Na-3Water", "Na-4Water", "Na-5Water", "Na-6Water",
     "K-3Water",  "K-4Water",  "K-5Water",  "K-6Water",
     "F-3Water",  "F-4Water",  "F-5Water",  "F-6Water",
    "Cl-3Water", "Cl-4Water", "Cl-5Water", "Cl-6Water",
    "Br-3Water", "Br-4Water", "Br-5Water", "Br-6Water",
]

counter = 1
index = {}
for i,k in allTwoBody.items():
    index[i] = str(counter).zfill(3)
    counter += 1

ionIonXyz = """2
 1 {0:2s}     0.000000     0.000000     0.000000{2:5d}
 2 {1:2s}{4:13.6f}     0.000000     0.000000{3:5d}
"""

ionIonPsi4 = """
{0} 1
{1:2s}     0.000000     0.000000     0.000000
--
{2} 1
{3:2s}{4:13.6f}     0.000000     0.000000
"""

ionIonQchem = """
{0} 1
--
{1} 1
{2:2s}     0.000000     0.000000     0.000000
--
{3} 1
{4:2s}{5:13.6f}     0.000000     0.000000
"""

ionWaterXyz = """4
 1 O {:13.6f}{:13.6f}{:13.6f}    1    2    3
 2 H {:13.6f}{:13.6f}{:13.6f}    2    1
 3 H {:13.6f}{:13.6f}{:13.6f}    2    1
 4 {:2s}{:13.6f}     0.000000     0.000000{:5d}
"""

ionWaterPsi4 = """
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
"""

ionWaterQchem = """
{} 1
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
"""

ion2WaterXyz = """7
 1 {:2s}{:13.6f}     0.000000     0.000000{:5d}
 2 O {:13.6f}{:13.6f}{:13.6f}    1    3    4
 3 H {:13.6f}{:13.6f}{:13.6f}    2    2
 4 H {:13.6f}{:13.6f}{:13.6f}    2    2
 5 O {:13.6f}{:13.6f}{:13.6f}    1    6    7
 6 H {:13.6f}{:13.6f}{:13.6f}    2    5
 7 H {:13.6f}{:13.6f}{:13.6f}    2    5
"""

ion2WaterPsi4 = """
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion2WaterQchem = """
{} 1
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion3WaterXyz = """10
 1 {:2s}{:13.6f}     0.000000     0.000000{:5d}
 2 O {:13.6f}{:13.6f}{:13.6f}    1    3    4
 3 H {:13.6f}{:13.6f}{:13.6f}    2    2
 4 H {:13.6f}{:13.6f}{:13.6f}    2    2
 5 O {:13.6f}{:13.6f}{:13.6f}    1    6    7
 6 H {:13.6f}{:13.6f}{:13.6f}    2    5
 7 H {:13.6f}{:13.6f}{:13.6f}    2    5
 8 O {:13.6f}{:13.6f}{:13.6f}    1    9   10
 9 H {:13.6f}{:13.6f}{:13.6f}    2    8
10 H {:13.6f}{:13.6f}{:13.6f}    2    8
"""

ion3WaterPsi4 = """
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion3WaterQchem = """
{} 1
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion4WaterXyz = """13
 1 {:2s}{:13.6f}     0.000000     0.000000{:5d}
 2 O {:13.6f}{:13.6f}{:13.6f}    1    3    4
 3 H {:13.6f}{:13.6f}{:13.6f}    2    2
 4 H {:13.6f}{:13.6f}{:13.6f}    2    2
 5 O {:13.6f}{:13.6f}{:13.6f}    1    6    7
 6 H {:13.6f}{:13.6f}{:13.6f}    2    5
 7 H {:13.6f}{:13.6f}{:13.6f}    2    5
 8 O {:13.6f}{:13.6f}{:13.6f}    1    9   10
 9 H {:13.6f}{:13.6f}{:13.6f}    2    8
10 H {:13.6f}{:13.6f}{:13.6f}    2    8
11 O {:13.6f}{:13.6f}{:13.6f}    1   12   13
12 H {:13.6f}{:13.6f}{:13.6f}    2   11
13 H {:13.6f}{:13.6f}{:13.6f}    2   11
"""

ion4WaterPsi4 = """
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion4WaterQchem = """
{} 1
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion5WaterXyz = """16
 1 {:2s}{:13.6f}     0.000000     0.000000{:5d}
 2 O {:13.6f}{:13.6f}{:13.6f}    1    3    4
 3 H {:13.6f}{:13.6f}{:13.6f}    2    2
 4 H {:13.6f}{:13.6f}{:13.6f}    2    2
 5 O {:13.6f}{:13.6f}{:13.6f}    1    6    7
 6 H {:13.6f}{:13.6f}{:13.6f}    2    5
 7 H {:13.6f}{:13.6f}{:13.6f}    2    5
 8 O {:13.6f}{:13.6f}{:13.6f}    1    9   10
 9 H {:13.6f}{:13.6f}{:13.6f}    2    8
10 H {:13.6f}{:13.6f}{:13.6f}    2    8
11 O {:13.6f}{:13.6f}{:13.6f}    1   12   13
12 H {:13.6f}{:13.6f}{:13.6f}    2   11
13 H {:13.6f}{:13.6f}{:13.6f}    2   11
14 O {:13.6f}{:13.6f}{:13.6f}    1   15   16
15 H {:13.6f}{:13.6f}{:13.6f}    2   14
16 H {:13.6f}{:13.6f}{:13.6f}    2   14
"""

ion5WaterPsi4 = """
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion5WaterQchem = """
{} 1
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion6WaterXyz = """19
 1 {:2s}{:13.6f}     0.000000     0.000000{:5d}
 2 O {:13.6f}{:13.6f}{:13.6f}    1    3    4
 3 H {:13.6f}{:13.6f}{:13.6f}    2    2
 4 H {:13.6f}{:13.6f}{:13.6f}    2    2
 5 O {:13.6f}{:13.6f}{:13.6f}    1    6    7
 6 H {:13.6f}{:13.6f}{:13.6f}    2    5
 7 H {:13.6f}{:13.6f}{:13.6f}    2    5
 8 O {:13.6f}{:13.6f}{:13.6f}    1    9   10
 9 H {:13.6f}{:13.6f}{:13.6f}    2    8
10 H {:13.6f}{:13.6f}{:13.6f}    2    8
11 O {:13.6f}{:13.6f}{:13.6f}    1   12   13
12 H {:13.6f}{:13.6f}{:13.6f}    2   11
13 H {:13.6f}{:13.6f}{:13.6f}    2   11
14 O {:13.6f}{:13.6f}{:13.6f}    1   15   16
15 H {:13.6f}{:13.6f}{:13.6f}    2   14
16 H {:13.6f}{:13.6f}{:13.6f}    2   14
17 O {:13.6f}{:13.6f}{:13.6f}    1   18   19
18 H {:13.6f}{:13.6f}{:13.6f}    2   17
19 H {:13.6f}{:13.6f}{:13.6f}    2   17
"""

ion6WaterPsi4 = """
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

ion6WaterQchem = """
{} 1
--
{} 1
{:2s}{:13.6f}     0.000000     0.000000
--
0 1
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
O {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
H {:13.6f}{:13.6f}{:13.6f}
"""

atomType = {
    "Li": 6,
    "Na": 7,
    "K":  8,
    "F":  14,
    "Cl": 15,
    "Br": 16,
}

atomCharge = {
    "Li": 1,
    "Na": 1,
    "K":  1,
    "F": -1,
    "Cl":-1,
    "Br":-1,
}

psi4Header = "MEMORY {} GB\n\n"

psi4Molecule = """molecule dimer {{{}
units ang
no_reorient
no_com
symmetry c1
}}

"""

psi4Set = """set {{{}}}

"""

psi4Final = "{}\n"

almoMolecule = "$molecule{}$end\n\n"

almoFinal = """$rem
JOBTYPE          eda
EDA2             1
METHOD           wB97M-V
BASIS            {}
SYMMETRY         false
MEM_TOTAL        50000
MEM_STATIC       10000
THRESH           14
SCF_CONVERGENCE  8
XC_GRID          000099000590
NL_GRID          1
EDA_CLS_DISP     true
FD_MAT_VEC_PROD  FALSE
$end
"""
