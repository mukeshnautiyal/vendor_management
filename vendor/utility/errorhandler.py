from rest_framework.views import exception_handler
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Update the structure of the response data.
    if response is not None:
        if response.status_code == 400:
            customized_response = {"status" : status.HTTP_400_BAD_REQUEST }
            customized_response['message']="Validation error"
            customized_response['data'] = {"message" : "Validation error", "form_errors" : dict(response.data.items()) }

            # for key, value in response.data.items():
            #     error = { key : value}
            #     customized_response['data']['form_errors'].append(error)
        elif response.status_code == 404:
            customized_response = {"status" : 404}
            customized_response["next"]= None
            customized_response["previous"]= None
            customized_response["message"]= "Resource Not found"
            customized_response['list']=[]
        else:
            customized_response = {"status" : response.status_code }
            customized_response['message']=response.status_text
            customized_response['data'] = {"message" : response.status_text, "errors" : dict(response.data.items())}
        response.data = customized_response
    return response



def successResponse(data, status_code):
	response = {"status": status_code, "message": "success"}
	data_dict = {}
	# for d in data:
	# 	if d != "password":
	# 		data_dict[d] = {"value":data[d], "message":"success", "status":True}
	data_dict['message'] = "success"
	data_dict['status'] = status_code
	response['data'] = data
	return response


def Custom_Queryset_Response(self,request, given_serializer ):
    try:
        queryset = self.filter_queryset(self.get_queryset())
        try:
            page = self.paginate_queryset(queryset)
        except Exception as E:
            data = {"status":400,"message":str(E),"data":{"trace":str(E)}}
            return data
        if page is not None:
            serializer = given_serializer(page, many=True,context={ 'request': request    })
            res=self.get_paginated_response(serializer.data)
            new_data= dict((res.data))
            if not new_data['results']:
                data = {"status":404,"message":"No data found","data":{'next':None,'previous':None,'count':0,'list':[]}}
            else:
                data = {"status":200,"message":"Success","data":{'next':new_data['next'],'previous':new_data['previous'],'count':new_data['count'],'list':new_data['results']}}
            return data
        else:
            data = {"status":400,"message":"Not Found"}
            return data
    except Exception as E:
        print("=-=-",E)
        data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
        return data 



def get_serializer_first_error(form):
    for key, value in form.errors.items():
        msg=str(key.capitalize()) + " - " +str(value[0])
        return [ str(key.capitalize()), str(value[0])] 