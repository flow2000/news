//时间位移，0表示今天，1表示昨天，以此类推
let offset = 0
//获取新闻API，可根据部署域名更换
let NEWS_API = "https://news.panghai.top/60s"
//壁纸API
let BINGAPI = "https://news.panghai.top/bing"
//微博热搜API
let WEIBOAPI = "https://news.panghai.top/weibo"
//B站热搜API
let BILIAPI = "https://news.panghai.top/bili"

//js入口
get_day_news(offset);

//获取新闻
function get_day_news(offset) {
    NProgress.start();
    // 获取壁纸
    axios.get(`${BINGAPI}`)
        .then(function (response) {
            bing_list = response.data.data
            //加载壁纸
            document.getElementById('bing').src = bing_list[offset].url
        })
        .catch(function (error) {
            Notiflix.Notify.failure(`获取壁纸数据失败\uD83D\uDE1E，请点击跳转至问题反馈`, function () {
                window.open("https://github.com/flow2000/news/issues/new")
            });
            NProgress.done()
            console.log(error);
        });

    axios.get(`${NEWS_API}?offset=${offset}`)
        .then(function (response) {
            load_day_news(response.data)
            //保存当前时间(12月24日，农历腊月初二，星期六！)
            if (offset === 0) {
                localStorage.setItem('current_time', response.data.data.time)
            }
        })
        .catch(function (error) {
            Notiflix.Notify.failure(`获取壁纸数据失败\uD83D\uDE1E，请点击跳转至问题反馈`, function () {
                window.open("https://github.com/flow2000/news/issues/new")
            });
            NProgress.done()
            console.log(error);
        });
}

//加载新闻
function load_day_news(data) {
    //切换按钮文字
    btn_text = document.getElementsByClassName("switch_btn")[0].innerText
    try {
        NProgress.done();
        if (data['data']) {
            data = data['data'];
            // 加载标题
            if (data['time'].includes('月')) {
                document.getElementById('date').innerHTML = data['time'];
            } else {
                document.getElementById('date').innerHTML = '暂无数据';
            }
            // 显示通知
            try {
                const date_now = str_to_date(data['time']);
                Notiflix.Notify.success(`${date_now} 更新成功`, {
                    showOnlyTheLastOne: false,
                });
            } catch (error) {
                Notiflix.Notify.success(`更新失败`, {
                    showOnlyTheLastOne: false,
                });
            }
            // 加载weiyu
            if (data['weiyu'].includes('【微语】')) {
                document.getElementById('weiyu').innerHTML = data['weiyu'].replace("【微语】", '');
            } else {
                load_yiyan()
            }
            // 清空原有的新闻
            document.getElementById('news').innerHTML = '';
            for (let i = 0; i < data['news'].length; i++) {
                // 将其变成 li 并插入ol
                const li = document.createElement('li');
                var n = data['news'][i];
                if (n[1] === '、') {
                    n = n.substring(2);
                } else if (n[2] === '、') {
                    n = n.substring(3);
                }
                if (btn_text !== '切换至微博热搜') {
                    li.innerHTML = `<a href=${data['urls'][i]} target='_blank'>${n}</a>`;
                } else {
                    li.innerHTML = n;
                }
                // 插入新的 li
                document.getElementById('news').appendChild(li);
            }
        } else {
            Notiflix.Notify.failure(`加载新闻失败 \uD83D\uDE1E`);
        }
    }
    catch (error) {
        Notiflix.Notify.failure(`加载新闻失败 \uD83D\uDE1E`);
    }
}

// 打开新窗口
function bing_click() {
    window.open(document.getElementById('bing').src.split('_1920x1080.jpg')[0] + '_UHD.jpg');
}

//后一天
function after() {
    if (offset === 0) {
        Notiflix.Notify.success('当前已经是最新的了');
    } else {
        offset -= 1;
        direction = 'before';
        get_day_news(offset);
    }
}

//前一天
function before() {
    if (offset === 4) {
        Notiflix.Notify.warning('之后没有了');
    } else {
        offset += 1;
        direction = 'after';
        get_day_news(offset);
    }
}

//切换新闻
function change_origin() {
    current_time = localStorage.getItem("current_time")
    btn_text = document.getElementsByClassName("switch_btn")[0].innerText
    if (btn_text === '切换至微博热搜') {
        NProgress.start();
        axios.get(WEIBOAPI)
            .then(function (response) {
                var data = response.data
                var news_data = {}
                var news_title = []
                var news_url = []
                for (let i = 0; i < data['data'].length; i++) {
                    news_title.push(data['data'][i].title)
                    news_url.push(data['data'][i].url)
                }
                news_data['news'] = news_title
                news_data['urls'] = news_url
                news_data['time'] = current_time
                news_data['topic'] = '微博热搜'
                news_data['weiyu'] = ''
                data['data'] = news_data
                load_day_news(data)
            })
            .catch(function (error) {
                Notiflix.Notify.failure(`微博热搜获取失败\uD83D\uDE1E，请点击跳转至问题反馈`, function () {
                    window.open("https://github.com/flow2000/news/issues/new")
                });
                NProgress.done()
                console.log(error);
            });
        document.getElementById("news_title").innerText = '微博热搜'
        document.getElementsByClassName("before_btn")[0].style.display = "none";
        document.getElementsByClassName("after_btn")[0].style.display = "none";
        document.getElementsByClassName("switch_btn")[0].innerText = '切换至B站热搜'
    } else if (btn_text === '切换至B站热搜') {
        axios.get(BILIAPI)
            .then(function (response) {
                var data = response.data
                var news_data = {}
                var news_title = []
                var news_url = []
                for (let i = 0; i < data['data'].length; i++) {
                    news_title.push(data['data'][i].title)
                    news_url.push(data['data'][i].url)
                }
                news_data['news'] = news_title
                news_data['urls'] = news_url
                news_data['time'] = current_time
                news_data['topic'] = 'B站热搜'
                news_data['weiyu'] = ''
                data['data'] = news_data
                load_day_news(data)
            })
            .catch(function (error) {
                Notiflix.Notify.failure(`B站热搜获取失败\uD83D\uDE1E，请点击跳转至问题反馈`, function () {
                    window.open("https://github.com/flow2000/news/issues/new")
                });
                NProgress.done()
                console.log(error);
            });
        document.getElementById("news_title").innerText = 'B站热搜'
        document.getElementsByClassName("before_btn")[0].style.display = "none";
        document.getElementsByClassName("after_btn")[0].style.display = "none";
        document.getElementsByClassName("switch_btn")[0].innerText = '切换至每日早报'
    } else if (btn_text === '切换至每日早报') {
        location.reload()
    }
}

//加载一言
function load_yiyan() {
    axios.get('https://v1.hitokoto.cn/?c=k')
        .then(function (response) {
            data = response.data
            document.getElementById('weiyu').innerHTML = response.data['hitokoto'];
        })
        .catch(function (error) {
            Notiflix.Notify.failure(`获取一言失败 \uD83D\uDE1E`);
            console.log(error);
        });
}

//字符串格式的日期格式化'yyyy-mm-dd'或者'mm-dd'
function str_to_date(str) {
    const dateRegex = /(\d{4})年?(\d{1,2})月(\d{1,2})日?/;
    const matches = str.match(dateRegex);
    if (matches) {
        return `${matches[1]}-${matches[2]}-${matches[3]}`;
    } else {
        // 如果没有年份，则默认为今年
        const year = new Date().getFullYear();
        const matches = str.match(/(\d{1,2})月(\d{1,2})日?/);
        if (matches) {
            return `${year}-${matches[1]}-${matches[2]}`;
        }
    }
    return str;
}