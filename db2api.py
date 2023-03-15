import http.client
import json
import pandas
from flask import Flask, jsonify, redirect, url_for, request
import numpy as np

app = Flask(__name__)

#credentials taken from db2
credentials = {
  "connection": {
    "cli": {
      "arguments": [
        [
          "-u",
          "yhc80422",
          "-p",
          "ztvWffHhMCYbmzXw",
          "--ssl",
          "--sslCAFile",
          "1dd14d0c-1b52-4f63-a606-53ecba28771d",
          "--authenticationDatabase",
          "admin",
          "--host",
          "8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30120"
        ]
      ],
      "bin": "db2",
      "certificate": {
        "certificate_base64": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURIVENDQWdXZ0F3SUJBZ0lVT3dvMC9va09CUEN5RjFWeFJxVGhKRW9ubDBVd0RRWUpLb1pJaHZjTkFRRUwKQlFBd0hqRWNNQm9HQTFVRUF3d1RTVUpOSUVOc2IzVmtJRVJoZEdGaVlYTmxjekFlRncweU1EQTRNRFF3TWpVMwpNalphRncwek1EQTRNREl3TWpVM01qWmFNQjR4SERBYUJnTlZCQU1NRTBsQ1RTQkRiRzkxWkNCRVlYUmhZbUZ6ClpYTXdnZ0VpTUEwR0NTcUdTSWIzRFFFQkFRVUFBNElCRHdBd2dnRUtBb0lCQVFEb0ZFNGQ0SGdOeXZMUVIwR3gKQTB0amRXQnM4NVBjTDNyRStjN1R3K2diRUdQSUxJU0VZV3o4Y1g1TG1XQk0rY1FnOG9VeSsrQXJ3OEoxaXdRZQpySmlIU2I1clF4WTM0c3BQeGRFVEZkWEhScnJhMGU2VmM4MW42TllJL0ZHSnl1Q3hrTG5GMUtFQW9hbHYwaDM2CnhDT0FvcXRwTlFrTzNpMTRGeU0yRDRiajkxckI4RGk4Vy9XMVpVdVhMNGwzZXVLZUVCeTRuZmhJV3kySVc3aUMKbGpMZ3RlN3hZTDVHbVpKOUdsYWtrSnJ1cnpNREFQLzVUYnRlUUIydElodTBRSVRFZHlESVFYUEZGRDBHYzloZAo3M29JdnpVZUJ3VC9uRHN3OTJNNC82SkdtZWpKN0lpdFBTN3Y2a2dlUVhINDlBaUVJNXpQdUVpVzNOYi9GR0pYCmY2a2JBZ01CQUFHalV6QlJNQjBHQTFVZERnUVdCQlR2RzZ2RU5MRjFVbWZnQ003MmxOcmMzSDI2bURBZkJnTlYKSFNNRUdEQVdnQlR2RzZ2RU5MRjFVbWZnQ003MmxOcmMzSDI2bURBUEJnTlZIUk1CQWY4RUJUQURBUUgvTUEwRwpDU3FHU0liM0RRRUJDd1VBQTRJQkFRQTgvdFVnUTZlaTZYWHZndDJ0dUdrbkpva1Y5UWNkaTNZbFVFWkNDUytjClVQZ3NnMnVBMldxcHlWTm1mRkhjcHZ1Vmp0VHRYTmk2NUM2WlZsRnYxc3p1cU9zdFB5bkJ4blN4cUs0dkc0dTkKVjBWRUgxcE1tZnZBSmxkV3c4UEJTZGJtTk1HdGM4SzlwT0o5OVdBQ1ZFRXVXVGdDeHJKTXFBZnpYUXlidUV0dwp0cW1pV2swTmVXNGk5ZEY4S2dTWUVaQWFodXVBSlRldXB2R2RPV1U0eEV4bm03aEVRbmZPV2ZITThDd08xNWFZClRGQ2s0Q0pDUmR4Mlg5U284V3o1Z3MzcncyRkFDQlJyZ0NYeFFDZnZrZTZUdVNHNkxFRHJHbmpWaXVSQkpZdW4KT1RxWXROaVBHaHpuTHJrL0Fzam1LMzBxQmFLTmFyNUdQajhqalpNb2RiZ04KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
        "name": "1dd14d0c-1b52-4f63-a606-53ecba28771d"
      },
      "composed": [
        "db2 -u yhc80422 -p ztvWffHhMCYbmzXw --ssl --sslCAFile 1dd14d0c-1b52-4f63-a606-53ecba28771d --authenticationDatabase admin --host 8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30120"
      ],
      "environment": {},
      "type": "cli"
    },
    "db2": {
      "authentication": {
        "method": "direct",
        "password": "ztvWffHhMCYbmzXw",
        "username": "yhc80422"
      },
      "certificate": {
        "certificate_base64": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURIVENDQWdXZ0F3SUJBZ0lVT3dvMC9va09CUEN5RjFWeFJxVGhKRW9ubDBVd0RRWUpLb1pJaHZjTkFRRUwKQlFBd0hqRWNNQm9HQTFVRUF3d1RTVUpOSUVOc2IzVmtJRVJoZEdGaVlYTmxjekFlRncweU1EQTRNRFF3TWpVMwpNalphRncwek1EQTRNREl3TWpVM01qWmFNQjR4SERBYUJnTlZCQU1NRTBsQ1RTQkRiRzkxWkNCRVlYUmhZbUZ6ClpYTXdnZ0VpTUEwR0NTcUdTSWIzRFFFQkFRVUFBNElCRHdBd2dnRUtBb0lCQVFEb0ZFNGQ0SGdOeXZMUVIwR3gKQTB0amRXQnM4NVBjTDNyRStjN1R3K2diRUdQSUxJU0VZV3o4Y1g1TG1XQk0rY1FnOG9VeSsrQXJ3OEoxaXdRZQpySmlIU2I1clF4WTM0c3BQeGRFVEZkWEhScnJhMGU2VmM4MW42TllJL0ZHSnl1Q3hrTG5GMUtFQW9hbHYwaDM2CnhDT0FvcXRwTlFrTzNpMTRGeU0yRDRiajkxckI4RGk4Vy9XMVpVdVhMNGwzZXVLZUVCeTRuZmhJV3kySVc3aUMKbGpMZ3RlN3hZTDVHbVpKOUdsYWtrSnJ1cnpNREFQLzVUYnRlUUIydElodTBRSVRFZHlESVFYUEZGRDBHYzloZAo3M29JdnpVZUJ3VC9uRHN3OTJNNC82SkdtZWpKN0lpdFBTN3Y2a2dlUVhINDlBaUVJNXpQdUVpVzNOYi9GR0pYCmY2a2JBZ01CQUFHalV6QlJNQjBHQTFVZERnUVdCQlR2RzZ2RU5MRjFVbWZnQ003MmxOcmMzSDI2bURBZkJnTlYKSFNNRUdEQVdnQlR2RzZ2RU5MRjFVbWZnQ003MmxOcmMzSDI2bURBUEJnTlZIUk1CQWY4RUJUQURBUUgvTUEwRwpDU3FHU0liM0RRRUJDd1VBQTRJQkFRQTgvdFVnUTZlaTZYWHZndDJ0dUdrbkpva1Y5UWNkaTNZbFVFWkNDUytjClVQZ3NnMnVBMldxcHlWTm1mRkhjcHZ1Vmp0VHRYTmk2NUM2WlZsRnYxc3p1cU9zdFB5bkJ4blN4cUs0dkc0dTkKVjBWRUgxcE1tZnZBSmxkV3c4UEJTZGJtTk1HdGM4SzlwT0o5OVdBQ1ZFRXVXVGdDeHJKTXFBZnpYUXlidUV0dwp0cW1pV2swTmVXNGk5ZEY4S2dTWUVaQWFodXVBSlRldXB2R2RPV1U0eEV4bm03aEVRbmZPV2ZITThDd08xNWFZClRGQ2s0Q0pDUmR4Mlg5U284V3o1Z3MzcncyRkFDQlJyZ0NYeFFDZnZrZTZUdVNHNkxFRHJHbmpWaXVSQkpZdW4KT1RxWXROaVBHaHpuTHJrL0Fzam1LMzBxQmFLTmFyNUdQajhqalpNb2RiZ04KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
        "name": "1dd14d0c-1b52-4f63-a606-53ecba28771d"
      },
      "composed": [
        "db2://yhc80422:ztvWffHhMCYbmzXw@8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30120/bludb?authSource=admin&replicaSet=replset"
      ],
      "database": "bludb",
      "host_ros": [],
      "hosts": [
        {
          "hostname": "8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud",
          "port": 30120
        }
      ],
      "jdbc_url": [
        "jdbc:db2://8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30120/bludb:user=<userid>;password=<your_password>;sslConnection=true;"
      ],
      "path": "/bludb",
      "query_options": {
        "authSource": "admin",
        "replicaSet": "replset"
      },
      "replica_set": "replset",
      "scheme": "db2",
      "type": "uri"
    }
  },
  "instance_administration_api": {
    "deployment_id": "crn:v1:bluemix:public:dashdb-for-transactions:eu-gb:a/1072bde6853044c2bcefefe05dfb8244:2060d3e3-ea60-4845-ba9d-42d821a077e2::",
    "instance_id": "crn:v1:bluemix:public:dashdb-for-transactions:eu-gb:a/1072bde6853044c2bcefefe05dfb8244:2060d3e3-ea60-4845-ba9d-42d821a077e2::",
    "root": "https://apieugb.db2.cloud.ibm.com/v5/ibm"
  }
}

