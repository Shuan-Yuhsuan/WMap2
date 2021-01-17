'''
packages used
--- These are preinstalled ---
# pip install urllib.request
# pip install json
# pip install ssl
# pip install random
# pip install math
# pip install csv

--- These need to be installed ---
pip install pandas
pip install plotly.express
pip install geopandas

pip install dash
pip install dash_core_components
pip install dash_bootstrap_components
pip install dash_html_components
'''


'''

TO be improved:
1. 運作速度優化
    https://dash-leaflet.herokuapp.com/#us_states

    Try Layers
    https://plotly.com/python/mapbox-layers/
V 2. 版面配置
V 3. 加上詳細天氣資料，作為 hover data
V 4. 配色
V 5. 在地圖上顯示所在鄉鎮、推薦鄉鎮
X 6. 隨機推薦按鈕
7. / 縣市邊界 / out of range
'''

# 所有行政區清單
district_list = ['中正區(臺北市)', '大同區', '中山區(臺北市)', '萬華區', '信義區(臺北市)',
                 '松山區', '大安區(臺北市)',
                 '南港區', '北投區', '內湖區', '士林區', '文山區', '板橋區', '新莊區', '泰山區',
                 '林口區', '淡水區', '金山區', '八里區', '萬里區', '石門區', '三芝區', '瑞芳區',
                 '汐止區', '平溪區', '貢寮區', '雙溪區', '深坑區', '石碇區', '新店區', '坪林區',
                 '烏來區', '中和區', '永和區', '土城區', '三峽區', '樹林區', '鶯歌區', '三重區',
                 '蘆洲區', '五股區', '仁愛區', '中正區(基隆市)', '信義區(基隆市)', '中山區(基隆市)',
                 '安樂區', '暖暖區',
                 '七堵區', '桃園區', '中壢區', '平鎮區', '八德區', '楊梅區', '蘆竹區', '龜山區',
                 '龍潭區', '大溪區', '大園區', '觀音區', '新屋區', '復興區', '竹北市', '竹東鎮',
                 '新埔鎮', '關西鎮', '峨眉鄉', '寶山鄉', '北埔鄉', '橫山鄉', '芎林鄉', '湖口鄉',
                 '新豐鄉', '尖石鄉', '五峰鄉', '東區(新竹市)', '北區(新竹市)', '香山區', '苗栗市', '通霄鎮',
                 '苑裡鎮', '竹南鎮', '頭份市', '後龍鎮', '卓蘭鎮', '西湖鄉', '頭屋鄉', '公館鄉',
                 '銅鑼鄉', '三義鄉', '造橋鄉', '三灣鄉', '南庄鄉', '大湖鄉', '獅潭鄉', '泰安鄉',
                 '中區', '東區(臺中市)', '南區(臺中市)', '西區(臺中市)', '北區(臺中市)',
                 '北屯區', '西屯區', '南屯區', '太平區',
                 '大里區', '霧峰區', '烏日區', '豐原區', '后里區', '東勢區', '石岡區', '新社區',
                 '和平區', '神岡區', '潭子區', '大雅區', '大肚區', '龍井區', '沙鹿區', '梧棲區',
                 '清水區', '大甲區', '外埔區', '大安區(臺中市)', '南投市', '埔里鎮', '草屯鎮', '竹山鎮',
                 '集集鎮', '名間鄉', '鹿谷鄉', '中寮鄉', '魚池鄉', '國姓鄉', '水里鄉', '信義鄉',
                 '仁愛鄉', '彰化市', '員林市', '和美鎮', '鹿港鎮', '溪湖鎮', '二林鎮', '田中鎮',
                 '北斗鎮', '花壇鄉', '芬園鄉', '大村鄉', '永靖鄉', '伸港鄉', '線西鄉', '福興鄉',
                 '秀水鄉', '埔心鄉', '埔鹽鄉', '大城鄉', '芳苑鄉', '竹塘鄉', '社頭鄉', '二水鄉',
                 '田尾鄉', '埤頭鄉', '溪州鄉', '斗六市', '斗南鎮', '虎尾鎮', '西螺鎮', '土庫鎮',
                 '北港鎮', '莿桐鄉', '林內鄉', '古坑鄉', '大埤鄉', '崙背鄉', '二崙鄉', '麥寮鄉',
                 '臺西鄉', '東勢鄉', '褒忠鄉', '四湖鄉', '口湖鄉', '水林鄉', '元長鄉', '太保市',
                 '朴子市', '布袋鎮', '大林鎮', '民雄鄉', '溪口鄉', '新港鄉', '六腳鄉', '東石鄉',
                 '義竹鄉', '鹿草鄉', '水上鄉', '中埔鄉', '竹崎鄉', '梅山鄉', '番路鄉', '大埔鄉',
                 '阿里山鄉', '東區(嘉義市)', '西區(嘉義市)', '中西區', '東區(臺南市)', '南區(臺南市)',
                 '北區(臺南市)', '安平區', '安南區',
                 '永康區', '歸仁區', '新化區', '左鎮區', '玉井區', '楠西區', '南化區', '仁德區',
                 '關廟區', '龍崎區', '官田區', '麻豆區', '佳里區', '西港區', '七股區', '將軍區',
                 '學甲區', '北門區', '新營區', '後壁區', '白河區', '東山區', '六甲區', '下營區',
                 '柳營區', '鹽水區', '善化區', '大內區', '山上區', '新市區', '安定區', '楠梓區',
                 '左營區', '鼓山區', '三民區', '鹽埕區', '前金區', '新興區', '苓雅區', '前鎮區',
                 '小港區', '旗津區', '鳳山區', '大寮區', '鳥松區', '林園區', '仁武區', '大樹區',
                 '大社區', '岡山區', '路竹區', '橋頭區', '梓官區', '彌陀區', '永安區', '燕巢區',
                 '田寮區', '阿蓮區', '茄萣區', '湖內區', '旗山區', '美濃區', '內門區', '杉林區',
                 '甲仙區', '六龜區', '茂林區', '桃源區', '那瑪夏區', '屏東市', '潮州鎮', '東港鎮',
                 '恆春鎮', '萬丹鄉', '長治鄉', '麟洛鄉', '九如鄉', '里港鄉', '鹽埔鄉', '高樹鄉',
                 '萬巒鄉', '內埔鄉', '竹田鄉', '新埤鄉', '枋寮鄉', '新園鄉', '崁頂鄉', '林邊鄉',
                 '南州鄉', '佳冬鄉', '琉球鄉', '車城鄉', '滿州鄉', '枋山鄉', '霧臺鄉', '瑪家鄉',
                 '泰武鄉', '來義鄉', '春日鄉', '獅子鄉', '牡丹鄉', '三地門鄉', '宜蘭市', '羅東鎮',
                 '蘇澳鎮', '頭城鎮', '礁溪鄉', '壯圍鄉', '員山鄉', '冬山鄉', '五結鄉', '三星鄉',
                 '大同鄉', '南澳鄉', '花蓮市', '鳳林鎮', '玉里鎮', '新城鄉', '吉安鄉', '壽豐鄉',
                 '秀林鄉', '光復鄉', '豐濱鄉', '瑞穗鄉', '萬榮鄉', '富里鄉', '卓溪鄉', '臺東市',
                 '成功鎮', '關山鎮', '長濱鄉', '海端鄉', '池上鄉', '東河鄉', '鹿野鄉', '延平鄉',
                 '卑南鄉', '金峰鄉', '大武鄉', '達仁鄉', '綠島鄉', '蘭嶼鄉', '太麻里鄉', '馬公市',
                 '湖西鄉', '白沙鄉', '西嶼鄉', '望安鄉', '七美鄉', '金城鎮', '金湖鎮', '金沙鎮',
                 '金寧鄉', '烈嶼鄉', '烏坵鄉', '南竿鄉', '北竿鄉', '莒光鄉', '東引鄉']

