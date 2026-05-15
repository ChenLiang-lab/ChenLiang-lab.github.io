import codecs

toml = '''baseURL = 'https://ChenLiang-lab.github.io/'
theme = 'stack'
defaultContentLanguage = 'zh-cn'
title = 'ChenLiang-lab\u7684\u6280\u672f\u535a\u5ba2'

[menu]
  [[menu.main]]
    identifier = 'home'
    name = '\u9996\u9875'
    url = '/'
    weight = 1
    [menu.main.params]
      icon = 'home'
  [[menu.main]]
    identifier = 'posts'
    name = '\u5f52\u6863'
    url = '/post/'
    weight = 3
    [menu.main.params]
      icon = 'archives'
  [[menu.main]]
    identifier = 'tags'
    name = '\u6807\u7b7e'
    url = '/tags/'
    weight = 4
    [menu.main.params]
      icon = 'tag'

[pagination]
    pagerSize = 5

[permalinks]
    post = '/:slug/'

[params]
  mainSections = ['post']

  [params.footer]
    since = 2026

  [params.sidebar]
    compact = false

  [params.article]
    toc = true
    readingTime = true
    [params.article.list]
      showTags = true

  [params.widgets]
    homepage = [
      { type = 'search' },
      { type = 'recent-posts', params = { limit = 5 } },
      { type = 'categories', params = { limit = 10 } }
    ]
    page = [
      { type = 'toc' },
      { type = 'categories', params = { limit = 10 } },
      { type = 'archives', params = { limit = 10 } },
      { type = 'tag-cloud' }
    ]

  [params.colorScheme]
    toggle = true
    default = 'auto'

  [params.imageProcessing]
    [params.imageProcessing.content]
      widths = [800, 1600, 2400]
      enabled = true
    [params.imageProcessing.thumbnail]
      enabled = true

[outputs]
  home = ['HTML', 'RSS', 'JSON']
  section = ['HTML', 'RSS']
'''

with codecs.open('E:/DeveloperSpace/Codex/Blog/hugo.toml', 'w', 'utf-8') as f:
    f.write(toml)
print('hugo.toml updated')
