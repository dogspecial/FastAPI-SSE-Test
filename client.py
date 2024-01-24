import json
import requests

url = "http://127.0.0.1:8081/st"


def get_event():
    with requests.get(url, stream=True) as stream:
        for chunk in stream.iter_lines():
            yield json.loads(chunk.decode("utf-8"))


for event in get_event():
    print(event)