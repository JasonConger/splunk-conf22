import import_declare_test
import splunklib.client as client
import six
import sys
import json
import requests
import os
from splunktaucclib.alert_actions_base import ModularAlertBase

class AlertActionWorker_post_post(ModularAlertBase):

    def __init__(self, ta_name, alert_name):
        super(AlertActionWorker_post_post, self).__init__(ta_name, alert_name)

    def validate_params(self):

        if not self.get_param("title"):
            self.log_error('title is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("body"):
            self.log_error('body is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("userid"):
            self.log_error('userId is a mandatory parameter, but its value is None.')
            return False

        return True

    def process_event(helper, *args, **kwargs):
        helper.log_info("_Splunk_ alert action post_post started.")
        title = helper.get_param("title")
        body = helper.get_param("body")
        userId = helper.get_param("userid")
    
        # If you need to use Splunk REST APIs in your code, here's how
        try:
            service = client.connect(token=helper.session_key)
        except Exception as e:
            helper.log_error("_Splunk_ error connecting to Splunk client: %s" % str(e))
            sys.exit(1)
        
        try:
            url = "https://jsonplaceholder.typicode.com/posts"
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            data = {
                "title": "{title}".format(title=title),
                "body": "{body}".format(body=body),
                "userId": userId
            }
            response = requests.post(url, headers=headers, json=data)
            helper.log_info("_Splunk_ wrote post to %s. Response: %s" % (url, json.dumps(response.json())))
        except Exception as e:
            helper.log_error("_Splunk_ exception occurred posting a post: %s" % str(e))
            sys.exit(1)
        return 0

if __name__ == "__main__":
    exitcode = AlertActionWorker_post_post("TA-conf22-debugging", "post_post").run(sys.argv)
    sys.exit(exitcode)