#important credentials from db2
userid = credentials['connection']['db2']['authentication']['username']
password = credentials['connection']['db2']['authentication']['password']
rest_api_hostname = 'bs2ipcul0apon0jufi80lite.db2.cloud.ibm.com'
deployment_id = credentials['instance_administration_api']['deployment_id']

#sql_command = "SELECT * FROM USERS ORDER BY userid DESC LIMIT 1"
sql_command = "SELECT * FROM IBM_AI"

#method to get authentication token
def get_auth(userid, password, rest_api_hostname, deployment_id):

  #establish a connection
  conn = http.client.HTTPSConnection(rest_api_hostname)

  #set up the payload with crednetials
  payload  = "{\"userid\":\"" + userid + "\",\"password\":\"" + password + "\"}"

  headers = {
      'content-type': "application/json",
      'x-deployment-id': deployment_id
      }

  #use a POST request to the /auth/tokens endpoint with the payload and headers
  conn.request("POST", "/dbapi/v4/auth/tokens", payload, headers = headers)

  #get response
  res = conn.getresponse()
  data = res.read()

  #parse response
  data_decoded = json.loads(data.decode("utf-8"))
  auth_token = data_decoded["token"]

  #return auth token to be used in further requests
  return(auth_token)

def get_api_key(rest_api_hostname, deployment_id, auth_token):
  conn = http.client.HTTPSConnection(rest_api_hostname)

  headers = {
      'content-type': "application/json",
      'authorization': "Bearer " + auth_token,
      'x-deployment-id': deployment_id
      }

  conn.request("GET", "/dbapi/v4/auth/token/publickey", headers=headers)

  res = conn.getresponse()
  data = res.read()

  data_decoded = json.loads(data.decode("utf-8"))
  public_key = data_decoded["kid"]

  return public_key