# 縣市清單
ciyt_list = ["桃園市", "基隆市", "臺北市", "新北市", "新竹縣", "苗栗縣", "新竹市", "彰化縣",
             "南投縣", "臺中市", "雲林縣", "嘉義縣", "臺南市", "嘉義市", "屏東縣", "高雄市",
             "宜蘭縣", "臺東縣", "花蓮縣", "連江縣", "金門縣", "澎湖縣"]

# 有同樣名稱的鄉鎮市區
list_samename_township = ["大安區", "信義區", "中正區", "中山區", "東區", "南區", "西區", "北區"]

'''
爬蟲部分，得到各鄉鎮的天氣
d_township_data = dict()

# print(d_township_data.get("中正區(臺北市)"))
#  [['2021-01-03', 0, '16至19', '60%', '無資料'], ['2021-01-04', 1, '16至21', '50%', '50'], ['2021-01-04', 2, '17至19', '90%', '50'], ['2021-01-05', 3, '16至19', '90%', '50'], ['2021-01-05', 4, '14至16', '90%', '50'], ...]

'''

# 爬蟲部分開始

import urllib.request as ur
import json
import ssl  # 處理網路連線

ssl._create_default_https_context = ssl._create_unverified_context


def set_url_weather(f_type_data):
    # 依照使用者需求給定不同之資料網址（用於查詢天氣資訊）
    f_url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/" + f_type_data + "?Authorization=CWB-98F06B22-A29A-4815-AF40-B5D1DE31536D&elementName=WeatherDescription"
    return (f_url)


def web_crawler_weather(f_url):
    # 爬蟲
    f_site = ur.urlopen(f_url)
    f_page = f_site.read()
    f_contents = f_page.decode()
    f_data = json.loads(f_contents)
    return f_data


# print("請稍等，程式運作中...")
condition = "2"

# 以下為空汙的部分
url = "https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000001?sort=PublishTime&offset=0&limit=1000"
data = str(web_crawler_weather(url))
data = data.split("Content")

# 空汙數據中簡稱所代表之全部縣市層級行政單位
d_city_contrast = {"北部": ["桃園市", "基隆市", "臺北市", "新北市"], "竹苗": ["新竹縣", "苗栗縣", "新竹市"], "中部": ["彰化縣", "南投縣", "臺中市"],
                   "雲嘉南": ["雲林縣", "嘉義縣", "臺南市", "嘉義市"], "高屏": ["屏東縣", "高雄市"], "宜蘭": ["宜蘭縣"], "花東": ["臺東縣", "花蓮縣"],
                   "馬祖": ["連江縣"], "金門": ["金門縣"], "澎湖": ["澎湖縣"]}
d_counties_airpollution = {}  # 縣市對應到空汙數據（AQI、預測之日期）
d_airpollution_recordday = {}  # 空氣污染預報中有預報到的日期，主要是供與下方氣象資訊合併時使用

# 從爬到的文字中取出需要的部分，並將其結合成一段字串，以利後續分析
d_tmp = {}
for count_1 in range(2, len(data)):
    area = data[count_1][data[count_1].find("Area") + 8:data[count_1].find("MajorPollutant") - 4]
    AQI = data[count_1][data[count_1].find("AQI") + 7:data[count_1].find("ForecastDate") - 4]
    time = data[count_1][data[count_1].find("ForecastDate") + 16:data[count_1].find("MinorPollutant") - 4]
    tmp = str(AQI) + "," + str(time)
    if area not in d_tmp:
        d_tmp[area] = tmp
    else:
        d_tmp[area] += "rrr" + tmp

# 建立日期與距離現在第幾天的dict
for count_1 in range(2, 5):
    time = data[count_1][data[count_1].find("ForecastDate") + 16:data[count_1].find("MinorPollutant") - 4]
    d_airpollution_recordday[str(time)] = count_1 - 2

l_area = ["北部", "竹苗", "中部", "雲嘉南", "高屏", "宜蘭", "花東", "馬祖", "金門", "澎湖"]
for count_1 in range(0, len(l_area)):
    # 把前面用字串串連起來的資料拆解成list
    d_tmp[l_area[count_1]] = d_tmp[l_area[count_1]].split("rrr")
    for count_2 in range(0, len(d_tmp[l_area[count_1]])):
        d_tmp[l_area[count_1]][count_2] = d_tmp[l_area[count_1]][count_2].split(",")

    # 把區域代換成各縣市名稱
    l_tmp = d_city_contrast[l_area[count_1]]
    for count_2 in range(0, len(l_tmp)):
        d_counties_airpollution[l_tmp[count_2]] = d_tmp[l_area[count_1]]

# 以下為天氣的部分
d_township_data = {}  # 鄉鎮市區對應到相應之天氣，型態為dictionary，keys為各鄉鎮市區的名稱，values則為一個裝載天氣資訊的list。  list的結構中第一層是時間（0代表當下的天氣預報，1代表之後3／6小時的天氣預報...），第二層則是（溫度，雨量）
d_township_counties = {}  # 鄉鎮市區對應到縣市，型態為dictionary，keys為各鄉鎮市區的名稱，values則為鄉鎮市所述的縣市名稱
d_township_lat_lon = {}  # 鄉鎮市區的經緯度座標，型態為dictionary，keys為各鄉鎮市區的名稱，values則為一個裝載經緯度的list。 (經度，緯度)

