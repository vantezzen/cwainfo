# CWAInfo Client Software

Dieser Teil des Projekts läuft auf den Raspberry Pi's, welche Informationen über die Corona-Warn-App Nutzer in der Gegend sammeln

## Installation

1. Setze Raspberry Pi OS inkl. einer Internetverbindung auf
1. Wechsel via `sudo su` zu root. Auf Grund von Permission-Einschränkungen bei Bluetooth LE kann nur root BLE Geräte scannen.
1. Klone diesen Teil der Repository auf den Raspberry Pi
1. Installiere die System-Dependencies mit:
```bash
sudo apt-get install gpsd gpsd-clients
sudo killall gpsd

# Kopiere hier die ID des GPS Moduls
# in meinem Fall "usb-u-blox_AG_-_www.u-blox.com_u-blox_7_-_GPS_GNSS_Receiver-if00"
sudo ls /dev/serial/by-id/

sudo nano /etc/default/gpsd
# Setze in dieser Datei "DEVICES=""" auf "/dev/serial/by-id/[ID des GPS Gerätes]"

sudo service gpsd start
```
1. Installiere die Dependencies über `pip3 install -r requirements.txt`
1. Passe `config.ini` an
1. Prüfe, dass die GPS-Verbindung funktioniert, durch `python3 gps_test.py`
1. Füge folgende Zeile über `crontab -e` als Cronjob hinzu:
```
*/5 * * * * python3 ~/cwainfo/client/main.py >/dev/null 2>&1
```
