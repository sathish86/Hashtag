from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import


from app_note.api import NotesResource
from app_note.api import HashTagsResource

v1_api = Api(api_name='v1')
v1_api.register(NotesResource())
v1_api.register(HashTagsResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'note_hashtag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),   
    url(r'^notes/', include('app_note.urls')), # ADD THIS NEW TUPLE! 
)


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
