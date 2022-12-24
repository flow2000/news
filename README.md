# 每日早报

![news](https://socialify.git.ci/flow2000/news/image?description=1&descriptionEditable=60%E7%A7%92%E8%AF%BB%E6%87%82%E4%B8%96%E7%95%8C%EF%BC%8C%E6%94%AF%E6%8C%81%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%EF%BC%8C%E5%BF%AB%E9%80%9F%E7%94%9F%E6%88%90%E6%8E%A5%E5%8F%A3%E6%95%B0%E6%8D%AE&font=Inter&language=1&logo=https%3A%2F%2Fnews.panghai.top%2Ffavicon.svg&name=1&owner=1&pattern=Formal%20Invitation&stargazers=1&theme=Light)

### 简介

60秒读懂世界！

### 效果

#### v1

![v1](https://static.panghai.top/img/screenshot/news.panghai.top-v1.png)

#### v2

![v2](https://static.panghai.top/img/screenshot/news.panghai.top-v2.png)

#### Vercel 一键部署（推荐）

#### v1

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/flow2000/news/tree/v1)

#### v2

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/flow2000/news/tree/v2)

### Docker 一键部署

#### v1

```markdown
docker run -itd --name=news --restart=always -p 9134:8888 flow2000/news:1.0.0
```

#### v2

```markdown
docker run -itd --name=news --restart=always -p 9134:8888 flow2000/news:2.0.0
```

### API

GET：`https://news.panghai.top/60s`，返回今日新闻json数据

##### 请求参数

| 参数名           | 位置  | 类型   | 必填 | 示例值 |说明  |
| :--------------- | :---- | :----- | :--: | :--------------------- | :--------------------- |
| `offset` | `query` | `int` |  否  | `0` |说明：`0` 为今天，`1` 为昨天，依次类推                            |

GET：`https://news.panghai.top/weibo`，返回微博热搜json数据

##### 请求参数：无

GET：`https://news.panghai.top/bili`，返回B站热搜json数据

##### 请求参数：无

GET：`https://news.panghai.top/bing`，返回必应热搜json数据

##### 请求参数：无

更多详情请点击：[每日早报API](https://news.panghai.top/docs)

