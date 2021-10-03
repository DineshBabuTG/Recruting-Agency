"""The candidate service access.

This module manages saving the candidates and reading them back.
"""
import logging
import datetime
import json
import requests

# create logger
logger = logging.getLogger('jobUIService')

jobServiceBaseurl = "http://127.0.0.1:9000"
addJobAPIURL = jobServiceBaseurl + "/jobservice/addjob"
getAllJobsAPIURL = jobServiceBaseurl + "/jobservice/getalljobs"

headers = {'Content-Type': 'application/json'}

def get_all_jobs():
    """Returns all the existing jobs.
    """
    print("In Get All Job method")
    jobs = requests.get(getAllJobsAPIURL, headers=headers)
    responseData = json.loads(jobs.content)
    print("GET Jobs: " + str(jobs.content))
    return responseData

def save_job(clientname, jobprofile, jobrequirements):
    print("In Save Job method")
    timestamp = datetime.datetime.now().isoformat().replace(":","")

    print("clientname " + clientname + " jobprofile " + jobprofile + " jobrequirements " + jobrequirements)
    print("Going to trigger Add Job API from web app")
    jobPayload = dict({'clientname': clientname, 'jobprofile': jobprofile, 'jobrequirements': jobrequirements})
    data = json.dumps(jobPayload)
    print("Add Job Request payload is: " + data)

    response = requests.post(addJobAPIURL, data, headers=headers)