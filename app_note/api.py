from django.conf.urls import *
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.utils import trailing_slash
from django.http import Http404
import json
import re

from app_note.models import Notes
from app_note.models import HashTags


"""
Developed Api for create and fetch data for Notes and HashTags models
"""
class NotesResource(ModelResource):
    class Meta:
        queryset = Notes.objects.all().order_by("-created_on")
        resource_name = 'note'
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        limit = 1000
        max_limit = 1000
        

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/page%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_page'), name="api_get_page"),
        ]

    
    def get_page(self, request, **kwargs):
        """
        Create note record and check for any hashtag present in that description.
        """
        try:
            object_list = {}
            note_res = NotesResource()

            if request.method == "POST":
                note_data = json.loads(request.body)
                if note_data.has_key("description") and note_data["description"]:
                    note_obj = Notes(description=note_data['description'])
                    note_obj.save()
                    list_of_hash_tags = re.findall(r"\#[\w]*", note_data['description'])

                    for ele in list_of_hash_tags:
                        hashtag_obj, hashtag_created = HashTags.objects.get_or_create(tags=ele)
                        hashtag_obj.notes.add(note_obj)

                    note_all = Notes.objects.all()
                    objects = []

                    # create bundle for each objects in Notes models.
                    for result in note_all:
                        bundle = self.build_bundle(obj=result, request=request)
                        bundle = self.full_dehydrate(bundle)
                        objects.append(bundle)

                    object_list = {
                        'objects': objects,
                    }                 
                    return self.create_response(request, object_list)
                else:
                    return self.create_response(request, object_list)
            else:
                return self.create_response(request, object_list)
        except Exception as e:
            print "Exception occurred in get page api resource:" + e
            return self.create_response(request, object_list)

class HashTagsResource(ModelResource):
    notes = fields.ToManyField(NotesResource, 'notes', full=True, null=True)

    class Meta:
        queryset = HashTags.objects.all().order_by("-created_on")
        resource_name = 'hashtag'
        allowed_methods = ['get', 'post']
        