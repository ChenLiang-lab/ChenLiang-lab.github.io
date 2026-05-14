import os
os.makedirs('E:/DeveloperSpace/Codex/Blog/content/page/about', exist_ok=True)
os.makedirs('E:/DeveloperSpace/Codex/Blog/content/page/search', exist_ok=True)

hugo = '''baseURL = 'https://ChenLiang-lab.github.io/'
theme = 'stack'
defaultContentLanguage = 'zh-cn'
title = 'ChenLiang-lab\u7684\u6280\u672f\u535a\u5ba2'

[menu]
  [[menu.main]]
    identifier = 'home'
    name = '\u9996\u9875'
    url = '/'
    weight = 1
  [[menu.main]]
    identifier = 'posts'
    name = '\u5f52\u6863'
    url = '/post/'
    weight = 3
  [[menu.main]]
    identifier = 'tags'
    name = '\u6807\u7b7e'
    url = '/tags/'
    weight = 4

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
      { type = 'recent-posts', params = { limit = 5 } }
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

about = '''---
title: "\u5173\u4e8e\u6211"
description: "\u8ba4\u8bc6\u535a\u5ba2\u4f5c\u8005"
date: 2026-05-14
slug: about
menu:
    main:
        weight: -90
        params:
            icon: user
---

## \u5173\u4e8e\u672c\u7ad9

\u8fd9\u662f\u4e00\u4e2a Hugo + Stack \u535a\u5ba2\u3002

## \u5173\u4e8e\u6211

\u4e00\u4f4d\u5168\u6808\u5f00\u53d1\u8005\u3002

## \u8054\u7cfb\u6211

- GitHub: [github.com/ChenLiang-lab](https://github.com/ChenLiang-lab)
- Email: ChenLiang.lab@gmail.com
'''

search = '''---
title: "\u641c\u7d22"
layout: search
outputs:
    - html
    - json
slug: search
menu:
    main:
        weight: -60
        params:
            icon: search
---
'''

with open('E:/DeveloperSpace/Codex/Blog/hugo.toml', 'w', encoding='utf-8') as f:
    f.write(hugo.strip() + '\n')
with open('E:/DeveloperSpace/Codex/Blog/content/page/about/index.md', 'w', encoding='utf-8') as f:
    f.write(about.strip() + '\n')
with open('E:/DeveloperSpace/Codex/Blog/content/page/search/index.md', 'w', encoding='utf-8') as f:
    f.write(search.strip() + '\n')
print('All written')
