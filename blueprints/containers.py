from sanic import Blueprint
from sanic.response import json
from sanic.response import text

from services.containers import Containers
import asyncio

application = Blueprint('containers', url_prefix='/api/containers')
containers = Containers()




@application.route("/list")
async def containersList(request):
    resultCodeRequest = await containers.listContainers()
    if resultCodeRequest[1] == 200:
        return json(resultCodeRequest[0], status=resultCodeRequest[1])
    else:
        return text('', status=resultCodeRequest[1])

@application.route("/start/<containerId>", methods=["PUT"],)
async def containersStart(request, containerId):
    resultCodeRequest = await containers.startContainers(containerId)
    return text('', status=resultCodeRequest)

@application.route("/stop/<containerId>", methods=["PUT"])
async def containersStop(request, containerId):
    resultCodeRequest = await containers.stopContainers(containerId)
    return text('', status=resultCodeRequest)

