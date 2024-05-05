import requests
import my_classes


# Define the URL of the API
url = "http://127.0.0.1:5000/"

# Define the name you want to search for
name = "TestName"
email = "TestName@mail.at"

# Send a GET request to the API with the name as a query parameter
response = requests.get(url, params={"name": name})

# Print the response from the server
print(response.text)
