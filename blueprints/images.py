#!/usr/bin/python
# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import json
from sanic.response import text
from sanic_validation import validate_json

from services.images import Images
import asyncio

application = Blueprint('images', url_prefix='/api/images')
images = Images()


@application.route("/list")
async def imagesList(request):
    resultCodeRequest = await images.listImages()
    if resultCodeRequest[1] == 200:
        return json(resultCodeRequest[0], status=resultCodeRequest[1])
    else:
        return text('', status=resultCodeRequest[1])

@application.route("/remove/", methods=["PUT"])
async def containerRemove(request):
    resultCodeRequest = await images.removeImage(request)
    return text('', status=resultCodeRequest)

@application.route("/container/create/", methods=["POST"])
@validate_json({
    'imageId': 
        {'type': 'string', 'required': True},
    'name': 
        {'type': 'string', 'required': False},
    'ports': 
        {'type': 'string', 'required': False},
    'command': 
        {'type': 'string', 'required': False},
    })
async def containerCreate(request):
    resultCodeRequest = await images.createImageContainer(request)
    return text('', status=resultCodeRequest)

    

