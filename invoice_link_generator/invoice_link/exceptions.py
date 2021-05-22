from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        customized_response = {
            'status_code': "400",
            'status': False,
            'message': "Validation error",
            'data': {}
        }

    if(isinstance(response.data,dict)):
        for key, value in response.data.items():#for handling dictionaries
            if(isinstance(value,dict)):#for handling 'user' details exceptions#
                for k,v in value.items():
                    error = {k: v}
                    customized_response['data'].update(error)
            else:
                error = {key: value}
                customized_response['data'].update(error)

    # if (isinstance(response.data, list)):#for handling list of dictionaries
    #     for i in response.data:
    #         for key, value in i.items():
    #             error = {key: value}
    #             customized_response['data'].update(error)

    response.data = customized_response

    return response