list_city_72hr = ["F-D0047-001", "F-D0047-005", "F-D0047-009", "F-D0047-013", "F-D0047-017", "F-D0047-021",
                  "F-D0047-025", "F-D0047-029", "F-D0047-033", "F-D0047-037", "F-D0047-041", "F-D0047-045",
                  "F-D0047-049", "F-D0047-053", "F-D0047-057", "F-D0047-061", "F-D0047-065", "F-D0047-069",
                  "F-D0047-073", "F-D0047-077", "F-D0047-081",
                  "F-D0047-085"]  # 代碼與縣市對照表 F-D0047-001(宜蘭縣),F-D0047-005(桃園市),F-D0047-009(新竹縣),F-D0047-013(苗栗縣),F-D0047-017(彰化縣),F-D0047-021(南投縣),F-D0047-025(雲林縣),F-D0047-029(嘉義縣),F-D0047-033(屏東縣),F-D0047-037(臺東縣),F-D0047-041(花蓮縣),F-D0047-045(澎湖縣),F-D0047-049(基隆市),F-D0047-053(新竹市),F-D0047-057(嘉義市),F-D0047-061(臺北市),F-D0047-065(高雄市),F-D0047-069(新北市),F-D0047-073(臺中市),F-D0047-077(臺南市),F-D0047-081(連江縣),F-D0047-085(金門縣)
list_city_7days = ["F-D0047-003", "F-D0047-007", "F-D0047-011", "F-D0047-015", "F-D0047-019", "F-D0047-023",
                   "F-D0047-027", "F-D0047-031", "F-D0047-035", "F-D0047-039", "F-D0047-043", "F-D0047-047",
                   "F-D0047-051", "F-D0047-055", "F-D0047-059", "F-D0047-063", "F-D0047-067", "F-D0047-071",
                   "F-D0047-075", "F-D0047-079", "F-D0047-083",
                   "F-D0047-087"]  # 代碼與縣市對照表 F-D0047-003(宜蘭縣),F-D0047-007(桃園市),F-D0047-011(新竹縣),F-D0047-015(苗栗縣),F-D0047-019(彰化縣),F-D0047-023(南投縣),F-D0047-027(雲林縣),F-D0047-031(嘉義縣),F-D0047-035(屏東縣),F-D0047-039(臺東縣),F-D0047-043(花蓮縣),F-D0047-047(澎湖縣),F-D0047-051(基隆市),F-D0047-055(新竹市),F-D0047-059(嘉義市),F-D0047-063(臺北市),F-D0047-067(高雄市),F-D0047-071(新北市),F-D0047-075(臺中市),F-D0047-079(臺南市),F-D0047-083(連江縣),F-D0047-087(金門縣)

# 一個縣市一個縣市去跑
for count_2 in range(0, len(list_city_72hr)):

    # 判斷是72小時（目前設定為"1"）還是一週（目前設定為"2"）
    if condition == "1":
        type_data = list_city_72hr[count_2]
    elif condition == "2":
        type_data = list_city_7days[count_2]

    url = set_url_weather(type_data)  # 要爬的網址
    data = web_crawler_weather(url)  # 爬出來的資料

    # 把同縣市中不同鄉鎮分割，並組合成一個list
    tmp_data_1 = str(data)
    tmp_data_1 = tmp_data_1.split("locationName")

    # 找到縣市名稱
    counties = tmp_data_1[1][tmp_data_1[1].find("'locationsName'") + 18:tmp_data_1[1].find("', 'dataid'")]

    # 只留下「天氣預報綜合描述」
    l_township = []  # 在這個縣市中有哪些鄉鎮市區
    l_township_lat = []  # 各鄉鎮市的緯度座標
    l_township_lon = []  # 各鄉鎮市的經度座標
    township = ""
    tmp = []
    tmp_data_2 = []
    for count_1 in range(2, len(tmp_data_1)):
        township = tmp_data_1[count_1][4:tmp_data_1[count_1].find(", 'geocode':") - 1]

        # 如果有相同名稱之鄉鎮市區則在後方加註縣市名稱，並將鄉鎮市區加入到list中
        if township in list_samename_township:
            township += "(" + str(counties) + ")"
        l_township.append(township)

        tmp = tmp_data_1[count_1].split("elementName")

        # 找出鄉鎮市區的經緯度
        lat = tmp_data_1[count_1][tmp_data_1[count_1].find("lat") + 7:tmp_data_1[count_1].find("lon") - 4]
        lon = tmp_data_1[count_1][tmp_data_1[count_1].find("lon") + 7:tmp_data_1[count_1].find("weatherElement") - 4]
        l_township_lat.append(lat)
        l_township_lon.append(lon)

        # 符合要求的data加入到新的一個暫時性清單
        tmp_data_2.append(tmp[1])

    # 將整段文字依照時間點分開，最後產出一個清單[不同的鄉鎮市][在不同時間]的[氣溫、降雨機率]
    tmp_time_day = ""
    tmp_temperature = ""
    tmp_rain = ""
    tmp_airpollution = ""
    l_single_data_set = []  # 單一時段之資料
    l_township_data_set = []  # 單一鄉鎮市區之資料
    l_all_data_set = []  # 全部之資料
    for count_1 in range(0, len(tmp_data_2)):
        tmp_data_2[count_1] = tmp_data_2[count_1].split("'startTime'")
        l_township_data_set = []
        for count_2 in range(1, len(tmp_data_2[count_1])):
            # 日期
            if count_2 != len(tmp_data_2[count_1]) - 1:
                tmp_time_day = tmp_data_2[count_1][count_2][3:13]

            # 氣溫
            tmp_temperature = tmp_data_2[count_1][count_2][
                              tmp_data_2[count_1][count_2].find("。溫度攝氏") + 5:tmp_data_2[count_1][count_2].find("度。")]

            # 降雨機率
            if condition == "2" and count_2 - 1 >= 7:
                tmp_rain = "無資料"
            else:
                tmp_rain = tmp_data_2[count_1][count_2][
                           tmp_data_2[count_1][count_2].find("降雨機率 ") + 5:tmp_data_2[count_1][count_2].find("。溫度攝氏")]
                if tmp_rain == "":  # 遇到沒有降雨機率時便顯示「無資料」
                    tmp_rain = "無資料"

            # 找到相應之空汙數據
            if tmp_time_day in d_airpollution_recordday:
                tmp_n = d_airpollution_recordday[tmp_time_day]
                if str(counties) in ["金門縣", "連江縣", "澎湖縣"] and tmp_n != 0:
                    tmp_airpollution = "無資料"
                else:
                    tmp_airpollution = d_counties_airpollution[str(counties)][tmp_n][0]
            else:
                tmp_airpollution = "無資料"

            l_single_data_set = [tmp_time_day, count_2 - 1, tmp_temperature, tmp_rain,
                                 tmp_airpollution]  # 日期*str*、流水碼*int*、氣溫*str*、降雨機率*str*、空氣污染狀況*str*
            l_township_data_set.append(l_single_data_set)
        l_all_data_set.append(l_township_data_set)

    # 將資料加入diction中
    for count_1 in range(0, len(l_township)):
        d_township_counties[l_township[count_1]] = str(counties)
        d_township_lat_lon[l_township[count_1]] = [l_township_lon[count_1], l_township_lat[count_1]]
        d_township_data[l_township[count_1]] = l_all_data_set[count_1]

