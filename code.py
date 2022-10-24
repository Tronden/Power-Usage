import calendar
import numpy as np
from calendar import monthrange

Usage2011 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202011.csv"
Usage2012 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202012.csv"
Usage2013 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202013.csv"

def getAMSdata(filnavn):
    startTid, stopTid = np.loadtxt(filnavn, dtype=str , delimiter=";", skiprows=1, unpack=True, usecols=(0,1))
    forbruk = np.loadtxt(filnavn, delimiter=";", skiprows=1, unpack=True, usecols=(2))
    return startTid, stopTid, forbruk

def getstartTiddata(filnavn, rad_nr):
    startTid = np.loadtxt(filnavn, dtype=str , delimiter=";", skiprows=1, unpack=True, usecols=(0))
    return startTid[rad_nr]

def getstopTiddata(filnavn, rad_nr):
    stopTid = np.loadtxt(filnavn, dtype=str , delimiter=";", skiprows=1, unpack=True, usecols=(1))
    return stopTid[rad_nr]

def getForbrukdata(filnavn):
    forbruk = np.loadtxt(filnavn, delimiter=";", skiprows=1, unpack=True, usecols=(2))
    return forbruk

def vis_rad(filnavn, rad_nr): #Test for å sjekke innlesing.
    startTid, stopTid, forbruk = getAMSdata(filnavn)
    print("Forbruket mellom", startTid[rad_nr], "og", stopTid[rad_nr], "var", forbruk[rad_nr], "kWh")

def getAverage(filnavn): # Rekner ut average forbruk for alle forbruksverdiene på lista.
    avgforbruk = sum(getForbrukdata(filnavn))/len(getForbrukdata(filnavn))
    print ("Average forbruk", ":", round(avgforbruk,3), "kWh")
    return avgforbruk

def getYear(dateAndTimeStr):
    year = (int(dateAndTimeStr[6:10]))
    return year

def getMonth(dateAndTimeStr):
    month = (calendar.month_name[int(dateAndTimeStr[3:5])])
    return month

def getDaysInMonth(dateAndTimeStr):
    days = monthrange(getYear((getstartTiddata(Usage2011, 150))), int(dateAndTimeStr[3:5]))
    return days[1]

vis_rad(Usage2011, 150)

print(getYear(getstartTiddata(Usage2011, 150)))
print(getMonth(getstartTiddata(Usage2011, 150)))
print(getDaysInMonth(getstartTiddata(Usage2011, 150)))

getAverage(Usage2013)