from os import path
from argparse import ArgumentParser

from tools import api_factory


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        dest='in_file',
        help='Path to Markdown file in Hugo format'
    )
    parser.add_argument(
        '-d',
        '--deploy',
        dest='deploy',
        type=int,
        required=False,
        default=0,
        help='Whether this is a deploy.'
    )
    args = parser.parse_args()
    args.deploy = bool(int(args.deploy))
    return args


def persist(article, out_file):
    # TODO persist non-body fields also?
    with open(out_file, 'w') as fp:
        fp.write(article.content)


def make_out_file(in_file, site):
    '''
    ex: (content/post/<name>/index.md, <site>) -> syndication/posts/<site>/<name>
    '''
    name = path.dirname(path.abspath(in_file)).split('/')[-1]
    return path.join('syndication/posts/{site}/{name}'.format(site=site, name=name)) + '.md'


def main():
    args = parse_args()

    # initialize the API and article converter classes
    for site, (api_cls, converter_cls) in api_factory.items():
        api = api_cls()
        converter = converter_cls('https://anthonyagnone.com')

        # convert, persist, and post the article
        returned = converter.convert(args.in_file)
        if returned is not None:
            post, summary = returned
            persist(post, make_out_file(args.in_file, site))
            if args.deploy:
                print('Deploying to {}'.format(site))
                api.post(post, summary)
            else:
                print('Deploy flag down --> not deploying to {}'.format(site))
        else:
            print('Per configuration, not deploying to {}'.format(site))


if __name__ == '__main__':
    main()
