import requests

from datetime import date
from datetime import timedelta


def get_last_week_data():
    today = date.today()
    return today - timedelta(weeks=1)


def get_trending_repositories(top_size=20):
    r = requests.get('https://api.github.com/search/repositories',
                     params={'q': 'created:>%s' % get_last_week_data(),
                             'sort': 'stars',
                             'order': 'desc'})
    return list(r.json()['items'])[:top_size]


def print_trending_repositories(trending_repositories):
    print(u'stars name open_issues_count url')
    for repositories in trending_repositories:
        print(u'%s %s %s URL:%s' % (repositories['stargazers_count'],
                                    repositories['name'],
                                    repositories['open_issues_count'],
                                    repositories['html_url'],))


if __name__ == '__main__':
    trending_repositories = get_trending_repositories()
    print_trending_repositories(trending_repositories)
