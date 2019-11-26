from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import PushServerError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from notifications.models import Notification

def create_notification(module):
    title = ''
    message = ''
    if(module["module_status"] == "OFFLINE"):
        title = f'[{module["module_name"]}] Módulo Offline!'
        message = f'Não foi possível localizar o {module["module_name"]}!'
        print(f'[LOG] {module["module_name"]} is OFFLINE')
    elif(module["module_status"] == "IN_MOTION"):
        title = f'[{module["module_name"]}] Em Movimento!'
        message = f'O sistema detectou que {module["module_name"]} aparentmente está em movimento!'
        print(f'[LOG] {module["module_name"]} is IN_MOTION')
    elif(module["module_status"] == "FIRERISK"):
        title = f'[{module["module_name"]}] Risco de Queimada!'
        message = f'O sistema detectou uma possível queimada! Verifique o {module["module_name"]}.'
        print(f'[LOG] {module["module_name"]} is in FIRERISK')

    notification = Notification(
                                title=title,
                                message=message,
                                module_name=module_name,
                                )
    notification.save()

def send_notification(tokens, message, extra=None):
    for token in tokens:
        try:
            response = PushClient().publish(
                PushMessage(to=token,
                            body=message,
                            data=extra))
        except PushServerError as exc:
            rollbar.report_exc_info(
                extra_data={
                    'token': token,
                    'message': message,
                    'errors': exc.errors,
                    'response_data': exc.response_data,
                })
            raise
        except (ConnectionError, HTTPError) as exc:
            rollbar.report_exc_info(
                extra_data={'token': token, 'message': message})
            raise self.retry(exc=exc)