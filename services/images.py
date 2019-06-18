#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import asyncio
import time

import docker
from docker import errors

client = docker.from_env()


class Images:
    def __init__(self):
        self.client = docker.from_env()

    async def listImages(self):
        requestCode = 200

        responseData = {}
        try:
            responseData['data'] = []
            images = self.client.images.list()
            for image in images:
                data = {}
                data['id'] = image.id
                data['labels'] = image.labels
                data['tags'] = image.tags
                responseData['data'].append(data)
            

        except Exception as e:
            requestCode = 500
            responseData = {}

        
        return responseData, requestCode


    async def removeImage(self, request):
        requestCode = 500
        if request.headers['Content-Type'] == 'application/json':
            try:
                dataImageStart = request.json
                requestCode = 406
                for image in self.client.images.list(all=True):
                    if image.id == dataImageStart['id']:
                        self.client.images.remove(image=image.id)
                        requestCode = 200
                    
            
            except Exception as e:
                pass

        return requestCode

    async def createImageContainer(self, request):
        requestCode = 500
        if request.headers['Content-Type'] == 'application/json':
            try:
                dataImageCreate = request.json
                dataImageCreate['command'] = dataImageCreate['command'] if 'command' in dataImageCreate else None
                requestCode = 406
                for image in self.client.images.list(all=True):
                    if image.id == dataImageCreate['imageId']:

                        args = {}
                        if 'name' in dataImageCreate:
                            args['name'] = dataImageCreate['name']
                        if 'ports' in dataImageCreate:
                            args['ports'] = json.loads(dataImageCreate['ports'].replace("'",'"'))

                        self.client.containers.create(image= image.id, command=None, **args)
                        requestCode = 200
                        break
                    
            
            except Exception as e:
                pass

        
        return requestCode