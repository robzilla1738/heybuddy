# HeyBud - AI-Powered Personal Assistant

HeyBud is an AI-powered personal assistant that allows users to interact with an intelligent chatbot via SMS. With HeyBud, users can easily manage tasks, set reminders, schedule events, take notes, and more, all through simple text messages.

## Features

- Natural language understanding and processing
- Task management and reminders
- Event scheduling and calendar integration
- Note-taking and information storage
- Email sending and notification
- Seamless communication via SMS

## Technologies Used

- Python
- Flask (Web Framework)
- Twilio (SMS Integration)
- Anthropic API (AI Language Model)
- SQLAlchemy (Database ORM)
- ngrok (Local Server Tunneling)

## Getting Started

To run HeyBud locally and start interacting with the AI assistant, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/heybud.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the necessary environment variables:
   - Create a `.env` file in the project root directory.
   - Add the following variables to the `.env` file:
     ```
     ANTHROPIC_API_KEY=your-anthropic-api-key
     TWILIO_ACCOUNT_SID=your-twilio-account-sid
     TWILIO_AUTH_TOKEN=your-twilio-auth-token
     TWILIO_PHONE_NUMBER=your-twilio-phone-number
     ```
   - Replace the placeholders with your actual API keys and credentials.

4. Run the Flask application:
   ```
   flask run
   ```

5. Expose your local server using ngrok:
   ```
   ngrok http 5000
   ```

6. Update your Twilio webhook URL:
   - Log in to your Twilio account.
   - Update the "A MESSAGE COMES IN" webhook URL for your Twilio phone number with the ngrok forwarding URL followed by `/sms` (e.g., `https://your-ngrok-url.ngrok.io/sms`).

7. Send an SMS message to your Twilio phone number and start interacting with HeyBud!

## Contributing

Contributions are welcome! If you find any bugs, have feature requests, or want to contribute enhancements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
