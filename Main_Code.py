#Coded in Visual Studio Code with Python 3.9.12
#Authors Emil Bjorneset, Simen Vangberg and Trond Zachariassen
#Coding started 24.10.2022
#Uploaded to github - Last changed 01.11.2022
#Link: https://github.com/Tronden/Power-Usage

#Importing libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import calendar
from calendar import monthrange

#File directory (Change to your own data\ path)
Usage1 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202011.csv"
Usage2 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202012.csv"
Usage3 = r"A:\OneDrive Personal\OneDrive\Visual Studio Code\Innføring ingeniørfag\Power Usage\Power-Usage\data\meteringvalues-mp-xxxxx-consumption-202101.csv"

#Printing available files
print("Available files:")
print(Usage1[-51:-4])
print(Usage2[-51:-4])
print(Usage3[-51:-4])

#User input  
a = int(input("Choose date: 1 = Nov 2020, 2 = Des 2020, 3 = Jan 2021: "))
if a == 1:
    Liste = Usage1
    Year = int(2020)
    Month = int(11)
    a = 0     
elif a == 2:
    Liste = Usage2
    Year = int(2020)
    Month = int(12)
    a = 0  
elif a == 3:
    Liste = Usage3
    Year = int(2021)
    Month = int(1)
    a = 0   
else:   
    a = 0
    print("Data ikkje tilgjengelig")

#Function for reading input file and returning the start time.
def getstartTiddata(filnavn, rad_nr):
    startTid = np.loadtxt(filnavn, dtype=str , delimiter=";", skiprows=1, unpack=True, usecols=(0))
    return startTid[rad_nr]

#Function for reading input file and returning the stop time.
def getstopTiddata(filnavn, rad_nr):
    stopTid = np.loadtxt(filnavn, dtype=str , delimiter=";", skiprows=1, unpack=True, usecols=(1))
    return stopTid[rad_nr]

#Function for reading input file and returning the consumption.
def getForbrukdata(filnavn):
    forbruk = np.loadtxt(filnavn, delimiter=";", skiprows=1, unpack=True, usecols=(2))
    return forbruk

#Function for getting amount of days in month by using calendar monthrange with predefined year and month.
def getDaysInMonth():
    days = monthrange(Year, Month)
    return days[1]

#Function for gettig average consumption in month.
def getAverage(filnavn):
    forbruk = getForbrukdata(filnavn)
    average = np.mean(forbruk)
    return average

#Funtion for finding peak interval.
def findPeakInterval(filnavn):
    forbruk = getForbrukdata(filnavn)
    peak = max(forbruk)
    peakindex = np.where(forbruk == peak)
    peakindex = peakindex[0][0]
    return peak, peakindex

#Function for getting average consumption per day in month.
def AveragePerDay(filnavn):
    forbruk = getForbrukdata(filnavn)
    days = monthrange(Year, Month)
    averagePerDay = np.mean(forbruk.reshape(days[1], 24), axis=1)
    return averagePerDay

#Function for plotting average daily consumption in month.
def plotAveragePerDayInMonth(filnavn):
    plt.figure()
    plt.title("Average comsumption per day " + (calendar.month_name[Month]) + " " + str(Year))
    x_verdier = np.arange(1, int(getDaysInMonth())+1)
    y_verdier = np.array(AveragePerDay(filnavn))
    plt.bar(x_verdier, y_verdier)
    plt.xlabel("Day")
    plt.ylabel("kWh")
    plt.show()

#Function for getting average hourly consumption for a average day in month.
def getAverageperhour(filnavn):
    forbruk = getForbrukdata(filnavn)
    averageperhour = np.mean(forbruk.reshape(int(getDaysInMonth()), 24), axis=0)
    return averageperhour

#Function for plotting average hourly consumption for a average day in month.
def plotAverageHourlyConsumption(filnavn):
    plt.figure()
    plt.title("Average hourly consumption in month")
    x_verdier = np.arange(1, 25)
    y_verdier = np.array(getAverageperhour(filnavn))
    plt.plot(x_verdier, y_verdier)
    plt.xlabel("Hour")
    plt.ylabel("kWh")
    plt.show()

#Function for main program.
def main():
    plotAveragePerDayInMonth(Liste)
    plotAverageHourlyConsumption(Liste)
    print("Day's in month:", getDaysInMonth())
    print("Average hourly consumption in month:", getAverage(Liste), "kWh")
    print("Peak interval is between", getstartTiddata(Liste, findPeakInterval(Liste)[1]), "and", getstopTiddata(Liste, findPeakInterval(Liste)[1]), "with", findPeakInterval(Liste)[0], "kWh")

#Calling main program.
main()