# print("爬蟲程式運作結束")

# 檢查單一區域天氣資料
# print('中正區天氣', d_township_data.get("中正區(臺北市)"))
# print('和平區天氣：', d_township_data.get('和平區'))

'''
中正區(臺北市)天氣：
[[date, serial#, temperature, prob., AQI]
[['2021-01-05', 0, '14至16', '90%', '無資料'], 
['2021-01-06', 1, '14至17', '80%', '50'], 
['2021-01-06', 2, '13至15', '100%', '50'], 
['2021-01-07', 3, '10至13', '100%', '50'], 
['2021-01-07', 4, '7至10', '70%', '50'], 
['2021-01-08', 5, '7至9', "021-01-08 06:00:00', 'endTime': '2021-01-08 18:00:00', 'elementValue': [{'value': '陰有雨", '50'], 
['2021-01-08', 6, '7至8', "021-01-08 18:00:00', 'endTime': '2021-01-09 06:00:00', 'elementValue': [{'value': '陰有雨", '50'], 
['2021-01-09', 7, '7至12', '無資料', '無資料'], 
['2021-01-09', 8, '10至11', '無資料', '無資料'], 
['2021-01-10', 9, '10至16', '無資料', '無資料'], 
['2021-01-10', 10, '13至14', '無資料', '無資料'], 
['2021-01-11', 11, '12至14', '無資料', '無資料'], 
['2021-01-11', 12, '11至12', '無資料', '無資料'], 
['2021-01-12', 13, '11至14', '無資料', '無資料'], 
['2021-01-12', 14, '11至12', '無資料', '無資料']]

和平區天氣： 
[['2021-01-05', 0, '11至14', '0%', '無資料'], 
['2021-01-06', 1, '11至17', '0%', '50'], 
['2021-01-06', 2, '11至13', '20%', '50'], 
['2021-01-07', 3, '10至13', '20%', '50'], 
['2021-01-07', 4, '7至10', '20%', '50'], 
['2021-01-08', 5, '7至9', "021-01-08 06:00:00', 'endTime': '2021-01-08 18:00:00', 'elementValue': [{'value': '陰時多雲", '50'], 
['2021-01-08', 6, '6至7', "021-01-08 18:00:00', 'endTime': '2021-01-09 06:00:00', 'elementValue': [{'value': '晴時多雲", '50'], 
['2021-01-09', 7, '6至12', '無資料', '無資料'], 
['2021-01-09', 8, '9至10', '無資料', '無資料'], 
['2021-01-10', 9, '9至15', '無資料', '無資料'], 
['2021-01-10', 10, '9至12', '無資料', '無資料'], 
['2021-01-11', 11, '9至13', '無資料', '無資料'], 
['2021-01-11', 12, '8至10', '無資料', '無資料'], 
['2021-01-12', 13, '8至14', '無資料', '無資料'], 
['2021-01-12', 14, '9至11', '無資料', '無資料']]

'''

'''
隨機推薦 function
input: 所在鄉鎮(location)、距離上限(distance)、出遊日期(time_diff)
output: 一個符合條件的鄉鎮

'''


