from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from fotos.models import Photo
# Create your views here.
from django.http import HttpResponse
from eventos.models import Event


class EventList(ListView):
    model = Event
    context_object_name = 'disponible_events'


# class EventDetail(DetailView):
#     model = Event
#
#      def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(EventDetail, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['photo_list'] = Photo.objects.all()
#         return context


class EventPhotoList(ListView):
    template_name = 'eventos/photo_by_event.html'

    context_object_name = 'disponible_photos'

    def get_queryset(self):
        self.event = get_object_or_404(Event, id=self.args[0])
        return Photo.objects.filter(event__id=self.event.id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventPhotoList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['event'] = self.event
        return context