from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import PushServerError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

def send_notification(tokens, message, extra=None):
    for token in tokens:
        print("AQUUII " + token)
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
