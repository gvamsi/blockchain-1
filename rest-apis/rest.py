from flask import Flask 
from flask import jsonify 
from flask import request
import json
from bson import ObjectId 
from flask_pymongo import PyMongo 

# USER DEFINED JSON ENCODER
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

# DB NAME AND CONNECTION
app.config['MONGO_DBNAME'] = 'aperio' 
app.config['MONGO_URI'] = 'mongodb://localhost:27017/aperio'

mongo = PyMongo(app)

# TEST ENDPOINT

@app.route('/')
def hello():
	return "OK"
@app.route('/data', methods=['GET'])
def get_data():
	db_name = mongo.db.users
	res = db_name.find_one()
	return JSONEncoder().encode(res)


# ADDING USER TO THE SYSTEM
@app.route('/addUser',methods=['POST'])
def add_User():
	db_name = mongo.db.users
	userName = request.json['userName']
	password = request.json['password']
	organization = request.json['organization']
	result = db_name.insert({'userName':userName , 'password':password , 'organization':organization})
	return JSONEncoder().encode(result)

# UPDATING USER TO THE SYSTEM
@app.route('/updateUser',methods=['POST'])


# ADDING CHANNEL TO THE NETWORK
@app.route('/addChannel',methods=['POST'])
def add_Channel():
	db_name = mongo.db.channel
	channelName = request.json['channelName']
	channelAdmin = request.json['channelAdmin']
	organizationsList = request.json['organizationsList']
	result = db_name.insert({'channelName':channelName , 'channelAdmin':channelAdmin , 'organizationsList':organizationsList})
	return JSONEncoder().encode(result)

# ADDING ADMIN ORGANIZATION TO THE NETWORK
@app.route('/addAdmin',methods=['POST'])
def add_Admin():
	db_name = mongo.db.organizations
	orgName = request.json['organizationName']
	channelName = request.json['channelName']
	noOfPeers = request.json['noOfPeers']
	peerNames = request.json['peerNames']
	properties = request.json['properties']
	admin = True
	result = db_name.insert({'organizationName':orgName, 'channelName':channelName, 'noOfPeers':noOfPeers, 'peerNames':peerNames, 'properties':properties, 'admin': admin})
	return JSONEncoder().encode(result)


# ADDING OTHER ORGANIZATION TO THE NETWORK
@app.route('/addOrg',methods=['POST'])
def add_Org():
	db_name = mongo.db.organizations
	orgName = request.json['organizationName']
	channelName = request.json['channelName']
	noOfPeers = request.json['noOfPeers']
	peerNames = request.json['peerNames']
	properties = request.json['properties']
	admin = False
	result = db_name.insert({'organizationName':orgName, 'channelName':channelName, 'noOfPeers':noOfPeers, 'peerNames':peerNames, 'properties':properties, 'admin': admin})
	return JSONEncoder().encode(result)


# ADDING  PEERS IN EACH ORGANIZATION
@app.route('/addPeers',methods=['POST'])
def add_Peers():
	db_name = mongo.db.peers
	channelName = request.json['channelName']
	peerName = request.json['peerName']
	organizationName = request.json['organizationName']
	properties = request.json['properties']
	result = db_name.insert({'channelName':channelName, 'peerName':peerName, 'organizationName':organizationName, 'properties':properties})
	return JSONEncoder().encode(result)

# MAIN FUNCTION CALL
if __name__ == '__main__':
  app.run()
