import requests, json
import settings

def main():
	URL = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key=" + settings.MOSRU_API_KEY

	resp = requests.get(URL)

	data = json.loads(resp.text)

	with open("newborns.json", "w") as text_file:
		text_file.write(resp.text)
		text_file.close()

if __name__ == "__main__":
	main()
