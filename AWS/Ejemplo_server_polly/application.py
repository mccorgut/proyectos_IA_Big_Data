# Import packages
from flask import Flask, request, abort, Response
from speechShynthesis import speechSynthesis as textToSpeech

# Create Flask application
application = Flask(__name__)


# api/speech-synthesis endpoint
@application.route('/speech-synthesis', methods=['POST'])
def speechSynthesis():
    try:
        textToSpeech(request.get_json())
    except Exception as error:
        print(error)
        abort(400)
    return Response(status=200)


# Run the app
if __name__ == "__main__":
    application.debug = True
    application.run()  # Running on http://127.0.0.1:5000/