def suggestion(location, distance_limit, time_diff):
    # 推薦地點部分開始
    import random

    # 須讀入使用者的輸入條件，此區塊暫時都為測試值！
    distance_require = distance_limit  # 距離
    temperature_upper_require = 25  # 設高溫為, 25
    temperature_lower_require = 10  # 設低溫為, 10
    rain_probability_require = 30  # 最大降雨機率, 30
    air_quality_require = 100  # 空氣品質AQI, 100
    time_require = 2 * time_diff
    # 因為在 d_township_data 裡面，一天有兩筆天氣資料，所以用 index 以 2 為單位查找

    # 檢查透過區域名稱讀取資料
    # for district in district_list:
    # weather = d_township_data.get(district)
    # print(district + weather[0][3])

    # 計算距離部分開始
    import math
    current_place = location  # 現在的位置
    d_distance_dict = {}
    lat1 = d_township_lat_lon[current_place][0]
    lng1 = d_township_lat_lon[current_place][1]
    lat1 = float(lat1)
    lng1 = float(lng1)

    # def Distance1(Lat_A,Lng_A,Lat_B,Lng_B):
    # ra = 6378.140 #赤道半徑
    # rb = 6356.755 #極半徑 （km）
    # flatten = (ra-rb)/ra  #地球偏率
    # rad_lat_A = math.radians(Lat_A)
    # rad_lng_A = math.radians(Lng_A)
    # rad_lat_B = math.radians(Lat_B)
    # rad_lng_B = math.radians(Lng_B)
    # pA = math.atan(rb/ra*math.tan(rad_lat_A))
    # pB = math.atan(rb/ra*math.tan(rad_lat_B))
    # xx = math.acos(math.sin(pA)*math.sin(pB)+math.cos(pA)*math.cos(pB)*math.cos(rad_lng_A-rad_lng_B))
    # c1 = (math.sin(xx)-xx)*(math.sin(pA)+math.sin(pB))**2/math.cos(xx/2)**2
    # c2 = (math.sin(xx)+xx)*(math.sin(pA)-math.sin(pB))**2/math.sin(xx/2)**2
    # dr = flatten/8*(c1-c2)
    # distance = ra*(xx+dr)
    # return distance

    def Distance2(lat1, lng1, lat2, lng2):  # 第二種計算方法
        radlat1 = math.radians(lat1)
        radlat2 = math.radians(lat2)
        a = radlat1 - radlat2
        b = math.radians(lng1) - math.radians(lng2)
        s = 2 * math.asin(
            math.sqrt(pow(math.sin(a / 2), 2) + math.cos(radlat1) * math.cos(radlat2) * pow(math.sin(b / 2), 2)))
        earth_radius = 6378.137
        s = s * earth_radius
        if s < 0:
            return -s
        else:
            return s

    def Distance_mean(lat1, lng1, lat2, lng2):  # 算平均
        distance = Distance2(lat1, lng1, lat2, lng2)
        return distance

    for count in range(len(district_list)):
        lat2 = d_township_lat_lon[district_list[count]][0]
        lng2 = d_township_lat_lon[district_list[count]][1]
        lat2 = float(lat2)
        lng2 = float(lng2)
        d_distance_dict[district_list[count]] = Distance_mean(lat1, lng1, lat2, lng2)

    # 創建新清單，為區域列表擴充資料
    district_list_with_data = [[1, 2]]

    for i in range(len(district_list)):
        weather = d_township_data.get(district_list[i])  # 獲取此輪區域天氣資料

        # 擴充距離資料
        distance = d_distance_dict.get(district_list[i])  # 須讀入實際距離，測試時先設為100
        district_list_with_data[i][0] = district_list[i]
        district_list_with_data[i][1] = distance
        if i != (len(district_list) - 1):
            district_list_with_data.append([1, 2])

        # 擴充溫度資料
        if condition == "1":
            temperature = weather[time_require][2]
            # 從 d_township_data 裡面取出選定日期的「溫度」資料
            # 在 d_township_data 裡，index0:date, index1:流水編號, index2:溫度str, index3: 降雨機率, index4: AQI
            if temperature == "無資料":
                temperature = 1000
            else:
                temperature = int(temperature)  # 將溫度轉為int
            district_list_with_data[i].append(temperature)
            district_list_with_data[i].append(temperature)
        elif condition == "2":
            temperature = weather[time_require][2]
            if temperature == "無資料":
                temperature_up = 1000
                temperature_low = 1000
            else:
                temperature_range = temperature.split("至")
                temperature_up = temperature_range[1]
                temperature_up = int(temperature_up)
                temperature_low = temperature_range[0]
                temperature_low = int(temperature_low)
            district_list_with_data[i].append(temperature_up)
            district_list_with_data[i].append(temperature_low)

        # 擴充降雨機率
        rain_probability = weather[time_require][3]
        if rain_probability == "無資料":
            if condition == "1":
                rain_probability = 1000
            elif condition == "2":
                rain_probability = 0
        else:
            rain_probability = rain_probability.rstrip('%')  # 將降雨資料轉為int的處理
            rain_probability = int(rain_probability)
        district_list_with_data[i].append(rain_probability)

        # 擴充空氣品質
        air_quality = weather[time_require][4]
        if air_quality == "無資料":
            air_quality = 0
        else:
            air_quality = int(air_quality)  # 將空氣品質轉為int
        district_list_with_data[i].append(air_quality)

    # 不確定還有什麼條件
    # 還有其他條件需擴充到清單的話
    # 程式碼加在此註解區塊之上

    # print('district_list_with_data', district_list_with_data[:5])  # 檢查擴充結果

    # [['中正區(臺北市)', 33.665623911131675, 16, 15, 0, 0],...]
    # [['town', distance, temp_upper, temp_lower, rain(default=0), aqi(default=0)], ...]

    # 為實行測試，把清單內第0項的資料作修改，測試值為所有區域都相同
    # district_list_with_data[0][1] = 50
    # district_list_with_data[0][2] = 25
    # district_list_with_data[0][3] = 30
    # district_list_with_data[0][4] = 40

    def ramdom_recommend(distance_require, temperature_upper_require, temperature_lower_require,
                         rain_probability_require, air_quality_require):
        """
        此function根據條件與資料，實行篩選，並輸出推薦的區域
        parameter目前依序為距離、高溫、低溫、降雨機率、空氣品質
        """
        recommend_list = []
        # 迴圈判定所有區域
        for i in range(len(district_list_with_data)):
            if district_list_with_data[i][1] > distance_require:  # 判斷距離
                continue
            elif district_list_with_data[i][2] > temperature_upper_require:  # 判斷高溫
                continue
            elif district_list_with_data[i][3] < temperature_lower_require:  # 判斷低溫
                continue
            elif district_list_with_data[i][4] > rain_probability_require:  # 判斷降雨機率
                continue
            elif district_list_with_data[i][5] >= air_quality_require:  # 判斷空氣品質
                continue
            # 若所有條件都符合，把區域名稱加入到推薦清單中
            else:
                recommend_list.append(district_list_with_data[i][0])

        #  用亂數從推薦清單中隨機挑出一個
        if len(recommend_list) == 0:
            recommend_result = 0
        else:
            number = random.randint(0, len(recommend_list) - 1)
            recommend_result = recommend_list[number]

        # return推薦的區域名稱，若全部不符合(推薦清單為空)就返回0
        return recommend_result

    # 套用function實行推薦
    recommend_district = ramdom_recommend(distance_require, temperature_upper_require,
                                          temperature_lower_require, rain_probability_require,
                                          air_quality_require)

    # 輸出結果recommend_district
    if recommend_district == 0:
        # print("無符合條件的區域！")
        recommend_district = "無符合條件的區域！"
        output = recommend_district
    else:
        # print("推薦地點: " + recommend_district)
        output = "推薦地點: " + str(recommend_district)

    # d_output(output)

    return output


'''

以下是鄉鎮天氣分數計算的部分
算出各鄉鎮的每天的天氣分數，並做成 7 個 dataframe

'''

# 以下為資料型態轉換 -- 把鄉鎮以代號呈現，計算分數後，存成 dataframe，以便跟地圖資訊 merge 起來

# 把鄉鎮代碼的檔案讀進來，並轉成 list 型態
import pandas as pd
import csv

