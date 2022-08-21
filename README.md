# CWAInfo (Corona-Warn-App Info)

This code was created as part of of a university course about wireless networks.

## Client

The client under `/client` provides a script to count the number of devices using the german Corona Warn App (https://www.bundesregierung.de/breg-de/themen/corona-warn-app) and save it together with the current GPS position.

Collected data will be uploaded to a central server or buffered into a local file while the device can't connect to the server to prevent loosing data.

## Server

The server under `/server` provides a basic API to store data points collected by the client into a SQL database.

## Grafana 

The Grafana panel configuration in `/grafana` can be used to turn the data saved in the database into a heatmap.

