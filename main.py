from sensor.logger import logging
import sys,os
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe


if __name__=="__main__":
     try:
          get_collection_as_dataframe(database_name="aps", collection_name="sensor")
     except Exception as e:
          print(e)