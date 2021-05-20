from bluepy import btle
from bluepy.btle import ScanEntry

class Collector:
  # Corona Interest Group Identifier as described in Google's whitepaper
  # See https://blog.google/documents/70/Exposure_Notification_-_Bluetooth_Specification_v1.2.2.pdf , Page 4
  CORONA_INTEREST_GROUP = "fd6f"

  def __init__(self):
    self.scanner = btle.Scanner(0)
    
  def scan(self, t=5):
    scan_entries = self.scanner.scan(t)
    received_beacons = 0

    for scan_entry in scan_entries:
      service = scan_entry.getValueText(ScanEntry.COMPLETE_16B_SERVICES)
      service_identifier = service[4:8]
      if (service_identifier == self.CORONA_INTEREST_GROUP):
        print("Found")
        received_beacons += 1;

    # for scan_entry in scan_entries:
    #   service = scan_entry.getValueText(ScanEntry.COMPLETE_16B_SERVICES)
    #   if service == self.CORONA_SERVICE:
    #     data = scan_entry.getValueText(ScanEntry.SERVICE_DATA_16B)
    #     if (
    #       # Service data should always be 88 bytes long as it contains UUiD, RPI and AEM
    #       len(data) == 44

    #       # Make sure the interest group is the Corona Interest Group
    #       and int(data[0:2], 16) + int(data[2:4], 16) * 0x100 == self.CORONA_INTEREST_GROUP):
    #       received_beacons += 1;

    print("Received: " + str(received_beacons))
    return received_beacons
    
  def collect(self, config):
    print("Collecting data...")
    devices = self.scan()
    