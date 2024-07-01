from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the request
    request_data = request.get_json()

    # Extract the session ID from the JSON data
    session_id = request_data.get('session')
    print(session_id)
    # Now you can save the session_id or perform any other operation you need
    # For example, saving it to a database
    save_session_id(session_id)

    # Prepare a response for Dialogflow
    response = {
        "fulfillmentText": "Session ID has been saved successfully."
    }

    return jsonify(response)

def save_session_id(session_id):
    # Your code to save the session_id goes here
    # For example, save it to a file, database, etc.
    with open('sessions.txt', 'a') as file:
        file.write(f"{session_id}\n")


