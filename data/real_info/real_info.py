# which data do i need as real_data?

# country -> for choosing proxy, phone

# user agent -> for choosing user agent that will match with selenium driver options

# get user agent from selected browser -> for choosing user agent that will match with selenium driver options

from flask import Flask, request
import threading
from multiprocessing import Process
import os
import werkzeug
app = Flask(__name__)
import webbrowser


# Shared variable to signal app shutdown
shutdown_requested = False

# Event to signal that the first request has been received
first_request_received = threading.Event()

def open_browser(link):
    webbrowser.open(link)


class UserAgent:

    file: str = 'user_agent.txt'
    current_folder: os.path = os.path.dirname(os.path.abspath(__file__))
    full_path: str = f'{current_folder}/{file}'
    user_agent: str = None

    def __init__(self):
        self.user_agent = self.get_user_agent()

    def get_user_agent(self):
        with open(self.full_path, 'r') as file:
            return file.read()
        
    def save_user_agent(self, user_agent):
        with open(self.full_path, 'w') as file:
            file.write(user_agent)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    global shutdown_requested
    shutdown_requested = True
    return 'Server shutting down...'

@app.route('/')
def get_user_agent():
    user_agent = request.headers.get('User-Agent')

    user_agent_file = UserAgent()

    # Check if the user agent has already been saved
    with open(user_agent_file.full_path, 'r') as file:
        if user_agent not in file.read():
            user_agent_file.save_user_agent(user_agent)

    # Set the event to signal that the first request has been received
    first_request_received.set()

    return user_agent

def run_app():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    server = Process(target=app.run)
    server.start()
    open_browser('http://localhost:5000/')

    # wait for app to register GET / request
    # Wait until the first request is received
    first_request_received.wait()

    # Shutdown the Flask app    
    server.terminate()
    server.join()