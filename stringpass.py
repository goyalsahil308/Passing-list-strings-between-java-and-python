from flask import Flask, jsonify
import pickle
import requests

def string():
    data=input("Enter your name:")
    with open("stringpass.pkl","wb") as sp:
       pickle.dump(data,sp)
string()