with open('townid.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)

# 把讀進來的鄉鎮 list，轉為以鄉鎮名稱為 key 的 dictionary
TownID = dict()
for atown in data:
    if atown[3] in list_samename_township:
        key = atown[3] + '(' + atown[2] + ')'
        TownID[key] = atown[0]
    else:
        TownID[atown[3]] = atown[0]


# print('TownID', TownID)

def get_score(day):
    # 各鄉鎮的天氣計算分數
    score_town = dict()
    for key in d_township_data:

        score = ['sunny']

        temp_str = d_township_data[key][day * 2][2]

        rain_str = d_township_data[key][day * 2][3][:-1]
        rain_prob = int(rain_str) if (rain_str[0] in str(range(10)) and len(rain_str) <= 3) else 1000
        rain_str2 = str(rain_prob) + '%' if (rain_prob != 1000) else '無資料'

        aqi_str = d_township_data[key][day * 2][4]
        aqi = int(aqi_str) if (aqi_str != '無資料') else 1000

        if 1000 > rain_prob >= 40:
            score[0] = 'rain'
        elif 1000 > aqi >= 100:
            score[0] = 'bad air quality'
        elif rain_prob == 1000 and aqi == 1000:
            score[0] = 'no data'

        weather_detail = '氣溫：' + temp_str + '度 / 降雨機率：' + rain_str2 + ' / 空氣品質：' + aqi_str
        score.append(weather_detail)

        score_town[key] = score
    # print('score_town: ', score_town)

    # 把各鄉鎮的分數 dictionary 轉為鄉鎮代碼表示

    score_in_townid = dict()
    for town_name in score_town:
        score_in_townid[TownID[town_name]] = score_town[town_name]

    # print('score_in_townid: ', score_in_townid)

    # 把 score_in_townid 從 dictionary 轉為 pandas dataframe
    df_score = pd.DataFrame.from_dict(score_in_townid, orient='index', columns=['score', 'detail'])
    df_score = df_score.reset_index()
    # print('df_score: ', df_score)

    '''
    # Original  df_score without weather details
        index    score
    0     G06  No data
    1     G09     rain
    2     G02  No data
    3     G03  No data
    4     G10     rain

    # New df_score with weather details
        index    score                        detail
    0     G06  No data   氣溫：13至15 / 降雨機率：無資料 / 空氣品質：50
    1     G09     rain  氣溫：14至16 / 降雨機率：100% / 空氣品質：50
    2     G02  No data   氣溫：13至15 / 降雨機率：無資料 / 空氣品質：50
    3     G03  No data   氣溫：13至15 / 降雨機率：無資料 / 空氣品質：50
    4     G10     rain  氣溫：13至14 / 降雨機率：100% / 空氣品質：50
    ..    ...      ...                           ...
    363   W05    sunny   氣溫：12至13 / 降雨機率：10% / 空氣品質：70
    364   W04    sunny   氣溫：11至13 / 降雨機率：10% / 空氣品質：70
    365   W01    sunny   氣溫：11至13 / 降雨機率：10% / 空氣品質：70
    366   W02    sunny   氣溫：11至12 / 降雨機率：10% / 空氣品質：70
    367   W03    sunny   氣溫：11至13 / 降雨機率：10% / 空氣品質：70


    '''

    return df_score


df_score0 = get_score(0)
df_score1 = get_score(1)
df_score2 = get_score(2)
df_score3 = get_score(3)
df_score4 = get_score(4)
df_score5 = get_score(5)
df_score6 = get_score(6)

'''

以下為畫地圖

'''

# 以下為畫地圖
import pandas as pd
import plotly.express as px
import geopandas as gpd

# 讀行政區地理邊界資料
town_shp = gpd.read_file('mapdata202010230200/TOWN_MOI_1091016.shp', encoding='utf-8')
# town_shp = gpd.read_file('/Users/linyuxuan/Desktop/mapdata202010230200/TOWN_MOI_1091016.shp', encoding='utf-8')
town_shp['TOWNID'] = town_shp['TOWNID'].astype('str')


# merged dataframe
def merged_df(aday):
    df = pd.merge(town_shp[['TOWNID', 'COUNTYNAME', 'TOWNNAME', 'COUNTYID', 'geometry']],
                  aday[['index', 'score', 'detail']], left_on='TOWNID', right_on='index', how='left')
    df = df.dropna().reset_index()

    return df


df0 = merged_df(df_score0)
df1 = merged_df(df_score1)
df2 = merged_df(df_score2)
df3 = merged_df(df_score3)
df4 = merged_df(df_score4)
df5 = merged_df(df_score5)
df6 = merged_df(df_score6)

# print(df.head())

town_shp.index = town_shp.index.astype('str')

# convert from gpd to json
town_epsg = town_shp.set_crs(epsg=4326)  # convert the coordinate reference system to lat/long
town_json = town_epsg.__geo_interface__  # convert to geoJSON

# 以下為 Dash

import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
# import dash_leaflet as dl
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO, external_stylesheets])
# Bootstrap 網頁風格選擇：https://bootswatch.com/


