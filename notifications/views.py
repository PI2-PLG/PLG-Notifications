from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from exponent_server_sdk import PushClient, PushMessage, PushServerError, PushResponseError, DeviceNotRegisteredError, MessageTooBigError, MessageRateExceededError
from notifications.helper import send_notification
import json
import requests as req
import io


class SendNotification(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        print("[LOG] Modules and modules status received...")
        try:
            modules = request.data["modules"]
            tokens = request.data["notification_tokens"]
            print("[LOG] Cheking modules status...")
            print(len(modules))
            for module in modules:
                if(module["module_status"] == "OFFLINE"):
                    message = "The module " + module["module_name"] + " is offline!"
                    print("[LOG] " + message)
                    send_notification(tokens, message)
                elif(module["module_status"] == "FIRERISK"):
                    message = "This module (" + module["module_name"] + ") is on fire risk!"
                    print("[LOG] " + message)
                    send_notification(tokens, message)
                elif(module["module_status"] == "IN_MOTION"):
                    message = "The module " + module["module_name"] + " is in move!"
                    print("[LOG] " + message)
                    send_notification(tokens, message)
            return Response({"response":"notifications_sent"}, status=status.HTTP_200_OK)

        except:
            return Response({"response":"unsent_notification"}, status=status.HTTP_200_OK)

