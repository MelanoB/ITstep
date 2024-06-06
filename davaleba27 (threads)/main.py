import json
import threading

file_names = ["data1.json", "data2.json", "data3.json"]

def read_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(f"{file_name}: {json.dumps(data, indent=4)}")

threads = []
for file_name in file_names:
    thread = threading.Thread(target=read_json, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()