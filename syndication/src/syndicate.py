from argparse import ArgumentParser

from tools import api_factory, converter_factory


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(dest='in_file', help='Path to Markdown file in Hugo format')
    parser.add_argument(dest='out_file', help='Desired path to Markdown file in dev.to format')
    return parser.parse_args()


def persist(article, out_file):
    # TODO persist non-body fields also?
    with open(out_file, 'w') as fp:
        fp.write(article.content)


def main():
    args = parse_args()

    # initialize the API and article converter classes
    for name, api_cls in api_factory.items():
        print(name)
        api = api_cls()
        converter = converter_factory[name]('https://anthonyagnone.com')

        # convert, persist, and post the article
        post, summary = converter.convert(args.in_file)
        persist(post, args.out_file)
        api.post(post, summary)


if __name__ == '__main__':
    main()
