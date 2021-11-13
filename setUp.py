import time
sleep = time.sleep
import requests

print("Welcome to the Enviro Node set up! How about we begin?")
sleep(2)
print("First, we need to install some dependencies")
print("[Pretend] Istailling xyz")
print("What would like the node to called?")
print("We surgest something simply and easy to identify like 'DWP-Leeds-QuarryHouse-4flr-East'")
nodeName = input("Node name: ")
print("Provide a deciptyion for the Node, Where it is located? Why you are part of the project?")
nodeDescription = input("Node description: ")
print("Please provide the maintainers email address")
maintainerEmail = input("Maintainer email: ")
print("Where is node setup?")
address = input("Address: ")
print("These are the details you have provided:")
print("Node name: " + nodeName)
print("Node description: " + nodeDescription)
print("Maintainer email: " + maintainerEmail)
print("Address: " + address)
print("Is this correct?")
confirmation = input("(y/n): ")
if confirmation == "y":
    nodeData =  {"name": nodeName, "description": nodeDescription, "maintainer_email": maintainerEmail, "address": address}
    response = requests.post("http://localhost:3000/node", json=nodeData)
    print("Status Code:", response.status_code)

    response_Json = response.json()
    print("Printing Post JSON data")
    print(response_Json)

    if response.status_code == 200:
        print("Node created successfully")
    else:
        print("Something went wrong")