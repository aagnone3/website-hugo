import os
import re
from glob import glob
from abc import abstractmethod

import frontmatter


class BaseConverter(object):

    def __init__(self, site, name):
        self.site = site
        self.name = name

    def should_process(self, matter):
        return self.name in matter.get('platforms', list())

    def format_static_links(self, body):
        '''
        # one example
        {{% staticref "files/atlanta_heatmap.html" "newtab" %}}
        generated webpage
        {{% /staticref %}}

        # another example
        {{% staticref "files/atlanta_heatmap.html" %}}generated webpage{{% /staticref %}}
        '''
        return re.sub(
            r'{{% staticref "(.*)\.([a-zA-Z0-9_]+)".*%}}\n?(.*)\n?{{% /staticref %}}',
            r'[\3]({site_name}/\1.\2)'.format(site_name=self.site),
            body
        )

    @abstractmethod
    def get_template(self):
        pass

    @staticmethod
    def parse_md_with_front_matter(file_path):
        with open(file_path, 'r') as fp:
            body_in = fp.read()
        matter = frontmatter.loads(body_in)
        return matter

    @staticmethod
    def get_image_ext(in_file):
        post_dir = os.path.dirname(in_file)
        files = glob(os.path.join(post_dir, 'featured*'))
        if len(files) == 0:
            raise OSError('No featured image found in {}.'.format(post_dir))
        if len(files) > 1:
            print('Multiple featured images found in {}. Using {}.'.format(post_dir, files[0]))
        return os.path.splitext(files[0])[1], post_dir

    @abstractmethod
    def convert(self, in_file):
        pass
