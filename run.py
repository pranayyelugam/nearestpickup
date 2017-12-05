from flask import Flask, request ,render_template, jsonify
import pandas as pd
from scipy import spatial
import dill as pickle
import os
app = Flask(__name__)


@app.route('/<location>')
def hello(location):
	lat,lon=location.split('&')
	lat = float(lat)
	lon = float(lon)
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
	fname = 'tree.pk'
	print("Loading the model...")
	tree = None
	with open(fname,'rb') as f:
		tree = pickle.load(f)
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port,debug=True)
