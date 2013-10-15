from mezzanine.blog.views import blog_post_feed
from django.contrib.sites.models import get_current_site
import re

def feed(request, *args, **kwargs):
	"""Fully qualify all links/image URLS, because RSS readers don't."""
	qual = u'https' if request.is_secure() else u'http'
	qual += '://' + get_current_site(request).domain
	response = blog_post_feed(request, *args, **kwargs)
	u = unicode(response.content,'utf-8')
	edited = re.sub(r'\b((?:href|src)=["\'])/', r'\1%s/' % qual, u)
	response.content = edited.encode('utf-8')
	return response
