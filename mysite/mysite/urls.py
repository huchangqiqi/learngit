"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from web.views import add, home, person, board,postmessage,current_time

urlpatterns = [
    url(r'^polls',include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^time/',current_time),
    url(r'^add/(\d+)/(\d+)',add),
    url(r'^home',home),
    url(r'^person',person),
    url(r'^board',board,name='board'),
    url(r'^postmessage/$',postmessage,name='postmessage')

]
