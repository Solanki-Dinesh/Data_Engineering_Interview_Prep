# GET is one of the most common HTTP methods you’ll use when working with REST APIs.
# This method allows you to retrieve resources from a given API.
# GET is a read-only operation, so you shouldn’t use it to modify an existing resource.

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.status_code)
print(response.json())


# POST
# Now, take a look at how you use requests to POST data to a REST API to create a new resource.
# You’ll use JSONPlaceholder again, but this time you’ll include JSON data in the request.
# Here’s the data that you’ll send:

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.status_code)
print(response.json())


# PUT
# Beyond GET and POST, requests provides support for all the other HTTP methods you would use with a REST API.
# The following code sends a PUT request to update an existing to do with new data.
#  Any data sent with a PUT request will completely replace the existing values of the to do.

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())


# PATCH
# Next up, you’ll use requests.patch() to modify the value of a specific field on an existing to do.
# PATCH differs from PUT in that it doesn’t completely replace the existing resource.
# It only modifies the values set in the JSON sent with the request.

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json())


# DELETE
# Last but not least, if you want to completely remove a resource, then you use DELETE.
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())


# import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# Get the HTTP Response Code
# r.status_code
# Get HTTP Response Body
# r.text


# RPC (Remote Procedure Call)
