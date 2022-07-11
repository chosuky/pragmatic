from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator

from articleapp.models import Article

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated