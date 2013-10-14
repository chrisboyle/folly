from mezzanine.conf import settings
from mezzanine.blog.models import BlogPost
from django.template import Context, loader

MAGIC = '_LATEST_BLOG_POST_'

def add_latest_post(content):
	settings.use_editable()
	if MAGIC not in content: return content

	out = 'Error loading latest blog post'
	posts = BlogPost.objects.published().select_related()
	#try:
	post = posts[0]
	t = loader.get_template('homeblocks/latest_post.html')
	out = t.render(Context({'blog_post':post}))
	#except:
	#	pass

	return content.replace(MAGIC, out)

