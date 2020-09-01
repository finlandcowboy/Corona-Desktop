import json
import requests
import country_stats
from googletrans import Translator
from datetime import date,time,datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def getCountries():
    response = requests.get('https://api.covid19api.com/countries')
    list_countries_data = response.json()
    countries = []
    for elem in list_countries_data:
        countries.append(elem.get('Country'))
    return countries

def getData(country):
        country.replace(' ', '-').lower()
        country_dayone_response = requests.get('https://api.covid19api.com/dayone/country/' + str(country))
        list_country_data = country_dayone_response.json()
        print(list_country_data)
        country_data = list_country_data[0]
        print(country_data)
        return country_data


summary = requests.get('https://api.covid19api.com/summary')
json_data = summary.json()
global_data = json_data.get('Global')
countries_data = json_data.get('Countries')
def getGlobalData(self):
    return 'Новые случаи:' + str(self.global_data.get('NewConfirmed')) + '\nВсего случаев:' + str(self.global_data.get('TotalConfirmed'))

def getCountryData(country):
    for elem in countries_data:
        if elem.get('Country') == country:
            return "Страна: " + Translator().translate(country, dest='ru').text + "\nКоличество случаев: " + str(elem.get('TotalConfirmed'))

    return 'No country found'



def getTrend(country):
    country.replace(' ', '-').lower()
    current_date = str(datetime.now()).split(' ')
    current_date = current_date[0]
    response = requests.get(
        'https://api.covid19api.com/total/country/' + country + '/status/confirmed?from=2020-03-01T00:00:00Z&to=' + current_date + 'T00:00:00Z')
    json_data = response.json()
    data = dict()
    for elem in json_data:
        data.update({str(elem['Date']): str(elem['Cases'])})

    cases = list(self.data.values())
    for elem in cases:
        elem = int(elem)

    case_dates1 = list(self.data.keys())
    case_dates = list()
    for elem in case_dates1:
        case_dates.append(elem[:10])

    print(cases)
    print(case_dates)
    fig, ax = plt.subplots()
    ax.scatter(cases, case_dates)
    # x coodrinates
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_minor_locator(ticker.AutoLocator())

    #y coordinates
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_minor_locator(ticker.AutoLocator())
    plt.ylabel('Cases')
    plt.xlabel('Date')
    fig.set_figwidth(8)
    fig.set_figheight(10)
    return ax

