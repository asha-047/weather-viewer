from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = {}
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "67941d9b9b7347571892c6594d5e14ea"  # Replace with actual key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