def send_sql(rest_api_hostname, deployment_id, auth_token, sql_command):
  #establish connection
  conn = http.client.HTTPSConnection(rest_api_hostname)

  #create payload and headers
  payload = "{\"commands\":\"" + sql_command + "\",\"limit\":10,\"separator\":\";\",\"stop_on_error\":\"yes\"}"

  headers = {
      'content-type': "application/json",
      'authorization': "Bearer " + auth_token,
      'x-deployment-id': deployment_id
      }

  #request to perform job
  conn.request("POST", "/dbapi/v4/sql_jobs", payload, headers = headers)

  res = conn.getresponse()
  data = res.read()

  #parse result
  data_decoded = json.loads(data.decode("utf-8"))
  job_id = data_decoded["id"]

  print(job_id)

  return job_id

def get_sql_result(auth_token, rest_api_hostname, job_id):

  #establish connection
  conn = http.client.HTTPSConnection(rest_api_hostname)

  #create headers
  headers = {
  'content-type': "application/json",
  'authorization': "Bearer " + auth_token,
  'x-deployment-id': deployment_id
  }

  #create request to get job result
  request = "/dbapi/v4/sql_jobs/"
  request = request + job_id

  #get request
  conn.request("GET", request, headers = headers)

  res = conn.getresponse()
  data = res.read()

  #parse response
  data_decoded = json.loads(data.decode("utf-8"))
  result = data_decoded["results"]
  
  return result

@app.route('/cloud')
def get_cloud():
  sql_command = "SELECT * FROM IBM_CLOUD"

  auth_token = get_auth(userid, password, rest_api_hostname, deployment_id)

  job_id = send_sql(rest_api_hostname, deployment_id, auth_token, sql_command)

  result = get_sql_result(auth_token, rest_api_hostname, job_id)

  json_result = result[0]
  
  rows = json_result["rows"]

  rows = np.array(rows)

  rows = rows.flatten()

  rows = rows.tolist()

  json_result["rows"] = rows

  return jsonify(json_result)

@app.route('/ai')
def get_ai():
  sql_command = "SELECT * FROM IBM_AI"

  auth_token = get_auth(userid, password, rest_api_hostname, deployment_id)

  job_id = send_sql(rest_api_hostname, deployment_id, auth_token, sql_command)

  result = get_sql_result(auth_token, rest_api_hostname, job_id)

  json_result = result[0]

  rows = json_result["rows"]

  rows = np.array(rows)

  rows = rows.flatten()

  rows = rows.tolist()

  json_result["rows"] = rows

  return jsonify(json_result)

@app.route('/security')
def get_security():
  sql_command = "SELECT * FROM IBM_SECURITY"

  auth_token = get_auth(userid, password, rest_api_hostname, deployment_id)

  job_id = send_sql(rest_api_hostname, deployment_id, auth_token, sql_command)

  result = get_sql_result(auth_token, rest_api_hostname, job_id)

  json_result = result[0]

  rows = json_result["rows"]

  rows = np.array(rows)

  rows = rows.flatten()

  rows = rows.tolist()

  json_result["rows"] = rows

  return jsonify(json_result)

@app.route('/data-science')
def get_data_science():
  sql_command = "SELECT * FROM IBM_DATA_SCIENCE"

  auth_token = get_auth(userid, password, rest_api_hostname, deployment_id)

  job_id = send_sql(rest_api_hostname, deployment_id, auth_token, sql_command)

  result = get_sql_result(auth_token, rest_api_hostname, job_id)

  json_result = result[0]

  rows = json_result["rows"]

  rows = np.array(rows)

  rows = rows.flatten()

  rows = rows.tolist()

  json_result["rows"] = rows

  return jsonify(json_result)

if __name__ == "__main__":
  app.run(port = 5000)
 