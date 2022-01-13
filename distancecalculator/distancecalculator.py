from requests_html import HTMLSession
import googletrans as gt

tr = gt.Translator()
s = HTMLSession()

print()
print("===========Distance Calculator===========".center(40))
print()
print("This calculator will give you the distance between two cities.")
loc1 = input("Enter city 1:")
loc2 = input("Enter city 2:")
url = f"https://www.google.co.uk/search?q=distance+between+{loc1}+and+{loc2}"
r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'})
print()
dist = r.html.find('span.UdvAnf', first=True).text
d1 = tr.translate(dist, dest='en')
dis = (d1.text).capitalize()
print(f"Distance between {loc1} and {loc2}: ", dis)

