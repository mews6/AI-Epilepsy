import json
import pika
from ftp_helper import *
from sys import path
from os import environ

rabbit_host = environ.get("RABBITMQ_DEFAULT_HOST")
rabbit_user = environ.get("RABBITMQ_DEFAULT_USER")
rabbit_password = environ.get("RABBITMQ_DEFAULT_PASS")
rabbit_queue_name_read = 'my-predictions'
rabbit_queue_name_write = 'my-predictions-anws'

credentials = pika.PlainCredentials(rabbit_user, rabbit_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=credentials))
channel = connection.channel()

channel.queue_declare(rabbit_queue_name_read, durable=True)
print('> Declared queue for new prediction requests')
channel.queue_declare(rabbit_queue_name_write, durable=True)
print('> Declared queue for new prediction responses')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    answer_pred = predict(payload)
    answer_json = json.dumps(answer_pred)
    ch.basic_publish(exchange='', routing_key=rabbit_queue_name_write, body=answer_json)
    print(" [x] Sent "+answer_json)

def predict(payload):
    answer = {}
    mri_path = payload['mripath']
    mri_file = payload['mrifile']
    print("Predicting from mri file "+mri_file+" at "+mri_path)
    if (len(mri_file)>0):
       fetch_file(mri_path,mri_file,"mriPred.zip")
       answer.update(predict_mri("mriPred.zip"))
    eeg_path = payload['eegpath']
    eeg_file = payload['eegfile']
    print("Predicting from eeg file "+eeg_file+" at "+eeg_path)
    if (len(eeg_file)>0):
       fetch_file(eeg_path,eeg_file,"eegPred.zip")
       answer.update(predict_eeg("eegPred.zip"))
    return answer

def predict_mri(local_file):
    answer = {'mriPred': "Negative"}
    return answer

def predict_eeg(local_file):
    from analyzeEEGFile import analyzeEEGFile
    result = analyzeEEGFile(local_file)
    # Input: zip file with multiple .edf files
    # Output: Dictionary where keys are the EDF file name. And the respective value is a list of 0s and 1s.
    # Each item on the list represents 5 seconds of the exam from the edf file. 
    # The list is organized chronologically, meaning the first element represents time from 0s to 5s. Second one, from 5s to 10s and so on.
    # 1 means that the 5 second fragament is from a seizure and 0 that is seizure-free.
    answer = {'eegPred': "Negative"}
    return answer

channel.basic_consume(queue=rabbit_queue_name_read, on_message_callback=callback, auto_ack=True)

print('> Waiting requests. To exit press CTRL+C')

channel.start_consuming()
