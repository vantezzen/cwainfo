import requests
import json

class Uploader:
  def upload(self, config):
    print("Trying to upload files")
    server = config['Uploader']['server'];
    r = requests.get(server + "/ping")
    if r.text != "pong":
      print("Server didn't return the correct response")
      return

    with open('datapoints.txt', 'r') as f:
      for line in f:
        if len(line.strip()) > 0:
          print("Uploading a datapoint")
          payload = json.loads(line)
          payload['key'] = config['Uploader']['pushkey']
          requests.post(server + "/push", data = payload)
    
    with open("datapoints.txt", "a") as f:
      f.truncate(20)

    print("Upload done")
