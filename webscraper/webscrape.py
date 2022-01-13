from requests_html import HTMLSession
import googletrans as gt

tr = gt.Translator()

s = HTMLSession()
query = ''

print()
print("===========WEATHER VIA WEB SCRAPING===========".center(40))
print()
query = input("Enter city to check weather:")
url = f"https://www.google.com/search?q=weather+{query}"
r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'})
print()
temp = r.html.find('span#wob_tm', first=True).text

unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
trans = tr.translate(desc, dest='en')
des = (trans.text).capitalize()

perc = r.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text

hmd = r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text

location = r.html.find('div#wob_loc', first=True).text
trans2 = tr.translate(location, dest='en')
loc = (trans.text).capitalize()

print("Location: ", loc)
print("Temperature: ", temp, unit)
print("Description: ", des)
print("Percipitation: ", perc)
print("Humidity: ", hmd)