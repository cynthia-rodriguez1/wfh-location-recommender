### Cost of Living Data Dictionary

The features included in this dictionary are all that remained after data cleaning.

| field          | data type   | description                                       |
| -------------- | ----------- | ------------------------------------------------- |
|name|object|city name|
|state|object|state name (or district, in the case of Washington, DC)|
|cost_of_living|float|overall cost of living index|
|grocery_cost_idx|float|grocery cost index|
|transportation_cost_idx|float|transportation cost index (includes gas, transit fare, etc.)|
|miscellaneous_cost_idx|float|miscellaneous cost index (includes clothing, restaurants, entertainment, repairs, etc.)|
|population|int|total population|
|median_age|float|median age in location|
|summer_comfort_index|float|summer climate comfort index|
|winter_comfort_index|float|winter climate comfort index|
|perc_growth_since_2020|float|population percent growth since 2020|
|political_left_lean|float|percent of total voting-age population that voted democrat in the 2020 presidential election|
|political_right_lean|float|percent of total voting-age population that voted republican in the 2020 presidential election|
