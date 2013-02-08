README
======

CAUTION! This repository is very large 

The City of Chicago is releasing selected datasets from the [data portal](http://data.cityofchicago.org 'Chicago Data Portal') under the MIT License (see below). This repository contains:

1. Data in a GeoJSON format.
2. Examples of importing data into R, Python, and Ruby.
3. Instructions to transform data from the data portal to data in the repository.

Working with GeoJSON Data
=========================

The data was released as a [GeoJSON](http://www.geojson.org/geojson-spec.html) file. Below are some simple instructions which will show you how to load GeoJSON in R, Python, and Ruby.

R
---

Find an example script [here](/examples/Importing%20GeoJSON%20R%20Demo.R 'Importing GeoJSON data to R'). This example will import the data in R and create a couple of maps.

Instructions:

1. Set the working directory to the location of the downloaded repository.
    ```r
    setwd("path\\to\\osd-building-footprints")
    ```

2. Install the "rgdal" library to let R read and translate the data from GeoJSON to a Shapefile. We will use "ggplot2" library to transform the spatial data frame to a regular data frame--and to make a map.
    ```r    
    install.packages(c("rgdal","ggplot2"))
    ```

3. Load the libraries:
    ```r    
    library(rgdal)
    library(ggplot2)
    ```

4. Import data to a spatial dataframe. City data is typically created using the transverse Mercator projection.
    ```r
    ogrInfo("data\\Buildings.json", layer="OGRGeoJSON")
    buildings.shapefile <- readOGR(dsn="data\\Buildings.json", layer="OGRGeoJSON", p4s="+proj=tmerc +ellps=WGS84")
    ```

5. Lets convert the spatial dataframe to a typical dataframe.
    ```r
    buildings.table <- fortify(buildings.shapefile)
    ```

6. Review the new dataframe.
    ```r
    head(buildings.table)
    ```

7. Plot the data.
    ```r
    ggplot(buildings.table, aes(x=long, y=lat, group=group)) + geom_polygon()
    ```

Here is the output you should expect from the plot() command:
![plot(buildings.shapefile)](/examples/R-plot-buildings.png)

Here is the output you should expect from the ggplot() command:
![ggplot(buildings.df, aes(x=long, y=lat, group=group))+geom_path()](/examples/R-ggplot-buildings.png)
    
Python
------

Find an example script [here](/examples/Importing%20GeoJSON%20Python%20Demo.py 'Importing GeoJSON data to Python Demo').

1. Load the necessary json and pprint libraries.
	```python
	import json
	```

2. Open GeoJSON data file.
	```python
	buildings_json = open('PATH/TO/osd-building-footprints/data/Buildings.json', 'r')
	```

3. Check first few lines of data (repeat this command several times)
    ```python
    buildings.readline()
    ```

4. Load GeoJSON file.
	```python
	buildings = json.load(buildings_json)
	```

5. Close the open GeoJSON file.
	```python
	json.close(buildings_json)
	```

Ruby
----

An example ruby script is provided to show loading GeoJSON and running spatial analysis using the RGeo suite. A simple Gemfile is provided to make getting the dependencies and using them easy.

        $ cd PATH/TO/osd-building-footprints/examples/ruby
        $ bundle
        $ ruby example.rb

This example script filters the `Buildings.json` to street segments within a 500ft buffer of 50 W Washington.

Differences between data portal and this repository
===================================================

Though the data in this repository is also available on Chicago's data portal, the data in this repository is different in several ways. First, the data within this repository is released under the MIT License. Second, this data has been edited to remove internal codes which do not provide useful information. Third, after changes were made to the dataset, the original shapefile was converted to GeoJSON using [GDAL's](http://www.gdal.org/, 'Geospatial Data Abstraction Library') [ogr2ogr](http://www.gdal.org/ogr2ogr.html)

The translation from portal to repository involves several steps. First, the original DBF file is transformed using OpenRefine to elminate unhelpful columns and clean data. The "Transformatons" folder contains the corresponding JSON, which contains the detailed list of changes made to the original table.

The resulting shapefile is then translated to GeoJSON using the ogr2ogr from the GDAL application. The transformation is completed in the command prompt:

ogr2ogr -f "GeoJSON" Buildings_ogr.json /path/to/portal/data/Buildings.shp

Unfortunately, ogr2ogr outputs in machine, but not human-readable files. At this time, we have not translated this to a more human readable form due to the large file size.

The folder "Transformations" contains the necessary code to transform data on the portal to the release in this repository.

License
=======
This data is released under the [MIT License](http://opensource.org/licenses/MIT 'MIT License'). See LICENSE.txt.