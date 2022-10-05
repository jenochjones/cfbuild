#CFBUILD

##Building CF Compliant netCDF files
This package is designed to help update or build netCDF datasets so that 
they are compliant with the Attribute Conventions for Data Discovery (ACDD)
and the Climate and Forecast (CF) Conventions. It is built to work with multidimensional
geo-referenced datasets but may be used on any netCDF file. No guarantee is given as to 
the accuracy of the updated datasets and user discretion is advised.

###Installation
To install cfbuild run "pip install cfbuild" in your terminal.

###Dependencies
* netCDF4
* pyproj
* cfunits
* isodate
* lxml

###Documentation and Demos
Read the documentation here: url

###Classes and Functions

`cfbuild.Dataset(dataset_or_filepath, conventions)`
> dataset_or_filepath: str - An OPeNDAP url or the path to a netCDF file.<br>
> conventions: str or list - One or both of ['CF-1.9', 'ACDD-1.3'].
> 
> >`cfbuild.to_ncml(output_filepath)`<br>
> >output_filepath: str - A filepath where an ncml file will be created which 
> >describes the cfbuild dataset<br>
> >`cfbuild.crs(epsg_number)`<br>
> >epsg_number: str or int - An EPSG number that defines the coordinate reference system for the dataset.<br>
> >`cfbuild.close()`<br>
> > Close the dataset.<br>
> >`group(name)`<br>
> >name: str - The name of the group to be created in the cfbuild dataset.<br>
> >`variable(name, data_type, dimensions, variable_type, values)`<br>
> >name: str - The name of the variable to be created in the cfbuild dataset.<br>
> >data_type: str - The data type of the variable.<br>
> >dimensions: tuple - The dimensions associated with the variable.<br>
> >variable_type: str - The Climate and Forecast Convention variable type for the variable. One of Coordinate,
Time Coordinate, X Coordinate, Y Coordinate, Z Coordinate', Auxiliary Coordinate',
Georeferenced Data Variable, Data Variable, Ancillary Data Variable,
Scalar Coordinate, Grid Mapping Variable, Domain Variable, Boundary Variable, Cell Measures Variable.<br>
> >values: numpy.array - An array of values for the variable.<br>
> >`dimension(name, length)`<br>
> >name: str - The name of the dimension to be created in the cfbuild dataset.<br>
> >length: int or None - The length of the dimension. Use None for an unlimited dimension.<br>
> >`attribute(name, value)`<br>
> >name: str - The name of the attribute to be created for dataset.<br>
> >value: str - The value of the attribute.<br>

`cfbuild.NCML(ncml_filepath, dataset)`
> ncml_filepath: str - A path to an ncml file used to configure the new dataset.<br>
> dataset: cfbuild.Dataset - A dataset created using cfbild.Dataset().
> >`to_nc(nc_filepath, write_mode)`<br>
> >nc_filepath: str - A path to the new netCDF dataset that will be created.
> >writ_mode: str - w or clobber. w will write to a new dataset but will raise an error if a dataset with the same name 
> >already exists. clobber uses the netCDF4 clobber function.
 
`cfbuild.NCML(ncml_filepath, dataset)`
> ncml_filepath: str - A path to an ncml file used to configure the new dataset.<br>
> dataset: cfbuild.Dataset - A dataset created using cfbild.Dataset().
> >`to_nc(nc_filepath, write_mode)`<br>
> >nc_filepath: str - A path to the new netCDF dataset that will be created.
> >writ_mode: str - w or clobber. w will write to a new dataset but will raise an error if a dataset with the same name 
> >already exists. clobber uses the netCDF4 clobber function.

###Tutorial

####Build a dataset
Import the necessary packages
```
import cfbuild
import numpy as np
```

Create a new dataset. Add dimensions and variables to the dataset.
```
ds = cfbuild.Dataset('path/to/netCDF_file.nc', ['CF-1.9', 'ACDD-1.3'])

time_dimension = ds.dimension('time', None)
lat_dimension = ds.dimension('lat', 180)
lon_dimension = ds.dimension('lon', 360)

time_variable = ds.variable('time', ('time',),
```

####Update a dataset
Import the necessary packages
```
import cfbuild
```





* f
* f
* f
* f
* f
* f
* f
* f
* f
* f
* f
* f
* f
* f




