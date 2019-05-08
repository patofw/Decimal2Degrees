def dec2degreeLatLon(lat, lon):
    """ Transforms a pair of latitudes and longitudes to DMS format"""

    # Transforming into degrees, minutes, seconds
    
    if (abs(lat) > 90 )|( abs(lon) >180):
        return None
    
    else: 
        dms_lat = dec2degrees(lat)
        dms_lon = dec2degrees(lon)

        # account for E/W & N/S
        if lon < 0:
            EorW = "(W)"
        else:
            EorW = "(E)"

        if lat < 0:
            NorS = "(S)"
        else:
            NorS = "(N)"
        # Creating the string for the output
        str_lat = str(abs(dms_lat[0])) + "°" + str(
            dms_lat[1]) + "'"+ str(dms_lat[2]) +  NorS
        str_lon = str(abs(dms_lon[0])) + "°" + str(
            dms_lon[1]) + "'" + str(dms_lon[2]) + EorW

    

    return (str_lat,str_lon)


def dec2degrees(dd):
    """ Transforms any decimal to degrees"""
    
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (int(degrees),int(minutes),round(seconds))



def dms2degree(latitude,longitude):
    """
     Transforms DMS format [11°16'(N)] to decimal     
    """
    #filter for none values 
    if  pd.isna(latitude):
        latitude = np.nan
        longitude = np.nan
    else:
        try: 
            N = 'N' in latitude 
            d, m = map(str, latitude[:-1].split('°'))
            m = [int(s) for s in m.split("'") if s.isdigit()][0]
            d = int(d)
            latitude = (d + (m / 60.)) * (1 if N else -1)

            #longitude = "26°39'(W)"
            W = 'W' in longitude
            d, m = map(str, longitude[:-1].split('°'))
            m = [int(s) for s in m.split("'") if s.isdigit()][0]
            d = int(d)
            longitude = (d + (m / 60.)) * (-1 if W else 1)
        except: 
            return None


    return latitude, longitude
    
    
### Example #####

#import pandas as pd

#lat = 70.199
#lon = -40.22

#coords = dec2degreeLatLon(lat, lon)
#print(coords)
## prints --> ("70°11'56(N)", "40°13'12(W)")
#decs = dms2degree(coords[0],coords[1])
#print(decs)
## prints ---> (70.18333333333334, -40.21666666666667)
    
    
    
