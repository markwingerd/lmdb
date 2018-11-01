# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from music.models import Artist


def index(request):
    if request.method == 'GET':
        artists = Artist.objects.all().order_by('name')
        return render(request, 'index.html', {'artists': artists})
    elif request.method == 'POST':
        # Validation
        name = request.POST.get('name')
        if not name:
            return render(request, 'index.html', {
                'artists': artists,
                'error_message': 'Name invalid',
            })
        artist = Artist.objects.create(name=name)
        artist.save()
        return HttpResponseRedirect(reverse('music:detail', args=(artist.id,)))


def detail(request, artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    content = {
        'artist': artist,
        'albums': artist.album_set.all().order_by('name'),
        'links': artist.link_set.all(),
    }

    if request.method == "GET":
        return render(request, 'detail.html', content)

    elif request.method == "POST":
        # Validation
        name = request.POST.get('name')
        url = request.POST.get('url')
        if not name or not url:
            content['error_message'] = 'Missing name or url'
            return render(request, 'detail.html', content)
        link = artist.link_set.create(name=name, url=url)
        link.save()
        artist.save()
        return render(request, 'detail.html', content)
