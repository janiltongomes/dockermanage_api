#!/usr/bin/python
# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import json
from sanic.response import text
from sanic_validation import validate_json

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
async def containerStart(request, containerId):
    resultCodeRequest = await containers.startContainer(containerId)
    return text('', status=resultCodeRequest)

@application.route("/stop/<containerId>", methods=["PUT"])
async def containerStop(request, containerId):
    resultCodeRequest = await containers.stopContainer(containerId)
    return text('', status=resultCodeRequest)

@application.route("/remove/<containerId>", methods=["PUT"])
async def containerRemove(request, containerId):
    resultCodeRequest = await containers.removeContainer(containerId)
    return text('', status=resultCodeRequest)

# @application.route("/add/", methods=["POST"])
# @validate_json({
#     'image': 
#         {'type': 'string', 'required': True},
#     'command': 
#         {'type': 'string', 'required': False},
#     })
# async def containerAdd(request):
#     resultCodeRequest = await containers.addContainer(request)
#     return text('', status=resultCodeRequest)

