import csv

def calculateAvgHwy(x):
    with open ('./files/mpg.csv') as f:
        mpg = list(csv.DictReader(f))

    HwyMpgByClass = []
    vehicleclass = set(d['class'] for d in mpg)
    for v in vehicleclass:
        summpg = 0
        vclasscount = 0
        for e in mpg:
            if e['class'] == v:
                summpg += float(e['hwy'])
                vclasscount += 1
        x = (v, summpg/vclasscount)
        HwyMpgByClass.append(x)
    return dict(HwyMpgByClass)
