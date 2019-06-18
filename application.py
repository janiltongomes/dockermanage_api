from sanic import Sanic
from urllib import response
from blueprints.globalRequest import global_requests
from blueprints.containers import application as containers
#from blueprints.promotion import application as promotion
#from blueprints.participation import application as participation
#from blueprints.user import application as user
#from blueprints.ocr import application as ocr

app = Sanic(__name__)
app.blueprint(containers)
#app.blueprint(participation)
#app.blueprint(user)
#app.blueprint(ocr)
app.blueprint(global_requests)

# @app.exception(Exception)
# async def test(request, exception):
#     return response.json({"utils": "{}".format(exception), "status": exception.status_code},
#                          status=exception.status_code)


def main():
    app.run(host="0.0.0.0", port=5000, workers=1, debug=False)


if __name__ == '__main__':
    main()
