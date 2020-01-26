from flask import Flask
import sys
import zulip

global recent_msg_id

app = Flask(__name__)

@app.route("/send")
def send_msg():
	client = zulip.Client(config_file="madhu")
	request = {
		"type": "private",
		"to": "fmy-bot@zulipchat.com",
		"content": "C#"
	}
	
	result = client.send_message(request)
	global recent_msg_id
	recent_msg_id = result["id"]
	return result

@app.route("/recv")
def recv_msg():

    client = zulip.Client(config_file="zuliprc")
    global recent_msg_id
    request = {
		'anchor' : recent_msg_id,
		'num_before': 0,
		'num_after': 1
		
    } 

    result = client.get_messages(request)
    return result

@app.route("/")
def home():
    
    return "Hello"
    
if __name__ == "__main__":
    app.run(debug=True)
