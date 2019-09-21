import os
import frontmatter
from glob import glob
from jinja2 import Template

from ..base import BaseConverter


class DevConverter(BaseConverter):

    def __init__(self, site):
        super(self.__class__, self).__init__(site, 'dev')

    def get_template(self):
        with open(os.path.join(os.path.dirname(__file__), 'dev.tmpl')) as fp:
            dev_template = Template(fp.read())
        return dev_template

    def convert(self, in_file):
        matter = self.parse_md_with_front_matter(in_file)

        if not self.should_process(matter):
            return None

        body = self.format_static_links(matter.content)
        body = self.format_image_links(body)
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
        return frontmatter.loads(body), matter
