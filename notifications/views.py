from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from exponent_server_sdk import PushClient, PushMessage, PushServerError, PushResponseError, DeviceNotRegisteredError, MessageTooBigError, MessageRateExceededError
import json
import requests as req
import io


class SendNotification(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        print("[LOG] Modules and modules status received...")
        try:
            modules = request.data
            print("[LOG] Cheking modules status...")
            for module in modules:
                if(module["module_status"] == "OFFLINE"):
                    print("[LOG] The module " + module["module_name"] + " is offline!")
                elif(module["module_status"] == "FIRERISK"):
                    print("[LOG] This module (" + module["module_name"] + ") is on fire risk!")
                elif(module["module_status"] == "IN_MOTION"):
                    print("[LOG] The module " + module["module_name"] + " is in move!")

            return Response({"response":"notifications_sent"}, status=status.HTTP_200_OK)

        except:
            return Response({"response":"unsent_notification"}, status=status.HTTP_200_OK)

