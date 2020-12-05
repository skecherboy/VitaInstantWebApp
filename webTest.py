from flask import Flask, render_template, request
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

app = Flask(__name__)

cred = credentials.Certificate("enviroment variable here")
fbAdmin = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.collection(u'UserData').document(u'RnDZwSsR1IRZjL0xLHMCdtAdTjg2').collection('boolState').document('93OQNYSqsxGUTLIISaeX')

@app.route('/',methods=["GET", "POST"])

def home():
    if request.method == 'POST':
        doc_ref.update({'boolInput':1})
        return render_template("index.html") # html/css template from https://morioh.com/p/bff65aebecf9
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)