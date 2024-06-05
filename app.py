from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    api_key = 'YOUR_API_KEY'
    city = 'London'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(api_url)
    if response.status_code != 200:
        return jsonify({'error': 'Network response was not ok'})

    data = response.json()
    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
