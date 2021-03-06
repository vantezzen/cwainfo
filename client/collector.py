from bluepy import btle
from bluepy.btle import ScanEntry
from gps import *
import json
import time

class Collector:
  # Corona Interest Group Identifier as described in Google's whitepaper
  # See https://blog.google/documents/70/Exposure_Notification_-_Bluetooth_Specification_v1.2.2.pdf , Page 4
  CORONA_INTEREST_GROUP = "fd6f"

  def __init__(self):
    self.scanner = btle.Scanner(0)
    self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

  def getPosition(self):
    # 6 tries to get the GPS location
    for run in range(6):
      nx = self.gpsd.next()
      if nx['class'] == 'TPV':
        break;  
    
    latitude = getattr(nx,'lat', "0")
    longitude = getattr(nx,'lon', "0")
    return [latitude, longitude]
    
  def scan(self, t=5):
    scan_entries = self.scanner.scan(t)
    received_beacons = 0

    for scan_entry in scan_entries:
      service = scan_entry.getValueText(ScanEntry.COMPLETE_16B_SERVICES)
      # print("Service: " + str(service))
      if (service != None and service[4:8] == self.CORONA_INTEREST_GROUP):
        received_beacons += 1;

    return received_beacons
    
  def collect(self, config):
    print("Collecting data...")
    devices = self.scan()
    print("Result: " + str(devices) + " device(s)")

    [latitude, longitude] = self.getPosition()
    print("At position: " + str(latitude) + ", " + str(longitude))

    currentTime = time.time()
    dataset = {
      "number": devices,
      "lon": longitude,
      "lat": latitude,
      "timestamp": currentTime,
    }

    with open("datapoints.txt", "a") as file:
      json.dump(dataset, file)
      file.write("\n")
    