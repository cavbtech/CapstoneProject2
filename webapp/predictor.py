# Implement the following two in another class
import pickle
import json
with open('/datavol/trained/model.pkl', 'rb') as f:
    clf2 = pickle.load(f)

with open("/datavol/trained/vectorCategory.json") as infile:
    data = json.load(infile)


def predict(text):
	predicted = clf2.predict(text)
	return data[predicted[0]]