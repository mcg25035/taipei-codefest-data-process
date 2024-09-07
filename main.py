import requests
import json

# Split the data into rows and then into columns

i = """黑客松大賽開始,2024台北秋季程式設計節，城市通微服務大黑客松,121.53492,25.0186,#activity #global,
台大社博,社團博覽會，有許多不同的社團可以了解、互動、參加，認識不同的同學,121.53774,25.01735,#activity #global,
神奇的隊名,把所有隊員的名字都塞在十個字內,121.53522,25.02165,#daily #global,
前往異世界的門,前往科技世界,121.51271,25.04964,#daily #global,
FF42,沒見過的cos，令人眼前一亮,121.52159,25.06967,#activity #global,
樹木倒塌,北檢旁的樹倒塌，大家要小心,121.5111981,25.0367945,#road-conditions #global,
北門,建於1884年，是清朝時期的城門之一。以紅磚砌成，展現古典建築風格。曾經是防禦和交通管理的要地,121.514248,25.04708181,#view #global,
台北市立動物園,非洲動物區非洲獅展示場9月9日停展,121.58417,24.995,#view #global,
路上天坑,如果有在附近記得小心避開,121.5156662,25.05388272,#road-conditions #global,
信義商圈,信義商圈融合了現代與時尚，吸引了大量購物和娛樂愛好者。區內的街道整潔、環境優美，還有眾多高級餐廳和娛樂設施,121.5663983,25.0331422,#view #global,
廟會活動,有獅、陣頭、遶境、歌仔戲等表演，以及各種小吃攤位，充滿熱鬧的氛圍。,121.515596,25.07337802,#activity #global,
大拇鍋,要讓台灣人放棄諧音梗已經Taiwan了,121.553319,25.03928002,#daily #global,
北藝,不愧是在士林夜市旁的表演藝術中心，生動演繹了貢丸、米血、百頁,121.52497,25.08516,#daily #global,
總統府,升旗時，國旗伴隨著國歌冉冉升起，象徵國家的尊嚴和人民的團結，共同感受濃厚的愛國情懷和慶祝氣氛。,121.5130095,25.04093624,#activity #global,
稀有寶可夢,沒人發現的新位置,121.519873,25.036444,#daily #global,
阿嬤的摩托車,車牌很不對勁,121.5301464,25.04068242,#daily #global,
完了,不知要如何開口,121.549524,25.04890898,#daily #global,
買一送一,咚咚店家現在正在促銷,25.04724999,25.03928002,#car-accident #global,
原來是同個人?,馬斯克變馬雲,121.574451,25.07458422,#daily #global,
負責畫線的人在搞笑?,救災優,121.519873,25.036444,#daily #global,
不明物品,要去打疫苗嗎?,121.5663983,25.0331422,#daily #global,
加油,月底沒錢，只能加1元的油,121.519873,25.036444,#daily #global,
真。鏡池,要透過水面才能看到正確的字,121.545754,25.09444799,#daily #global
球?,河裡竟然有球?,121.520692,25.07610201,#good #global
三角錐陣列,應該不會有人去踩了吧?,25.04724999,25.03928002,#daily #global
五折,西西店家特價中,121.540406,25.06606699,#good #global
變異?,好多條尾巴,121.542481,25.04711992,#daily #global
童年崩壞系列,這樣是否對小孩有影響?,121.519873,25.036444,#daily #global
每天必買,如果沒有你，我就活不下去了,121.530614,25.03060001,#good #global
路名,這是想不到路名了嗎?,121.519873,25.036444,#daily #global
走丟的貓咪,請家屬接回,121.577574,25.04724999,#daily #global"""

rows = i.strip().split('\n')
headers = ['Title', 'Description', 'Lng', 'Lat', 'Category', "Image"]

# Convert rows into a list of dictionaries
formatted_data = [dict(zip(headers, row.split(','))) for row in rows]
count = 1
import base64

for i in formatted_data:
    # if count == 15 : 
    #     break
    count+=1

    with open(f"./media/{count}.txt", "rb") as image_text_file:
        encoded_string = image_text_file.read().decode('utf-8')
        i['Image'] = encoded_string 

        url = "https://taipei.codingbear.mcloudtw.com/api/warp_event"

        payload = {
            "lng": i['Lng'],
            "lat": i['Lat'],
            "title": i['Title'],
            "category": i['Category'],
            "base64image": i['Image']
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print("Event created successfully")
        else:
            print("Failed to create event")
