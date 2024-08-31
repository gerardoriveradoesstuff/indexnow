import requests
import json

# Define the URL and headers for the POST request
url = "https://api.indexnow.org/indexnow"
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

# Prepare the JSON payload
payload = {
    "host": "www.enzototalconstruction.com",
    "key": "eddeaa3fc1bd436d9152859190adf280",
    "keyLocation": "https://www.enzototalconstruction.com/eddeaa3fc1bd436d9152859190adf280.txt",
    "urlList": [
        "https://www.enzototalconstruction.com/menu/allserv.html",
        "https://www.enzototalconstruction.com/menu/hi.html",
        "https://www.enzototalconstruction.com/menu/maint.html",
        "https://www.enzototalconstruction.com/menu/out.html",
        "https://www.enzototalconstruction.com/menu/qoute.html",
        "https://www.enzototalconstruction.com/menu/util.html",
        "https://www.enzototalconstruction.com/pages/about.html",
        "https://www.enzototalconstruction.com/pages/contact.html",
        "https://www.enzototalconstruction.com/pages/faq.html",
        "https://www.enzototalconstruction.com/pages/gallery.html",
        "https://www.enzototalconstruction.com/pages/jobs.html",
        "https://www.enzototalconstruction.com/pages/partners.html",
        "https://www.enzototalconstruction.com/pages/privacy.html",
        "https://www.enzototalconstruction.com/pages/projects.html",
        "https://www.enzototalconstruction.com/pages/terms.html",
        "https://www.enzototalconstruction.com/services/bathroomremodel.html",
        "https://www.enzototalconstruction.com/services/concrete.html",
        "https://www.enzototalconstruction.com/services/electricalandplumbing.html",
        "https://www.enzototalconstruction.com/services/hardscaping.html",
        "https://www.enzototalconstruction.com/services/janitorialservices.html",
        "https://www.enzototalconstruction.com/services/kitchenremodel.html",
        "https://www.enzototalconstruction.com/services/landscapingservices.html",
        "https://www.enzototalconstruction.com/services/poolservices.html",
        "https://www.enzototalconstruction.com/services/roomaddition.html",
        "https://www.enzototalconstruction.com/services/services.html"
    ]
}

# Convert the payload to a JSON string
data = json.dumps(payload)

# Send the POST request
response = requests.post(url, headers=headers, data=data)

# Print the status code
print(f"Status Code: {response.status_code}")

# Try to parse the response as JSON
try:
    response_json = response.json()
    print(response_json)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format:")
    print(response.text)
