import os
import re
from argparse import ArgumentParser

from github import Github
from github.InputFileContent import InputFileContent


def gistify(title, in_file, test=False):

    # load the markdown from the file
    with open(in_file, 'r') as fp:
        body = fp.read()

    # extract code snippets from the text body
    # captured = re.findall(r'```bash\n[\s\S]*?\n```', body)
    captured = re.findall(r'```[a-zA-Z]*\n[\s\S]*?\n```', body)

    # make gists for each snippet
    g = Github(os.environ['GITHUB_GIST_TOKEN'])
    user = g.get_user()
    gist_urls = list()
    for i, snippet in enumerate(captured):
        print('{}/{}'.format(i + 1, len(captured)))
        if not test:
            gist_urls.append(
                user.create_gist(
                    public=True,
                    description='{}_{}'.format(title, i + 1),
                    files={0: InputFileContent(snippet)}
                ).html_url
            )
        else:
            sep = '=' * 30
            print(sep)
            print(snippet)
            print(sep)
    return gist_urls


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(dest='title', help='Name of the article')
    parser.add_argument(dest='in_file', help='Path to markdown text file')
    parser.add_argument('-t', '--test', help='Test mode (only print matching code blocks', required=False,
                        default=False, action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    urls = gistify(args.title, args.in_file, test=args.test)
    print(urls)
