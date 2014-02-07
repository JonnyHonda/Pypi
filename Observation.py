__author__ = 'johnburrin'

class observation:

    """
        this objects represents a map of a line of data in pywws raw data file
    """

    idx = None              # String - Date string
    delay = None            # Integer - delay?
    hum_in = None           # Integer - indoor humidity
    temp_in = None          # Float - indoor temperature
    hum_out = None          # Integer - outdoor humidity
    temp_out = None         # Float - outdoor temperature
    abs_pressure = None     # Float - air pressure (at sea level - mslp)
    wind_ave = None         # Float - average wind speed
    wind_gust = None        # Float - wind gust speed
    wind_dir = None         # Integer - wind direction 22 degree intervals
    rain = None             # Float - rainfall in mm
    status = None           # Integer - ?