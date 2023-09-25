import http.client
import gzip
import io
import csv
import json
import time

print("Python message helper :)")

#globals
token = input("Please enter your XBL3.0 token: ")
host = "xblmessaging.xboxlive.com"
port = 443

with open('xuids.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for individual_id in row:

            #connects to the xbox live messaging api
            conn = http.client.HTTPSConnection(host, port)
            conn.request("CONNECT", host + ":" + str(port))

            #prints the response to the connection request 
            response = conn.getresponse()
            print("Response Status:", response.status)
            print("Response Headers:")
            for header, value in response.getheaders():
                print(header + ": " + value)

            #the request parameters
            headers = {
                "x-xbl-contract-version": "1",
                "Accept-Encoding": "gzip, deflate",
                "x-xbl-clientseqnum": "2",
                "signature": "AAAAAQHZ6bUlJABpPZSWe69aPES/teR/+md2Lmq7+9yclBnGPNMeRU9nNWhhR5hxboOPAG+VxmRI5lEFFveBe3tzL5XwKH03ltsJWg==",
                "accept": "application/json",
                "ms-cv": "fehIcPuGpTq3rwEvtzg9ux.201",
                "authorization": token,
                "Content-Type": "application/json",
                "Host": "xblmessaging.xboxlive.com",
                "Connection": "Keep-Alive",
                "Cache-Control": "no-cache"
            }

            body = {"parts":[{"contentType":"text","version":0,"text":"Boom Roasted - Michael Scott"}]}
            
            #sending the request 
            conn.request("POST", "/network/xbox/users/me/conversations/users/xuid("+individual_id+")", body=json.dumps(body), headers=headers)

            #getting the request response
            response = conn.getresponse()
            print(response.status, response.reason)
            response_body = response.read()

            print("Response Status:", response.status)
            print("Response Headers:")
            for header, value in response.getheaders():
                print(header + ": " + value)
            
            #sleeps to lower risk
            time.sleep(15)
