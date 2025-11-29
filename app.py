from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging to write to a file (Wazuh will read this later)
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def home():
    return "<h1>Welcome to the Secure App</h1>"

# VULNERABILITY: This route allows Command Injection (BAD!)
# We are putting this here on purpose for the project.
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    # A secure app would not do this. This is for demonstration.
    import os
    os.system(f"ping -c 1 {ip}") 
    logging.info(f"Ping command executed for IP: {ip}")
    return f"Ping request sent to {ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)