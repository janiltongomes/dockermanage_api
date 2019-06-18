#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
from functools import wraps

import aiohttp
from sanic import Blueprint
from sanic.response import json

global_requests = Blueprint('global_requests')

def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            
            is_authorized = False
            authorization = request.headers['Authorization'] if 'Authorization' in request.headers else None

            if authorized is not None:
                # implement authentication
                is_authorized = True

            if is_authorized:
                # the user is authorized.
                response = await f(request, *args, **kwargs)
                return response
            else:
                # the user is not authorized.
                return json({'status': 'unauthorized'}, 401)

        return decorated_function

    return decorator


@global_requests.middleware("request")
@authorized()
async def log_uri(request):
    pass