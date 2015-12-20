from __future__ import print_function
import json
import requests
import boto3
import constants

def lambda_handler(event, context):
    name = event['name']
    contact = event['contact']
    publish = event['publish']
    message = event['message']
    payload = { 'secret': RECAPTCHA_SECRET, 'response': event["recaptcha"] }
    r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=payload)
    print(r.json())
    if r.json()['success']:
        client = boto3.client('ses')
        client.send_email(Source=FROM,
                          Destination={ 'ToAddresses' : TO},
                          Message={
                            'Subject': {
                                'Data': 'New feedback from ' + name,
                                'Charset': 'UTF-8'
                            },
                            'Body': {
                                'Text': {
                                    'Data': """Hi there!

%s has contacted you on your blog. %s had the following to say:

%s

%s can be contacted at: %s and had this to say about publishing: %s

Thank you.
""" % (name, name, message, name, contact, publish)
                                }
                            }
                        })
        
    return r.json()
