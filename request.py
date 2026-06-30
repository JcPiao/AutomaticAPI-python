import requests

url_get = "http://127.0.0.1:28080/admin/login"

url_login = "http://127.0.0.1:28080/api/admin/login"

get_r = requests.get(url = url_get)

#print the get response text and status code
# print(r.text)
# print(r.status_code)

post_data = {
    "userName": "admin",
    "password": "123456",
    "https": False
}

post_r = requests.post(url = url_login, json = post_data, verify = False)

#print the post response text and status code
print(post_r.text)
print(post_r.status_code)