from tastypie.resources import ModelResource
from .models import Post

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'

    def dehydrate(self, bundle):
        bundle.data['publish_date'] = bundle.data['publish_date'].strftime("%b %d %Y")
        return bundle