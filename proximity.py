##
## Sars Cov 19 mutations replications
## author Felipe Lima <felipe@felipelima.eti.br>
##

import constant
import scapev
import os
from faker import Faker

faker = Faker()

print("Covid LOOKUP: ")

def findHospedeiros():
    getRnas()
    vacine(constant.vacine1_rna_message)

def vacine(vac: str):
    print("vacine")
    scapev.vacineResult(vac)

def initTransmission():
    print("init tranmsmission Wuhan")
    name = faker.name();
    sequencemutation = faker.ssn();

    scapev.infect(name, sequencemutation)
    scapev.mutations(name, sequencemutation)

def getRnas():
    # exists mutations ?
    if not os.listdir(constant.mutationsDir):
       return initTransmission()
    else:
      return pandemicTransmission()

def pandemicTransmission():

    print('pandemic')
    name = faker.name();
    sequencemutation = faker.ssn();

    scapev.infect(name, sequencemutation)
    scapev.mutations(name, sequencemutation)

## STARTED IN WURAN
findHospedeiros()