
def airport_list (airlist):
    airport_str = ""
    for airport in airlist:
        airport_str+=str(airport+",")
    return(airport_str[:-1]+";")
    
def initial_airport(airlist):
    return("f="+airport_list(airlist))
    
def final_airport(airlist):
    return("t="+airport_list(airlist))
    
def flight_date(date):
    day = str(date.day).zfill(2)
    month = str(date.month).zfill(2)
    year = str(date.year)
    return(year+"-"+month+"-"+day+";")
    
def start_date(date):
    return("d="+flight_date(date))
    
def return_date(date):
    return("r="+flight_date(date))

def search_link(start_airlist, end_airlist, d_date, r_date):
    flights_web = "https://www.google.com/flights/#search;"
    return(flights_web+initial_airport(start_airlist)+final_airport(end_airlist)+start_date(d_date)+return_date(r_date))
    