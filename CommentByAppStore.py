import requests
import openpyxl

url="https://itunes.apple.com/rss/customerreviews/page=1/id=414478124/sortby=mostrecent/json?l=en&&cc=cn"
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
comment=requests.get(url,headers=headers)
data=comment.json()

wb=openpyxl.load_workbook('example.xlsx')
sheet=wb['Sheet']
sheet['A1']='昵称'
sheet['B1']='评分'
sheet['C1']='标题'
sheet['D1']='评论'

for i in range(0,50):
    name=data['feed']['entry'][i]['author']['name']['label']
    rating=data['feed']['entry'][i]['im:rating']['label']
    title=data['feed']['entry'][i]['title']['label']
    content=data['feed']['entry'][i]['content']['label']
    sheet.append([name, rating, title,content])


wb.save('example.xlsx')
