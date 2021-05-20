# CWAInfo Client Software

Dieser Teil des Projekts läuft auf den Raspberry Pi's, welche Informationen über die Corona-Warn-App Nutzer in der Gegend sammeln

## Installation

1. Setze Raspberry Pi OS inkl. einer Internetverbindung auf
1. Wechsel via `sudo su` zu root. Auf Grund von Permission-Einschränkungen bei Bluetooth LE kann nur root BLE Geräte scannen.
1. Klone diesen Teil der Repository auf den Raspberry Pi
1. Installiere die Dependencies über `pip3 install -r requirements.txt`
1. Passe `config.py` an
1. Füge folgende Zeile über `crontab -e` als Cronjob hinzu:
```
*/5 * * * * python3 ~/cwainfo/client/main.py >/dev/null 2>&1
```
