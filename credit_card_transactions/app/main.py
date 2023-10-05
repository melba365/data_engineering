#Create and host API using fastAPI and uvicorn
#Send the json message onto Kafka topic via kafka producer
from fastapi import FastAPI

#BaseModel for the class
from pydantic import BaseModel

#Turn the defined class into JSON and return response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

#For json.dumps (to str)
import json

#Kafka
from kafka import KafkaProducer, producer

#creating class schema for the json
class CreditCardTx(BaseModel):
    row_id: int
    trans_date_trans_time: str
    cc_num:int
    merchant:str
    category: str
    amt: float
    first: str
    last: str
    gender: str
    street: str
    city: str
    state: str
    zip: int
    lat: float
    long: float
    city_pop: int
    job: str
    dob: str
    trans_num: str
    unix_time: int
    merch_lat: float
    merch_long: float
    is_fraud:int

app=FastAPI()

@app.get("/")
async def root():
    return{"message":"Credit Card Transactions API"}

@app.post("/creditcardtx")
async def post_creditcard_tx(tx:CreditCardTx):
    print("Transaction Received")

    try:
        #Converting class to Json to be sent as response
        tx_as_json=jsonable_encoder(tx)

        tx_json_as_str=json.dumps(tx_as_json)
        print("Json to string for kafka:",tx_json_as_str)
        produce_kafka(tx_json_as_str)

        print("Successful Json Response to be sent with status code 201")
        return JSONResponse(content=tx_as_json, status_code=201)

    except ValueError:
        print("Error Json Response to be sent with status code 400")
        return JSONResponse(content=jsonable_encoder(tx), status_code=400)

def produce_kafka(tx_json_str):
    #Attaching kafka producer to bootstrap server
    #incase on localhost use localhost:9093 (in place of kafka:9092)
    producer = KafkaProducer(bootstrap_servers='kafka:9092',acks=1)
    
    print("Sending transaction string onto kafka topic cc-ingestion-topic")
    #Write tx_json_string as bytes to kafka topic
    producer.send('cc-ingestion-topic',bytes(tx_json_str,'utf-8'))
    producer.flush()