from django.http import HttpResponse, Http404
from django.template import loader
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('gymkhana/index.html')
    context = {
        'all_albums':all_albums,
    }

    #for album in all_albums:
    #    url = "/music/" + str(album.id) + "/"
    #    html +=  '<a href="' + url +'">' + album.album_title + '</a></br>'

    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Hey beyotch")

    return HttpResponse(template.render(context, request))