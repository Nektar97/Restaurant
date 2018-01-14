import os
from app import app

if __name__ == 'main':
	host = os.environ.get('IP', '127.0.0.1')
	port = int(os.environ.get('PORT',80))
	app.run(host=host, port=port)