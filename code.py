from asyncio.format_helpers import _format_callback_source
import numpy as np

Usage2011 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202011.csv"
Usage2012 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202012.csv"
Usage2013 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202101.csv"

def getAMSdata(filnavn, rad_nr):
    startTid, stopTid = np.loadtxt(filnavn, dtype=str , delimiter=";", skiprows=1, unpack=True, usecols=(0,1))
    forbruk = np.loadtxt(filnavn, delimiter=";", skiprows=1, unpack=True, usecols=(2))
    return startTid, stopTid, forbruk

"""
Test for å sjekke innlesing.
def vis_rad(filnavn, rad_nr):
    startTid, stopTid, forbruk = getAMSdata(filnavn, rad_nr)
    print("Forbruket mellom", startTid[rad_nr], "og", stopTid[rad_nr], "var", forbruk[rad_nr], "kWh")
    
vis_rad(Usage2011, 0)
"""
# Rekner ut average forbruk for alle forbruks verdiene på lista.
def getAverage(filnavn):
    forbruk = sum(np.loadtxt(filnavn, delimiter=";", skiprows=1, unpack=True, usecols=(2)))
    avgforbruk = forbruk / len(np.loadtxt(filnavn, delimiter=";", skiprows=1, unpack=True, usecols=(2)))
    print ("Average forbruk", filnavn[-8:-4], round(avgforbruk,3), "kWh")
    return avgforbruk

getAverage(Usage2012)