from flask import Flask
from datetime import datetime
import os
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Get the full name
    name = "Mrudula Gajulapalli"  # Replace with your actual name

    # Get the username
    username = os.getlogin()

    # Get server time in IST
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get the top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Render the data as an HTML page
    return f"""
    <html>
        <body>
            <h2>Name: {name}</h2>
            <h3>Username: {username}</h3>
            <h3>Server Time (IST): {server_time}</h3>
            <h3>TOP output:</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
