from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json
    # Process the incoming data
    print('Received data:', data)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)