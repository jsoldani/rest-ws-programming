import requests

url = 'http://localhost:50000'
scores = '/scores'

player = 'jacopo'

# POST
# post default score for player
score = { 'player': player }
r = requests.post(url + scores, json=score)
# handle possible errors (by quitting)
if r.status_code == 409:
    print("POST_ERROR: score already included")
    exit(-1)
elif r.status_code != 201:
    print("POST_ERROR: status code " + r.status_code)
    exit(-1)
# get path of added score 
score_path = r.headers.get('Location')
# print message for completed post
print("POST: " + player + "'s score posted")

# GET 
# get representation of added score
r = requests.get(url + score_path)
# handle possible errors (by quitting)
if r.status_code == 404:
    print("GET_ERROR: score not found")
    exit(-1)
elif r.status_code != 200:
    print("GET_ERROR: status code " + r.status_code)
    exit(-1) 
# print body of reply
body = r.json()
print("GET: " + player + "'s score is " + str(body['score']))

# PUT
# update player's score
score = { 'score': 2000 }
r = requests.put(url + score_path, json=score)
# handle possible errors (by quitting)
if r.status_code == 404:
    print("GET_ERROR: score not found")
    exit(-1)
elif r.status_code != 200:
    print("GET_ERROR: status code " + r.status_code)
    exit(-1) 
# print body of reply
print("UPDATE: " + player + "'s score updated")

# GET 
# get representation of added score
r = requests.get(url + score_path)
# handle possible errors (by quitting)
if r.status_code == 404:
    print("GET_ERROR: score not found")
    exit(-1)
elif r.status_code != 200:
    print("GET_ERROR: status code " + r.status_code)
    exit(-1) 
# print body of reply
body = r.json()
print("GET: " + player + "'s score is " + str(body['score']))

# DELETE 
# delete representation score
r = requests.delete(url + score_path)
# handle possible errors (by quitting)
if r.status_code == 404:
    print("ERROR: score not found")
    exit(-1)
elif r.status_code != 200:
    print("ERROR: status code " + r.status_code)
    exit(-1) 
# print message of deleted score
print("DELETE: " + player + "'s score deleted")


