from TableScraper import ScrapeTableByRowCount
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import numpy as np
import string

def ConvertSAtoIA(input):
    return np.array([int(y) for y in input])

def ConvertYMDtoYears(value):

    value = value.replace('y', '')
    value = value.replace('m', '')
    value = value.replace('d', '')
    value = value.split(' ')

    fraction_age = int(value[0])+ float(value[1])/12.0 + float(value[2])/365.0
    return fraction_age

x = ScrapeTableByRowCount("https://www.statsf1.com/en/statistiques/pilote/champion/age.aspx", 4)
npX = np.array(x)
byYear = npX[np.argsort(npX[:,1])]

years = ConvertSAtoIA(byYear[:,1])
ages = np.array([ConvertYMDtoYears(y) for y in byYear[:,3]])
print(ages)

years_smooth = np.linspace(years.min(), years.max(), 400)
age_smooth = spline(years, ages, years_smooth)

plt.scatter(years, ages, marker=">")
plt.plot(years_smooth, age_smooth, 'red')
plt.xlabel('Year')
plt.ylabel('Age of winner')
plt.show()