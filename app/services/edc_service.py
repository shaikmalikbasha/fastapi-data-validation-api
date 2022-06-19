class EDCService:
    def metric_instance_param_parser(self, req_body):
        """Function to remove "<" and ">" symbol from the request body keys"""
        # req_body look like this
        # req_body = {'<BATCH_ID>': '123456', '<GROUP>': 'TEST_GROUP_NAME', '<ADDRESS_STATE>': 'OHIO'}
        temp_dict = dict()
        custom_parameter_string = ""

        for key in req_body.keys():
            altered_key = key.replace("<", "")  #'BATCH_ID>'
            altered_key = altered_key.replace(">", "")  #'BATCH_ID'
            temp_dict[altered_key] = req_body[
                key
            ]  # temp_dict['BATCH_ID'] = req_body['key']
            if custom_parameter_string != "":
                custom_parameter_string += (
                    ", " + altered_key + ":" + temp_dict[altered_key]
                )
            else:
                custom_parameter_string += altered_key + ":" + temp_dict[altered_key]
        return custom_parameter_string
