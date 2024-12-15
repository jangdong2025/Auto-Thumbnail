from PIL import Image, ImageFont, ImageDraw
import datetime as dt

target_img = Image.open("./src/그림3.jpg")

draw = ImageDraw.Draw(target_img,"RGBA")
box_coords = [(46, 56), (290, 150)]  # 상자의 좌상단과 우하단 좌표
draw.rectangle(box_coords, fill=(255, 255, 255,128))  # 흰색 상자, 투명도 조정


font1 = ImageFont.truetype("./src/hy헤드라인m.ttf", 20)
font2 = ImageFont.truetype("./src/hy헤드라인m.ttf", 28)

title_text = "대한예수교장로회"
out_img = ImageDraw.Draw(target_img)
out_img.text(xy=(50,60), text=title_text, fill=(0, 0, 0), font=font1)

x = dt.datetime.now()
format = '%Y. %m. %d'
date = dt.datetime.strftime(x,format)
str1 = str(date)

text1 = "장동교회 "

if x.weekday()==2:
    text1 += "수요"
elif x.weekday()==6:
    if x.hour<12:
        text1 += "오전"
    else:
        text1 += "오후"

text1 += "예배"
text2 = '('+str1+')'
out_img.text(xy=(50,86), text=text1, fill=(0, 0, 0), font=font2)
out_img.text(xy=(50,120), text=text2, fill=(0, 0, 0), font=font2)


target_img.save("썸네일.png")