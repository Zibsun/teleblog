from flask import Flask, abort, request
import newborns


app = Flask (__name__)

@app.route("/")
def index():
	return "Hi!"

@app.route("/names")
def names():
	try:
		request_year = int(request.args.get("year"))
		return newborns.get_table_newborns(request_year)
	except:
		return newborns.get_table_newborns("")

if __name__ == "__main__":
	app.run()