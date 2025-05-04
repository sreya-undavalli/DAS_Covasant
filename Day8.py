# Question-11:
# Weather mock API 
# format comes from below endpoint 
    # Parse format, if xml, show xml, 
    # if none, show json 
    # Put all random temp 
    # City name may change based on PATH param 
    # (currently not implemented in demo api endpoint)

#urls
#http://localhost:5000/weather/Delhi
#http://localhost:5000/weather/Delhi?format=xml
#http://localhost:5000/weather/Delhi?date=18-04-2025
#http://localhost:5000/weather/Delhi?format=xml&date=18-04-2025


from flask import Flask, request, jsonify, Response
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def create_weather_data(city_names, days=100):
    weather_conditions = ["Sunny", "Cloudy", "Partly Cloudy", "Mostly Sunny", "Windy", "Clear Sky", "Breezy"]
    forecast_data = {}
    base_date = datetime.strptime("19-04-2025", "%d-%m-%Y")

    for city in city_names:
        city_forecast = []
        current_day = base_date

        for _ in range(days):
            entry = {
                "date": current_day.strftime("%d-%B-%Y"),
                "day": current_day.strftime("%a"),
                "high_temp": random.randint(25, 45),
                "low_temp": None,
                "humidity": random.randint(25, 45),
                "rain_chances": random.randint(10, 40),
                "text": random.choice(weather_conditions),
                "code": random.randint(20, 50)
            }
            entry["low_temp"] = random.randint(10, entry["high_temp"])  # Low temp must be <= high temp
            city_forecast.append(entry)
            current_day += timedelta(days=1)

        forecast_data[city] = {"forecast": city_forecast}

    return forecast_data

def dict_to_xml(forecast_entries):
    xml_response = "<forecast>"
    for day in forecast_entries:
        xml_response += "<day>"
        for key, value in day.items():
            xml_response += f"<{key}>{value}</{key}>"
        xml_response += "</day>"
    xml_response += "</forecast>"
    return xml_response

# List of predefined cities for forecasting
city_list = ["Mumbai", "Chennai", "Hyderabad", "Bengaluru", "Pune", "Delhi", "Vizag", "Kochi", "Jaipur", "Lucknow"]
weather_data = create_weather_data(city_list)

@app.route('/weather/<city>', methods=['GET'])
def fetch_forecast(city):
    output_format = request.args.get('format', 'json').lower()
    query_date = request.args.get('date')

    if city not in weather_data:
        return jsonify({"error": f"Forecast unavailable for city: {city}"}), 404

    city_data = weather_data[city]["forecast"]

    if query_date:
        try:
            formatted_query_date = datetime.strptime(query_date, "%d-%m-%Y").strftime("%d-%B-%Y")
            day_forecast = next((day for day in city_data if day["date"] == formatted_query_date), None)

            if not day_forecast:
                return jsonify({"error": f"No data found for {city} on {query_date}"}), 404

            if output_format == "xml":
                return Response(dict_to_xml([day_forecast]), mimetype='application/xml')

            return jsonify({city: {"forecast": [day_forecast]}})
        except ValueError:
            return jsonify({"error": "Date format should be DD-MM-YYYY"}), 400

    if output_format == "xml":
        return Response(dict_to_xml(city_data), mimetype='application/xml')

    return jsonify({city: {"forecast": city_data}})

if __name__ == '__main__':
    app.run(debug=True)
