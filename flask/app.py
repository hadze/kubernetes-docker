from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images
images = [
    "https://iconarchive.com/show/my-seven-icons-by-itzikgur/Backup-IBM-Server-icon.html",
    "https://iconarchive.com/show/oxygen-icons-by-oxygen-icons.org/Places-network-server-database-icon.html",
    "https://iconarchive.com/show/windows-8-icons-by-icons8/Network-Server-icon.html",
    "https://iconarchive.com/show/oxygen-icons-by-oxygen-icons.org/Mimetypes-application-x-smb-server-icon.html"
]

@app.route('/')
def index():
    urls_with_images = random.choice(images)
    return render_template('index.html', url=urls_with_images)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
