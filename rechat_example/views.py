from typing import Union
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.contrib.auth.views import LoginView, redirect_to_login


class IndexView(LoginView):
    template_name = "index.html"

    def dispatch(
        self, request, *args, **kwargs
    ) -> Union[HttpResponseRedirect, HttpResponseBase]:
        if self.request.user.is_authenticated is False:  # type: ignore
            return redirect_to_login("/", "/login/")
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class LoginView(LoginView):
    template_name = "login_form.html"
