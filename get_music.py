def get_list(name):
    #选择浏览器的类型
    chrome_options = Options()
    # 设置chrome浏览器无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = "https://music.163.com/#/search/m/?s=" + name + "type=1"

    # 链接相关url网站
    browser.get(url)
    # 切换到iframe网页中
    browser.switch_to.frame(browser.find_element_by_id("g_iframe"))
    # 查找相应的和html代码
    data = browser.find_element_by_class_name("srchsongst").find_elements_by_class_name("item")

    #创建一个list用来保存数据
    dlist = {}
    for i in range(len(data)):
        d = data[i].find_element_by_class_name("w0")
        id = d.find_element_by_tag_name("a").get_attribute("href").split('=')[1]
        name = d.find_element_by_tag_name("b").get_attribute("title")
        id_name = data[i].find_element_by_class_name("w1").text
        radio = data[i].find_element_by_class_name("w2").text
        dlist[i+1] = [id,name,id_name,radio]

    return dlist


#获取要下载的歌曲的id
def get_num(data):
    for key in data:
        print(key,end = "  ")
        for i in range(len(data[key])):
            if i != 0:
                print(data[key][i],end = "  ")
        print()
    num = input("前输入要下载的歌曲的编号或输入0进行全部下载:")
    return num

#下载歌曲
def downLoad(num,data):
    num = int(num)
    headers = {
        'Referer': 'https://music.163.com/search/',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    url = "http://music.163.com/song/media/outer/url?id="
    if num == 0:
        #下载全部
        for key in data:
            name = data[key][1] + "_" + data[key][2] + data[key][3] + ".mp3"
            name = name.replace("/", " ") if "/" in name else name
            urlId = "http://music.163.com/song/media/outer/url?id=" + data[key][0] + ".mp3"
            with open("m/" + name, "wb") as f:
                f.write(requests.get(urlId, headers=headers).content)
    else:
        print(data[num])
        #下载指定
        name = data[num][1]+"_"+data[num][2]+data[num][3] +".mp3"
        urlId = "http://music.163.com/song/media/outer/url?id=" + data[num][0] + ".mp3"
        name = name.replace("/"," ") if "/" in name else name
        print(name)
        with open("m/"+ name, "wb") as f:
            f.write(requests.get(urlId, headers=headers).content)


if __name__ == "__main__":
    name = input("请输入歌名的名字:")
    data = get_list(name)
    get_m = get_num(data)
    downLoad(get_m,data)
