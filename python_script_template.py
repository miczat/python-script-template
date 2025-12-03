"""
A template for single-file Python scripts using arcpy, with logging and error handling


Args:
    parameter: description
    parameter: description

Preconditions:
    Statements that must be true before running the program.


Postconditions
    Statements that will be true after running the program.


Returned values
    What is returned by the program, if anything.

Issues and known limitations:
    Writen for Python 3.11.11 as shipped with ArcGIS Pro 3.5.3

Dev Notes:
    Remote origin: https://github.com/miczat/python-script-template

    Terminology, with pathlib name:
       image_path   =  C:\TEMP\A.JPG     # full path 'p'
       image_folderpath =  C:\TEMP       # p.parent
       image_foldername =  TEMP          # p.parent.name
       image_filename   =  A.JPG         # p.name
       image_name       =  A             # p.stem
       image_extension  =  JPG           # p.suffix   
     
"""
__author__ = "Mic Zatorsky"
__version__ = '2.0'
LAST_UPDATED = "2025-12-03"


import arcpy  # pyright: ignore[reportMissingImports]
from arcpy import env # pyright: ignore[reportMissingImports]
from arcpy.sa import * # pyright: ignore[reportMissingImports]
import logging
import os
import datetime
import sys
import traceback
import csv
from pathlib import Path    


start_time = datetime.datetime.now()
log = logging.getLogger()

# -----------------------------------------
# run config
# -----------------------------------------
log_name = r"program name here"
log_folder = r"."


# input parameters

# output parameters

# other config

# set the geoprocessing environment
arcpy.env.workspace = r'c:\Temp'   # fGDB or folder
arcpy.env.overwriteOutput = True   # avoids having to test for existence and delete
arcpy.env.addOutputsToMap = False

# Update with the default CRS you want to use
sr_GDA2020_MGA_Zone_56 = arcpy.SpatialReference(28356) 
arcpy.env.outputCoordinateSystem = sr_GDA2020_MGA_Zone_56

# for raster analysis 
arcpy.env.extent = None
arcpy.env.snapRaster = None


# -----------------------------------------
# create and configure the logger
# -----------------------------------------
def setup_logger(log_folder):
    logfile_ext = '.log.csv'
    logfile = os.path.join(log_folder, log_name + logfile_ext)

    """Configures a logger
    
    :param logfile: the name of a logfile that will be written
    :returns None
    :raises PermissionError: if the logfile is open in another app
    :raises IOError: if the logfile can't be written for another reason
    """

    # A formatter for use by all handlers
    d = ","   # log column delimiter
    log_msg_format_str = f'%(asctime)s{d}%(levelname)s{d}%(filename)s{d}%(funcName)s{d}"%(message)s"'
    datetime_fmt_str = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(log_msg_format_str, datetime_fmt_str)

    # Create a file handler which logs debug messages
    try:
        fh = logging.FileHandler(filename=logfile, mode='a')
    except PermissionError as pe:
        print("The log file could not be written due to permissions. "
              "Check if it is open in Excel or another app. Program stopping.")
        print(repr(pe))
        raise
    except OSError as oe:
        print("Some other I/O-related error occurred. Program stopping.")
        print(repr(oe))
        raise
    except Exception as e:
        print('An error occurred. Program stopping')
        print(repr(e))
        raise

    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    log.setLevel(logging.DEBUG)    # or INFO to be less verbose


# -----------------------------------------
# get row count
# -----------------------------------------
def get_row_count(table_or_layer) -> int:
    """Return the number of rows in a table or feature layer.

    Args:
        table_or_layer: Table or feature layer path, name, or object accepted
            by arcpy.GetCount_management. This can be, for example, a feature
            class path, an in-memory layer name, or a layer object.

    Returns:
        int: Number of rows in the input dataset.

    Raises:
        arcpy.ExecuteError: If the underlying geoprocessing tool fails.
        RuntimeError: If ArcPy is not initialized or the workspace is invalid.
    """
    row_count = int(arcpy.GetCount_management(table_or_layer)[0])
    log.debug(f"{row_count} rows in {table_or_layer}")
    return row_count



# -----------------------------------------
# main
# -----------------------------------------

def main():
    """main"""
    log.info('Start')
    log.info(f"Script version {__version__}, by {__author__} last updated {LAST_UPDATED}")
    log.info(f'Using Python version {sys.version}')

    # Productive code goes here
    try:
        log.info('Trying...')
        # do stuff

    except arcpy.ExecuteError as ee:
        log.error('The file may not exist. Program stopping')
        error_value = sys.exc_info()[1]
        log.error(error_value.args[0].replace(',', ' ').strip().replace('\r', '').replace('\n', ''))
        sys.exit()

    except Exception as e:
        error_value = sys.exc_info()[1]
        error_traceback = sys.exc_info()[2]
        tbinfo = traceback.format_tb(error_traceback)[0]
        log.error("SOMETHING ELSE WENT WRONG")
        log.error(error_value.args[0].replace(',', ' ').strip().replace('\r', '').replace('\n', ''))
        log.error(tbinfo.replace(',', ' ').strip().replace('\r', '').replace('\n', ''))
        raise

    # wrap up
    log.info('Finished')
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    log.info(f'Duration          {duration}')

    # close the log to release locks
    log.debug('Closing log')
    log_handlers_list = list(log.handlers)
    for h in log_handlers_list:
        log.removeHandler(h)
        h.flush()
        h.close()


# program entry point when called from the command line
if __name__ == '__main__':
    setup_logger(log_folder)
    main()