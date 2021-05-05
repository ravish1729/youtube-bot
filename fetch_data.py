from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import requests
from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)

options = Options()
options.headless = True
driver = webdriver.Chrome("./chromedriver", options=options)
#print(sys.argv[1:][0])

@app.route('/get_youtube', methods=['GET'])
def get_data():
	keyword = request.args.get('keyword')
	keyword = keyword.replace(" ","+")
	
	driver.get("http://www.youtube.com/results?search_query="+keyword)
	source = driver.page_source
	return jsonify({'status': 200, 'message' : 'success', 'data': source})

if __name__ == "__main__":
    app.run(debug=True)
