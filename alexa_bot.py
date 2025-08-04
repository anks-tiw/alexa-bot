from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alexa', methods=['POST'])
def alexa_webhook():
    req_data = request.get_json()

    try:
        user_query = req_data['request']['intent']['slots']['query']['value']
    except:
        user_query = "unknown"

    print("Received query from Alexa: {}".format(user_query))

    response_text = "This is a static response from your chatbot backend."

    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": response_text
            },
            "shouldEndSession": False
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
