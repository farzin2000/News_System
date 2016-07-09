from pydoc import Doc
from mongoengine import *
import datetime
# Create your models here.


class Tag(EmbeddedDocument, Document):
    name = StringField(max_length=20)


class Category(EmbeddedDocument, Document):
    name = StringField(max_length=20)


class ImageGallery(EmbeddedDocument):
    images = ListField(ImageField())


class Comment(EmbeddedDocument):
    comment = StringField(max_length=60)
    user_id = IntField()
    username = StringField()
    date = DateTimeField(default=datetime.datetime.now)


class News(Document):
    my_id = IntField()
    image = ImageField(default='news-image.jpg')
    date = DateTimeField(default=datetime.datetime.now)
    title = StringField(max_length=60)
    source = StringField(max_length=60)
    categories = ListField(EmbeddedDocumentField(Category))
    tags = ListField(EmbeddedDocumentField(Tag))
    abstract = StringField(max_length=600)
    content = StringField()
    gallery = EmbeddedDocumentField(ImageGallery)
    comments = ListField(EmbeddedDocumentField(Comment))
    relative_news = ListField(IntField())
    views = IntField()








