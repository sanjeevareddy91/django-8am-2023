from django.utils.deprecation import MiddlewareMixin
from typing import Optional
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
class SampleMiddleware(MiddlewareMixin):

    def __init__(self, get_response) -> None:
        super().__init__(get_response)

    def process_request(self,request):
        request.session['location'] = "Hyderabad"
        urls_list = ['/movie_add/','/movie_list/','/hello_api/']
        print(request.path)
        if request.path in urls_list:
            response = Response({})
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
        else:
            response = Response({'status':403,'message':'Unauthorised'})
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
        print(request)