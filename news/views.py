from django.shortcuts import render, render_to_response
from news.models import Comment, News, Tag
import json

# Create your views here.


def test(request):

    # tag2 = Tag(name="3d")
    # tag2.save()
    #
    # news = News(my_id = 1, content="lorem ipsum lorem,lorem, ipsum lorem ipsum lorem,lorem, ipsum lore ipsum lorem,lorem, ipsum",
    #             abstract="lorem ipsum test and done", title="lorem", views=102)
    # news.tags.append(tag1)
    # news.save()
    # news.tags.append(tag2)
    # news.save()


    context = {
        'user': request.user,
        'news': News.objects().first(),
        'tags': Tag.objects.all()
    }
    return render(request, 'main.html', context)
