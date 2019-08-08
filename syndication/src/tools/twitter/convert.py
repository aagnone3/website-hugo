import os
import frontmatter
from jinja2 import Template

from ..base import BaseConverter


class TwitterConverter(BaseConverter):

    def __init__(self, site):
        super(self.__class__, self).__init__(site)

    def get_template(self):
        with open(os.path.join(os.path.dirname(__file__), 'twitter.tmpl')) as fp:
            dev_template = Template(fp.read())
        return dev_template

    def convert(self, in_file):
        matter = self.parse_md_with_front_matter(in_file)
        body = self.format_static_links(matter.content)
        image_ext, post_dir = self.get_image_ext(in_file)

        body = self.get_template().render(
            title=matter['title'],
            subtitle=matter['subtitle'],
            published='false',
            tags=matter['tags'],
            cover_image='{site_name}/blog{slug}/featured{ext}'.format(site_name=self.site, slug=matter['slug'], ext=image_ext),
            canonical_url='{site_name}/blog/{title}'.format(site_name=self.site, title=post_dir.split(os.path.sep)[-1]),
            body=body
        )
        return frontmatter.loads(body), matter['summary']
