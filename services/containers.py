#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import asyncio
import time

import docker
from docker import errors

client = docker.from_env()


class Containers:
    def __init__(self):
        self.client = docker.from_env()

    async def listContainers(self):
        requestCode = 200

        responseData = {}
        try:
            responseData['data'] = []
            for container in self.client.containers.list(all=True):
                data = {}
                data['id'] = container.id
                data['name'] = container.name
                data['status'] = container.status
                data['labels'] = container.labels
                data['ports'] = container.ports
                responseData['data'].append(data)
            

        except Exception as e:
            requestCode = 500
            responseData = {}
            #responseReturn['errno'] = e['errno']
            #responseReturn['explanation'] = str(e['explanation'])
        
        return responseData, requestCode


    async def startContainer(self, containerId):
        requestCode = 500
        if containerId is not None:
            filterData = {'id' : containerId }

        try:
            for container in self.client.containers.list(all=True, filters=filterData):
                container.start()
                requestCode = 200
            

        except Exception as e:
            pass

        
        return requestCode


    async def stopContainer(self, containerId):
        requestCode = 500
        if containerId is not None:
            filterData = {'id' : containerId }

        try:
            for container in self.client.containers.list(filters=filterData):
                container.stop()
                requestCode = 200
            

        except Exception as e:
            pass

        
        return requestCode

    async def removeContainer(self, containerId):
        requestCode = 500
        if containerId is not None:
            filterData = {'id' : containerId }

        try:
            for container in self.client.containers.list(all=True, filters=filterData):
                container.remove()
                requestCode = 200
            

        except Exception as e:
            pass

        
        return requestCode
