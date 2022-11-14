### Walkability Data Dictionary

The features included in this dictionary are all that remained after data cleaning. A full data dictionary of all features can be found [here](/epa_sld_3.0_technicaldocumentationuserguide_may2021.pdf)

| field          | data type   | description                                       |
| -------------- | ----------- | ------------------------------------------------- |
|place|object|city name|
|state|object|state name (or district, in the case of Washington, DC)|
|auto_accss_idx|float|proportion of working-age people who are able to reach their destinations via personal vehicle (theirs or someone else's)|
|pct_no_vehicle|float|percent of households that own zero vehicles|
|pct_one_or_more_vehicles|float|percent of households that own one or more vehicles|
|transit_accss_idx|float|proportion of working-age people who are able to reach their destinations via public transit|
|walkability_idx|float|walkability index comprised of weighted ranks against all other 50 states|
