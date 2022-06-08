# encoding = utf-8

import os
import sys
import time
import datetime
import json
import import_declare_test
from splunklib import modularinput as smi
bin_dir = os.path.basename(__file__)
import traceback
import requests
from splunklib import modularinput as smi
from solnlib import conf_manager
from solnlib import log
from solnlib.modular_input import checkpointer
from splunktaucclib.modinput_wrapper import base_modinput  as base_mi

class ModInputjson_placeholder(base_mi.BaseModInput):

    def __init__(self):
        use_single_instance = False
        super(ModInputjson_placeholder, self).__init__("ta_conf22_debugging", "json_placeholder", use_single_instance)
        self.global_checkbox_fields = None

    def get_scheme(self):
        """overloaded splunklib modularinput method"""
        scheme = super(ModInputjson_placeholder, self).get_scheme()
        scheme.title = ("{JSON} Placeholder")
        scheme.description = ("Go to the add-on\'s configuration UI and configure modular inputs under the Inputs menu.")
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True

        scheme.add_argument(smi.Argument("name", 
                                        title="Name",
                                        description="",
                                        required_on_create=True))

        scheme.add_argument(smi.Argument("resource", 
                                        title="Resource",
                                        description="The resource to query for results",
                                        required_on_create=True,
                                        required_on_edit=False))
        return scheme

    def validate_input(helper, definition):
        pass

    def collect_events(helper, ew):
        resource = helper.get_arg("resource")
        response = requests.get("https://jsonplaceholder.typicode.com%s" % resource)
        resources = json.loads(response.content)
        for resource in resources:
            event = helper.new_event(data=json.dumps(resource))
            ew.write_event(event)    

    def get_account_fields(self):
        account_fields = []
        return account_fields

    def get_checkbox_fields(self):
        checkbox_fields = []
        return checkbox_fields

    def get_global_checkbox_fields(self):
        if self.global_checkbox_fields is None:
            checkbox_name_file = os.path.join(bin_dir, 'global_checkbox_param.json')
            try:
                if os.path.isfile(checkbox_name_file):
                    with open(checkbox_name_file, 'r') as fp:
                        self.global_checkbox_fields = json.load(fp)
                else:
                    self.global_checkbox_fields = []
            except Exception as e:
                self.log_error('Get exception when loading global checkbox parameter names. ' + str(e))
                self.global_checkbox_fields = []
        return self.global_checkbox_fields

if __name__ == "__main__":
    exitcode = ModInputjson_placeholder().run(sys.argv)
    sys.exit(exitcode)
