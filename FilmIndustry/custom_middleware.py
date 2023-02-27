from django.utils.deprecation import MiddlewareMixin
from typing import Optional
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
class SampleMiddleware(MiddlewareMixin):

    def __init__(self, get_response) -> None:
        super().__init__(get_response)

    # def process_request(self,request):
    #     request.session['location'] = "Hyderabad"
    #     urls_list = ['/movie_add/','/movie_list/','/hello_api/','/cls_movieapiview/']
    #     # import pdb;pdb.set_trace()
    #     print(request.path)
    #     if 'Authorization' in request.headers:
    #         authorize = request.headers['Authorization'].split()[1]
    #         import pdb;pdb.set_trace()
    #         try:
    #             get_token = Token.objects.get(key=authorize)
    #             get_token = get_token.user
    #         except:
    #             get_token = None
    #         request.user = get_token

    #     if request.user:
    #         if request.path in urls_list:
    #             response = Response({})
    #         else:
    #             response = Response({'status':403,'message':'Access Denied'})
    #     else:
    #         response = Response({'status':403,'message':'Unauthorised'})
    #     response.accepted_renderer = JSONRenderer()
    #     response.accepted_media_type = "application/json"
    #     response.renderer_context = {}
    #     response.render()
    #     return response

