"""The candidate service access.

This module manages saving the candidates and reading them back.
"""
import logging
import datetime
import pathlib
import json
import requests
from firefly.client import Client

logger = logging.getLogger('candidateUIService')

candidate_service_api = Client("http://127.0.0.1:8000")

candidateServiceBaseurl = "http://127.0.0.1:8000"
addCandidateAPIURL = candidateServiceBaseurl + "/candidateservice/addcandidate"
getAllCandidatesAPIURL = candidateServiceBaseurl + "/candidateservice/getallcandidates"

headers = {'Content-Type': 'application/json'}

def get_all_candidates():
    """Returns all the existing candidates.
    """
    print("In Get All Candidate method")
    candidates = requests.get(getAllCandidatesAPIURL, headers=headers)
    responseData = json.loads(candidates.content)
    print("GET Candidates: " + str(candidates.content))
    return responseData

def save_candidate(name, address, qualification, jobskill, yearsofexperience):
    print("In Save Candidate method")
    timestamp = datetime.datetime.now().isoformat().replace(":","")

    print("name " + name + " address " + address + " qualification " + qualification + " jobskill " + jobskill + " yearsofexperience " + yearsofexperience)
    print("Going to trigger Add Candidate API from web app")
    candidatePayload = dict({'name': name, 'address': address, 'qualification': qualification, 'jobskill': jobskill, 'yearsofexperience': yearsofexperience})
    data = json.dumps(candidatePayload)
    print("Request payload is: " + data)

    #print(candidate_service_api.add_candidate(name=name, address=address, qualification=qualification, jobskill=jobskill, yearsofexperience=yearsofexperience))
    response = requests.post(addCandidateAPIURL, data, headers=headers)
    #print("Response is: " + response.content.json)
    #addedcandidate = candidate_service_api.add_candidate(name=name, address=address, qualification=qualification, jobskill=jobskill, yearsofexperience=yearsofexperience)
    #print(addedcandidate)
