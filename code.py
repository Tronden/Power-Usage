import calendar
import numpy as np
from calendar import monthrange

Usage1 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202011.csv"
Usage2 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202012.csv"
Usage3 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202013.csv"

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

def getAverage(filnavn): # Rekna ut average forbruk for alle forbruksverdiene på lista.
    avgforbruk = sum(getForbrukdata(filnavn))/len(getForbrukdata(filnavn))
    return avgforbruk

def getYear(filnavn, rad_nr):
    year = int(getstartTiddata(filnavn, rad_nr)[6:10])
    return year

def getMonth(filnavn, rad_nr):
    month = (calendar.month_name[int(getstartTiddata(filnavn, rad_nr)[3:5])])
    return month

def getDaysInMonth(filnavn, rad_nr):
    days = monthrange(getYear(filnavn, rad_nr), int(getstartTiddata(filnavn, rad_nr)[3:5]))
    return days[1]

def getdays(filnavn, rad_nr):
    days = int(getstartTiddata(filnavn, rad_nr)[0:2])
    return days

def getHours(filnavn, rad_nr):
    hours = int(getstartTiddata(filnavn, rad_nr)[11:13])
    return hours

def findPeakInterval(filnavn):
    forbruk = getForbrukdata(filnavn)
    peak = max(forbruk)
    peakindex = np.where(forbruk == peak)
    peakindex = peakindex[0][0]
    return peak, peakindex

def findLowestInterval(filnavn):
    forbruk = getForbrukdata(filnavn)
    lowest = min(forbruk)
    lowestindex = np.where(forbruk == lowest)
    lowestindex = lowestindex[0][0]
    return lowest, lowestindex
    
def getAverageMonth(filnavn, rad_nr):
    avgMonth = getAverage(filnavn)*getDaysInMonth(filnavn, rad_nr)
    print("Average forbruk for", getMonth(filnavn, rad_nr), "er", round(avgMonth,3), "kWh")
    return avgMonth

def getAverageDay(filnavn, rad_nr):
    avgDay = getAverageMonth(filnavn, rad_nr)/getDaysInMonth(filnavn, rad_nr)
    print("Average forbruk for", getMonth(filnavn, rad_nr), "er", round(avgDay,3), "kWh")
    return avgDay

Liste = Usage3
Rad = 150

vis_rad(Liste, Rad)
print("Year:", getYear(Liste, Rad))
print("Month:", getMonth(Liste, Rad))
print("Day's in month:", getDaysInMonth(Liste, Rad))
print("Peak intervallet er mellom", getstartTiddata(Liste, findPeakInterval(Liste)[1]), "og", getstopTiddata(Liste, findPeakInterval(Liste)[1]), "med", findPeakInterval(Liste)[0], "kWh")
print("Laveste intervallet er mellom", getstartTiddata(Liste, findLowestInterval(Liste)[1]), "og", getstopTiddata(Liste, findLowestInterval(Liste)[1]), "med", findLowestInterval(Liste)[0], "kWh")
getAverageMonth(Liste, Rad)
getAverageDay(Liste, Rad)