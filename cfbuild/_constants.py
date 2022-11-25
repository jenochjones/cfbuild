import csv
import io

from importlib import resources


WARNING_MESSAGE = '!!!CHANGE ME!!! - '

NEW_VARIABLE_NAME = WARNING_MESSAGE + 'new variable name'

TABLE_AND_CONSTANTS_LOCATION = 'tables_and_constants/'

CONVENTION_VERSIONS = ['CF-1.9', 'ACDD-1.3']

CF_FEATURE_TYPES = ['point', 'timeSeries', 'trajectory', 'profile', 'timeSeriesProfile', 'trajectoryProfile']

DATA_TYPES = ['uint8', 'uint16', 'uint32', 'ufloat32', 'ufloat64', 'int8', 'int16',
              'int32', 'float32', 'float64', 'str', 'char', '|S1', '|S2']

CELL_METHODS_VALUES = ['point', 'sum', 'maximum', 'maximum_absolute_value', 'median', 'mid_range', 'minimum',
                       'minimum_absolute_value', 'mean', 'mean_absolute_value', 'mean_of_upper_decile', 'mode',
                       'range', 'root_mean_square', 'standard_deviation', 'sum_of_squares', 'variance']

OPENDAP_RESERVED_KEYWORDS = ['alias', 'array', 'attributes', 'byte', 'dataset', 'error', 'float32', 'float64',
                             'grid', 'int16', 'int32', 'maps', 'sequence', 'string', 'structure', 'uint16', 'uint32',
                             'url', 'code', 'message', 'program_type', 'program']

LIST_OF_VARIABLE_NAMES = ['Time Coordinate', 'Z Coordinate', 'Y Coordinate', 'X Coordinate', 'Coordinate',
                          'Auxiliary Coordinate', 'Scalar Coordinate', 'Grid Mapping Variable', 'Domain Variable',
                          'Boundary Variable', 'Cell Measures Variable', 'Georeferenced Data Variable',
                          'Data Variable', 'Ancillary Data Variable', 'Unknown']

VARIABLE_TYPE_INDICATORS = {
    'C': 'Coordinate',
    'T': 'Time Coordinate',
    'X': 'X Coordinate',
    'Y': 'Y Coordinate',
    'Z': 'Z Coordinate',
    'AC': 'Auxiliary',
    'GD': 'Georeferenced Data',
    'D': 'Data',
    'AD': 'Ancillary Data',
    'S': 'Scalar',
    'G': 'Grid Mapping',
    'DO': 'Domain',
    'B': 'Boundary',
    'CM': 'Cell Measures',
    'M': 'Geometry Container',
    'U': 'Unknown'
}

COORDINATE_VARIABLE_LIST = ['Coordinate', 'Time Coordinate', 'X Coordinate', 'Y Coordinate', 'Z Coordinate']

UNITS = {
    'degrees_north': 'Y',
    'degree_north': 'Y',
    'degree_N': 'Y',
    'degrees_N': 'Y',
    'degreeN': 'Y',
    'degreesN': 'Y',
    'degrees_east': 'X',
    'degree_east': 'X',
    'degree_E': 'X',
    'degrees_E': 'X',
    'degreeE': 'X',
    'degreesE': 'X'
    }

STANDARD_NAMES = {
    'grid_latitude': 'Y',
    'latitude': 'Y',
    'projection_y_angular_coordinate': 'Y',
    'projection_y_coordinate': 'Y',
    'grid_longitude': 'X',
    'longitude': 'X',
    'projection_x_angular_coordinate': 'X',
    'projection_x_coordinate': 'X',
    'altitude': 'Z',
    'height': 'Z',
    'time': 'T'
    }


def _convert_csv_to_dict(filepath):
    with open(filepath, mode='r') as csv_file:
        rows = csv.reader(csv_file)

        attribute_dict = {}

        for row_index, row in enumerate(rows):
            print(attribute_dict)
            if row_index <= 0:
                header_list = row
                print(header_list)
            else:
                for entry_index, entry in enumerate(row):
                    if entry_index <= 0:
                        attribute_dict[row[0]] = {}
                    else:
                        if header_list[entry_index] == 'value':
                            entry = WARNING_MESSAGE + entry
                        attribute_dict[row[0]][header_list[entry_index]] = entry

    return attribute_dict


def _convert_xml_to_dict(filepath):
    with resources.open_binary('cfbuild', filepath) as file_path:
        table = file_path.read()
    xml_table = io.BytesIO(table)
    return xml_table
