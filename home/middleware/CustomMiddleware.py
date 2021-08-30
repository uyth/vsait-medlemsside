from urllib.parse import urlparse
from django.http import Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import resolve
from django.utils.http import urlquote

class CustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        redirect = self.process_request(request)
        if redirect:
            return redirect
        return response

    def process_request(self, request):
        if request.path_info != "/":
            if not is_valid_path(request.path_info):
                new_path = request.path_info
                if new_path.startswith("//"):
                    new_path = new_path[1:]
                if not new_path.endswith("/"):
                    new_path += "/"
                if is_valid_path(new_path):
                    if request.get_host():
                        new_url = "{}://{}{}".format('https' if request.is_secure() else 'http', request.get_host(), urlquote(new_path))
                    else:
                        new_url = urlquote(new_path)
                    if request.GET:
                        new_url += "?" + request.META['QUERY_STRING']
                    return HttpResponsePermanentRedirect(new_url)



def is_valid_path(path):
    try:
        url = urlparse(path)[2]
        match = resolve(url)
        print(match)
        if match.url_name == 'index' and match.app_names[0] == "home" and path != "/" and path != "/admin/":
            return False
        return True
    except Exception:
        return False
