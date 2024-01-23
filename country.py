from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

API_ENDPOINT = "https://www.travel-advisory.info/api"

def lookup_country_name(country_code):
    response = requests.get(f"{API_ENDPOINT}?countrycode={country_code}")
    data = response.json()

    if data['status'] == 'ok':
        country_name = data['data'][country_code]['name']
        return country_name
    else:
        return f"Could not retrieve data for country code {country_code}"

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/diag')
def diag():
    try:
        response = requests.get(API_ENDPOINT)
        api_status = {"api_status": {"code": response.status_code, "status": response.json().get('status')}}
        return jsonify(api_status)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/convert/<country_name>')
def convert(country_name):
    country_code = None

     country_code = lookup_country_code(country_name)

     local_data = read_from_file()
     country_code = local_data.get(country_name)

    return jsonify({"country_name": country_name, "country_code": country_code})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
