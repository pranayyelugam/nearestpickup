from flask import Flask, request ,render_template, jsonify
import pandas as pd
from scipy import spatial
import dill as pickle
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/<tno>')
def hello(tno):
	id=fd.loc[fd['Truck_number'] == int(tno)]
	val=id.values.tolist()
	lat=val[0][1]
	lon=val[0][2]
	dis,idx =tree.query([(lat,lon)])
	index =idx[0]
	l=lists[index]
	res = {
		'latitude': l[0],
		'longitude': l[1],
	}
	return jsonify(res)




if __name__ == '__main__':
	df = pd.read_csv('final.csv')
	lists = df.values.tolist()
	fd = pd.read_csv('Truck.csv')
	fname = 'tree.pk'
	print("Loading the model...")
	tree = None
	with open(fname,'rb') as f:
		tree = pickle.load(f)
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port,debug=True)
