# Implement the following two in another class
import pickle
with open('../datavol/trained/model.pkl', 'rb') as f:
    clf2 = pickle.load(f)

with open("../datavol/trained/vectorCategory.pkl", 'rb') as infile:
    data = pickle.load(infile)


def predict(text):
    print(f"data={data}")
    predicted = clf2.predict(text)
    return data[predicted[0]]

predictedVal = predict([" Chennai won IPL cricket trophhy"])
print(f"predictedVal={predictedVal}")