# 所在地點選單
all_options = {
    '臺北市': ['中正區(臺北市)', '大同區', '中山區(臺北市)', '萬華區', '信義區(臺北市)',
            '松山區', '大安區(臺北市)', '南港區', '北投區', '內湖區', '士林區', '文山區'],
    '新北市': ['板橋區', '新莊區', '泰山區', '林口區', '淡水區', '金山區', '八里區', '萬里區', '石門區', '三芝區', '瑞芳區',
            '汐止區', '平溪區', '貢寮區', '雙溪區', '深坑區', '石碇區', '新店區', '坪林區',
            '烏來區', '中和區', '永和區', '土城區', '三峽區', '樹林區', '鶯歌區', '三重區',
            '蘆洲區', '五股區'],
    '基隆市': ['仁愛區', '中正區(基隆市)', '信義區(基隆市)', '中山區(基隆市)', '安樂區', '暖暖區', '七堵區'],
    '桃園市': ['桃園區', '中壢區', '平鎮區', '八德區', '楊梅區', '蘆竹區', '龜山區',
            '龍潭區', '大溪區', '大園區', '觀音區', '新屋區', '復興區'],
    '新竹縣': ['竹北市', '竹東鎮', '新埔鎮', '關西鎮', '峨眉鄉', '寶山鄉', '北埔鄉', '橫山鄉', '芎林鄉', '湖口鄉',
            '新豐鄉', '尖石鄉', '五峰鄉'],
    '新竹市': ['東區(新竹市)', '北區(新竹市)', '香山區'],
    '苗栗縣': ['苗栗市', '通霄鎮', '苑裡鎮', '竹南鎮', '頭份市', '後龍鎮', '卓蘭鎮', '西湖鄉', '頭屋鄉', '公館鄉',
            '銅鑼鄉', '三義鄉', '造橋鄉', '三灣鄉', '南庄鄉', '大湖鄉', '獅潭鄉', '泰安鄉'],
    '臺中市': ['中區', '東區(臺中市)', '南區(臺中市)', '西區(臺中市)', '北區(臺中市)',
            '北屯區', '西屯區', '南屯區', '太平區', '大里區', '霧峰區', '烏日區', '豐原區', '后里區', '東勢區', '石岡區', '新社區',
            '和平區', '神岡區', '潭子區', '大雅區', '大肚區', '龍井區', '沙鹿區', '梧棲區',
            '清水區', '大甲區', '外埔區', '大安區(臺中市)'],
    '南投縣': ['南投市', '埔里鎮', '草屯鎮', '竹山鎮', '集集鎮', '名間鄉', '鹿谷鄉', '中寮鄉', '魚池鄉', '國姓鄉', '水里鄉', '信義鄉', '仁愛鄉'],
    '彰化縣': ['彰化市', '員林市', '和美鎮', '鹿港鎮', '溪湖鎮', '二林鎮', '田中鎮', '北斗鎮', '花壇鄉', '芬園鄉', '大村鄉', '永靖鄉', '伸港鄉', '線西鄉', '福興鄉',
            '秀水鄉', '埔心鄉', '埔鹽鄉', '大城鄉', '芳苑鄉', '竹塘鄉', '社頭鄉', '二水鄉', '田尾鄉', '埤頭鄉', '溪州鄉'],
    '雲林縣': ['斗六市', '斗南鎮', '虎尾鎮', '西螺鎮', '土庫鎮',
            '北港鎮', '莿桐鄉', '林內鄉', '古坑鄉', '大埤鄉', '崙背鄉', '二崙鄉', '麥寮鄉',
            '臺西鄉', '東勢鄉', '褒忠鄉', '四湖鄉', '口湖鄉', '水林鄉', '元長鄉'],
    '嘉義縣': ['太保市', '朴子市', '布袋鎮', '大林鎮', '民雄鄉', '溪口鄉', '新港鄉', '六腳鄉', '東石鄉',
            '義竹鄉', '鹿草鄉', '水上鄉', '中埔鄉', '竹崎鄉', '梅山鄉', '番路鄉', '大埔鄉', '阿里山鄉'],
    '嘉義市': ['東區(嘉義市)', '西區(嘉義市)'],
    '臺南市': ['中西區', '東區(臺南市)', '南區(臺南市)', '北區(臺南市)', '安平區', '安南區',
            '永康區', '歸仁區', '新化區', '左鎮區', '玉井區', '楠西區', '南化區', '仁德區',
            '關廟區', '龍崎區', '官田區', '麻豆區', '佳里區', '西港區', '七股區', '將軍區',
            '學甲區', '北門區', '新營區', '後壁區', '白河區', '東山區', '六甲區', '下營區',
            '柳營區', '鹽水區', '善化區', '大內區', '山上區', '新市區', '安定區'],
    '高雄市': ['楠梓區', '左營區', '鼓山區', '三民區', '鹽埕區', '前金區', '新興區', '苓雅區', '前鎮區',
            '小港區', '旗津區', '鳳山區', '大寮區', '鳥松區', '林園區', '仁武區', '大樹區',
            '大社區', '岡山區', '路竹區', '橋頭區', '梓官區', '彌陀區', '永安區', '燕巢區',
            '田寮區', '阿蓮區', '茄萣區', '湖內區', '旗山區', '美濃區', '內門區', '杉林區',
            '甲仙區', '六龜區', '茂林區', '桃源區', '那瑪夏區'],
    '屏東縣': ['屏東市', '潮州鎮', '東港鎮',
            '恆春鎮', '萬丹鄉', '長治鄉', '麟洛鄉', '九如鄉', '里港鄉', '鹽埔鄉', '高樹鄉',
            '萬巒鄉', '內埔鄉', '竹田鄉', '新埤鄉', '枋寮鄉', '新園鄉', '崁頂鄉', '林邊鄉',
            '南州鄉', '佳冬鄉', '琉球鄉', '車城鄉', '滿州鄉', '枋山鄉', '霧臺鄉', '瑪家鄉',
            '泰武鄉', '來義鄉', '春日鄉', '獅子鄉', '牡丹鄉', '三地門鄉'],
    '宜蘭縣': ['宜蘭市', '羅東鎮', '蘇澳鎮', '頭城鎮', '礁溪鄉', '壯圍鄉', '員山鄉', '冬山鄉', '五結鄉', '三星鄉', '大同鄉', '南澳鄉'],
    '花蓮縣': ['花蓮市', '鳳林鎮', '玉里鎮', '新城鄉', '吉安鄉', '壽豐鄉',
            '秀林鄉', '光復鄉', '豐濱鄉', '瑞穗鄉', '萬榮鄉', '富里鄉', '卓溪鄉'],
    '臺東縣': ['臺東市', '成功鎮', '關山鎮', '長濱鄉', '海端鄉', '池上鄉', '東河鄉', '鹿野鄉', '延平鄉',
            '卑南鄉', '金峰鄉', '大武鄉', '達仁鄉', '綠島鄉', '蘭嶼鄉', '太麻里鄉'],
    '澎湖縣': ['馬公市', '湖西鄉', '白沙鄉', '西嶼鄉', '望安鄉', '七美鄉'],
    '金門縣': ['金城鎮', '金湖鎮', '金沙鎮', '金寧鄉', '烈嶼鄉', '烏坵鄉'],
    '連江縣': ['南竿鄉', '北竿鄉', '莒光鄉', '東引鄉']
}


# put all the input items into a card, and the map into another card。
# 為了方便排版美觀，把地圖以外的東西都裝進一個 card 裡放在畫面左邊，地圖自己一個 card 放在畫面右邊
'''
Bootstrap: 網頁排版
tutorial： https://www.youtube.com/watch?v=vqVwpL4bGKY

Bootstrap.Card: 把網頁元件打包成一個個美觀、彈性的 card
tutorial: https://www.youtube.com/watch?v=aEz1-72PKwc&t=34s

'''

