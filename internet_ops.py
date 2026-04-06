import requests
from bs4 import BeautifulSoup


class InternetOps:
    def get_weather(self):
        try:
            # 1. Get location
            ip_resp = requests.get('https://ipapi.co/json/').json()
            city = ip_resp.get('city', 'Chennai')

            # 2. Get Weather (format 1 is cleaner for voice)
            # %C = Condition (Sunny/Cloudy), %t = Temperature
            weather_url = f"https://wttr.in/{city}?format=%C+%t"
            response = requests.get(weather_url)
            report = response.text.strip()

            # 3. Clean up encoding issues for the Windows Console
            report = report.encode('ascii', 'ignore').decode('ascii')

            return f"Sir, the weather in {city} is currently {report}."
        except Exception as e:
            return "I'm unable to reach the weather satellite, sir."
    def web_search(self, query):
        try:
            # Simple Google Search redirect or summary
            # For a true 'Jarvis' experience, we just open the browser for you
            import webbrowser
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            return f"I've opened a search for {query} on your browser, sir."
        except Exception as e:
            return "I couldn't reach the search engines at the moment."