from firebase import firebase
import random

auth_url = 'https://bmake2020-7dae9.firebaseio.com/'

class Firebase:
    def __init__(self, id):
        self.db = firebase.FirebaseApplication(auth_url, None)
        self.id = id
    
    def update_loc(self, lat, lng):
        self.db.post('/drones/drone' + str(self.id) + 'lat', lat)
        self.db.post('/drones/drone' + str(self.id) + 'lng', lng)

    def add_fire(self, lat, lng, id): 
        self.db.post('/fireLocations/fire'+ str(id) + '/lat', lat)
        self.db.post('/fireLocations/fire' + str(id) + '/lng', lng)
        
 


