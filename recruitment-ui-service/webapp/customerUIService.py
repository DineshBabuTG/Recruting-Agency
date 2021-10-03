"""The candidate service access.

This module manages saving the candidates and reading them back.
"""
import logging
import datetime
import pathlib
import json
import requests
from firefly.client import Client

logger = logging.getLogger('customerUIService')

customer_service_api = Client("http://127.0.0.1:9001")

customerServiceBaseurl = "http://127.0.0.1:9001"
addCustomerAPIURL = customerServiceBaseurl + "/customerservice/addcustomer"
getAllCustomersAPIURL = customerServiceBaseurl + "/customerservice/getallcustomers"

headers = {'Content-Type': 'application/json'}

def get_all_customers():
    """Returns all the existing customers.
    """
    print("In Get All Customer method")
    customers = requests.get(getAllCustomersAPIURL, headers=headers)
    responseData = json.loads(customers.content)
    print("GET Customers: " + str(customers.content))
    return responseData

def save_customer(name, address):
    print("In Save Customer method")
    timestamp = datetime.datetime.now().isoformat().replace(":","")

    print("name " + name + " address " + address)
    print("Going to trigger Add Customer API from web app")
    customerPayload = dict({'name': name, 'address': address})
    data = json.dumps(customerPayload)
    print("Request payload is: " + data)

    response = requests.post(addCustomerAPIURL, data, headers=headers)
