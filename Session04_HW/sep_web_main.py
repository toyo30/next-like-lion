import requests
from bs4 import BeautifulSoup
from sep_web_fuc import extract_info
import csv

file = open('./Session04_HW/web-toon.csv', mode="w", newline='')
writer = csv.writer(file)
final_result = []

# 우리가 정보를 얻고 싶어하는 URL
WEB_URL = f"https://comic.naver.com/webtoon/weekdayList?week=sun"
#f는 문자열 포메팅을 의미함. 




# get 요청을 통해 해당 페이지 정보를 저장
web_html = requests.get(WEB_URL)


# # 요청을 보냄 


# # bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
web_soup = BeautifulSoup(web_html.text, "html.parser")



web_list_box = web_soup.find("ul", {"class":"img_list"})
web_list = web_list_box.find_all("li")





# # #list를 더하는 것은 리스트 안에 요소가 더해짐 
final_result += extract_info(web_list)




print(final_result)






# mode="w" csv 파일에다가 정보를 입력하고 쓰는 모드
# newline = '' 뛰어쓰기 없이 입력


# 쓰기 모드

writer.writerow(["title", "name", "rating"])

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['name'])
    row.append(result['rating'])
    writer.writerow(row)

    
# print(final_result)


