import os
import requests
import time

# PythonAnywhere API endpoint
API_BASE_URL = "https://www.pythonanywhere.com/api/v0/user/{username}/"
# PythonAnywhere console ID
CONSOLE_ID = os.environ["PA_CONSOLE_ID"]


def send_command(username, token, command):
    headers = {"Authorization": f"Token {token}"}

    # Send command to the console
    response = requests.post(
        API_BASE_URL.format(username=username) + f"consoles/{CONSOLE_ID}/send_input/",
        headers=headers,
        data={"input": command + "\n"},
    )
    if response.status_code != 200:
        raise Exception(f"Failed to send command: {response.content}")


def deploy_to_pythonanywhere():
    username = os.environ["PA_USERNAME"]
    token = os.environ["PA_API_TOKEN"]

    # Update files from GitHub
    print("Pulling latest code from GitHub...")
    send_command(username, token, "cd ~/word-api && git pull")

    # Install/update dependencies
    print("Updating dependencies...")
    send_command(username, token, "cd ~/word-api && pip install -r requirements.txt")

    time.sleep(30)

    # Reload the web app
    print("Reloading web app...")
    headers = {"Authorization": f"Token {token}"}
    response = requests.post(
        API_BASE_URL.format(username=username)
        + f"webapps/{username}.pythonanywhere.com/reload/",
        headers=headers,
    )
    if response.status_code != 200:
        raise Exception(f"Failed to reload web app: {response.content}")

    print("Deployment completed successfully!")


if __name__ == "__main__":
    deploy_to_pythonanywhere()
