### Weather Data Dictionary

The features included in this dictionary are the combined features from the temperature and rain datasets, with seasonal trend features added.

| field          | data type   | description                                       |
| -------------- | ----------- | ------------------------------------------------- |
|place|object|city name|
|state|object|state name (or district, in the case of Washington, DC)|
|MONTH_avg_temp|float|average temperature in the given month (in fahrenheit)|
|MONTH_avg_rain|float|average rain in the given month (in inches)|
|winter_avg_temp|float|averaged temp of the dec, jan, and feb values|
|spring_avg_temp|float|averaged temp of the mar, apr, and may values|
|summer_avg_temp|float|averaged temp of the jun, jul, and aug values|
|autumn_avg_temp|float|averaged temp of the sep, oct, and nov values|
|winter_avg_rain|float|averaged rain of the dec, jan, and feb values|
|spring_avg_rain|float|averaged rain of the mar, apr, and may values|
|summer_avg_rain|float|averaged rain of the jun, jul, and aug values|
|autumn_avg_rain|float|averaged rain of the sep, oct, and nov values|