card_inputs = dbc.Card(
    [
        dbc.CardBody([

            # select the date
            html.Header('請選擇您的出遊日期'),

            dcc.Dropdown(id="slct_day",
                 options=[
                     {"label": "今天", "value": 0},
                     {"label": "明天", "value": 1},
                     {"label": "後天", "value": 2},
                     {"label": "三天後", "value": 3},
                     {"label": "四天後", "value": 4},
                     {"label": "五天後", "value": 5},
                     {"label": "一週後", "value": 6}, ],
                 multi=False,
                 value=0,
                 style={'width': "40%"}
                 ),
            html.Div(id='day_slctd_output_container', children=[], style={'text-align': 'right'}),
            html.Br(),

            # Select the current location
            html.Header('請選擇您的所在地'),

            dcc.Dropdown(
                id='counties-slct',
                options=[{'label': k, 'value': k} for k in all_options.keys()],
                value='臺北市',
                multi=False,
                style = {'width': "70%"}
            ),

            # html.Hr(),

            dcc.Dropdown(id='towns-slct', style = {'width': "70%"}),

            # html.Hr(),

            html.Div(id='display-current-location', style={'text-align': 'right'}),
            # html.Br(),
            html.Hr(),

            # Select the max travel distance
            html.Header('請選擇最大旅遊距離'),

            dcc.Slider(
                id='dist-slider',
                min=0,
                max=400,
                step=10,
                marks={
                    10: '10', 30: '30', 50: '50', 70: '70', 100: '100',
                    150: '150', 200: '200', 300: '300', 400: '400'},
                value=100,
            ),

            html.Div(id='slider-output-container', style={'text-align': 'right'}),

            html.Hr(),

            #  Display the recommended town
            html.Div(id='display-recommended-town')
        ])
    ],
    color='dark',   # https://bootswatch.com/default/ for more card colors
    inverse=False,   # change color of text (black or white)
    outline=False   # True = remove the block colors from the background and header
)


card_map = dbc.Card(
    [
        dbc.CardBody([
            dcc.Graph(id='my_weather_map', figure={}),
            html.Header('當日各地天氣', style={'text-align': 'center'}),
        ])

    ],
    color='dark',
    inverse=False,
    outline=False
)

# App layout: arrange the layout of the app, and put the cards above inside the layout section
app.layout = html.Div([

    # Row 0: empty row
    dbc.Row(dbc.Col(html.H1(' '), width=12)),

    # Row 1: the title
    dbc.Row(dbc.Col(html.H1("台灣氣象旅遊地圖", style={'text-align': 'center'}),
                    width=12
                    )
            ),

    # Row 2: empty row
    dbc.Row(dbc.Col(html.H1(' '), width=12)),

    # Row 3: Input card to the left & map card to the right
    dbc.Row([dbc.Col(card_inputs, width=4),
             dbc.Col(card_map, width=6)], justify='around') # justify="start", "center", "end", "between", "around"

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components

# 地圖區
@app.callback(
    [Output(component_id='day_slctd_output_container', component_property='children'),
     Output(component_id='my_weather_map', component_property='figure')],
    [Input(component_id='slct_day', component_property='value'),
     Input(component_id='towns-slct', component_property='value'),
     Input(component_id='display-recommended-town', component_property='children')]
)
def update_graph(day_slctd, towns_slct, town_recommended):
    container = "您選擇的出遊日期為: {}天後".format(day_slctd)

    # 依據輸入的旅遊時間，選定該天天氣資料的 dataframe
    df_dict = {0: df0, 1: df1, 2: df2, 3: df3, 4: df4, 5: df5, 6: df6}
    dff = df_dict[day_slctd].copy()

    # 把所在地的 score 改成 "current locaiton，在地圖中顯示成不同顏色
    dff.loc[dff['TOWNNAME'] == towns_slct, ['score']] = 'current location'
    # rec_str = town_recommended[6:]
    # df_loc = pd.DataFrame(columns=dff.columns)
    # loc_new = dff.loc[dff['TOWNNAME'] == towns_slct]
    # loc_rec = dff.loc[dff['TOWNNAME'] == rec_str]
    # df_loc = df_loc.append(loc_new, ignore_index=True)
    # df_loc = df_loc.append(loc_rec, ignore_index=True)
    # df_loc.loc[df_loc['TOWNNAME'] == towns_slct, ['score']] = 'current location'
    # df_loc.loc[df_loc['TOWNNAME'] == rec_str, ['score']] = 'recommended location'

    # 把推薦地的 score 改成 "recommended location，在地圖中顯示成不同顏色
    rec_str = town_recommended[6:]
    print('rec_str: ', rec_str)
    dff.loc[dff['TOWNNAME'] == rec_str, ['score']] = 'recommended location'
    # print('used dff: ', dff)

    # Plotly Express
    fig = px.choropleth_mapbox(dff, geojson=town_json, locations='level_0', color='score',
                               color_discrete_map={'rain': '#00BFFF', 'bad air quality': 'grey', 'sunny': '#FFD700',
                                                   'no data': 'white', 'current location': '#C71585',
                                                   'recommended location': 'red'},
                               hover_name='COUNTYNAME', hover_data=['TOWNNAME', 'score', 'detail'],
                               labels={'TOWNNAME': '鄉鎮', 'score': '概況', 'detail': '詳細資料'},
                               center={"lat": 23.5000, "lon": 120.9797}, zoom=6, height=700,
                               mapbox_style="carto-positron"
                               )
    # 色票：https: // www.w3schools.com / cssref / css_colors.asp

    return container, fig


# 所在地 dropdown 區
@app.callback(
    Output('towns-slct', 'options'),
    Input('counties-slct', 'value'))
def set_towns_options(selected_county):
    return [{'label': i, 'value': i} for i in all_options[selected_county]]


@app.callback(
    Output('towns-slct', 'value'),
    Input('towns-slct', 'options'))
def set_towns_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-current-location', 'children'),
    Input('counties-slct', 'value'),
    Input('towns-slct', 'value'))
def set_display_children(selected_county, selected_town):
    return u'所在位置為 {}{}'.format(
        selected_county, selected_town,
    )


# 旅遊距離 slider 區
@app.callback(
    Output('slider-output-container', 'children'),
    [Input('dist-slider', 'value')])
def update_output(value):
    return '您選擇的旅遊距離為 "{}"公里'.format(value)


# 隨機推薦區
@app.callback(
    Output('display-recommended-town', 'children'),
    Input('towns-slct', 'value'),
    Input('dist-slider', 'value'),
    Input('slct_day', 'value'))
def set_display_children(location, distance_limit, time_diff):
    return suggestion(location, distance_limit, time_diff)

    # return u'所在位置為 {}{}'.format(selected_county, selected_town)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    # app.run_server(debug=True, port=1337)
    app.run_server(debug=True,port=8910)
    # app.run_server(debug=True)
