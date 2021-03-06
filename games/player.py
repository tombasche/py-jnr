import requests
import json

import xml.etree.ElementTree as ET

headers = {'content-type': 'application/json'}  


class Player(object):

    def __init__(self, path):
        tree = ET.parse('data/' + path + '.xml')
        root = tree.getroot()

        config = ET.parse('data/config.xml')
        configTree = config.getroot()

        data = {"Token": "", "BotName": "", "BotVersion": "", "Game": "", "RPCEndpoint": "", "ProgrammingLanguage": "", "Website": "", "Description": ""} 

        data['Game'] = root.get('game')
        data['ProgrammingLanguage'] = root.get('language')

        for child in configTree:

            if child.tag == 'token':
                data['Token'] = child.text
            if child.tag == 'name':
                data['BotName'] = child.text
            if child.tag == 'version':
                data['BotVersion'] = child.text
            if child.tag == 'endpoint':
                data['RPCEndpoint'] = child.text
            if child.tag == 'url':
                url = child.text
            if child.tag == 'website':
                data['Website'] = child.text
            if child.tag == 'description':
                data['Description'] = child.text

        registerMessage = {
           "method": "RegistrationService.Register",
           "params": data,
           "jsonrpc": "2.0",    
           "id": 1
        }

        # response = requests.post(url, data=json.dumps(registerMessage), headers=headers)
        # print response
