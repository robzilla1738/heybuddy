import os
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, User
from twilio.twiml.messaging_response import MessagingResponse
import anthropic
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        # TODO: Validate phone number and save user to database
        user = User(phone_number=phone_number)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/sms', methods=['POST'])
def handle_sms():
    incoming_msg = request.values.get('Body', '').lower()
    user_phone = request.values.get('From', '')

    # TODO: Retrieve user from database based on user_phone
    user = User.query.filter_by(phone_number=user_phone).first()

    if user:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        client = anthropic.Client(api_key)
        response = client.messages.create(
            model='claude-v1',
            messages=[
                {'role': 'system', 'content': 'You are a helpful AI assistant.'},
                {'role': 'user', 'content': incoming_msg}
            ]
        )
        ai_response = response.content
    else:
        ai_response = "Sorry, you need to register first to use this service."

    resp = MessagingResponse()
    resp.message(ai_response)
    return str(resp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
