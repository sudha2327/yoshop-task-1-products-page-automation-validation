import requests
from bs4 import BeautifulSoup
import csv


import pandas as pd
urll=input("enter the URL:")
urll=urll+"/products"
HEADERS = ({'User-Agent':
                'Chrome/44.0.2403.157 Safari/537.36',
                                'Accept-Language': 'en-US, en;q=0.5'})
products=[]              #List to store the name of the product
real_prices=[] 
modified_price=[]               #List to store price of the product
ratings=[]  
url=[]  
img_url=[]
image_status=[]
for i in range(1,13):
    url1=urll+"?page={}".format(i)
    print("scrapping url page:",url1)
    

    # print(url1)
    webpage = requests.get(url1, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    for data in soup.find_all('div',attrs={"class":'col-sm-3 col-xs-6'}):
        im=data.find('img')
        # print(im)
        if "noimage" in im.get('src'):
            #print("missing value at",im.get('src'))
            image_status.append("missing images")
            img_url.append(im.get('src'))
            names=data.find('span',class_='product-title')
            rat=data.find('span',attrs={'class':'yotpo-icon'})
            r=soup.find('div',class_='product-price')
            li=soup.find('a',class_="product-link")
            real_prices.append(r.find_next('span').text)
            modified_price.append(r.find('span').find_next('span').find_next('span').text)
            url.append(li.get('href'))
            products.append(names.string)
            ratings.append(rat)
            

        else:
            # print("no missing")
            continue


  
        # if "noimage" in h:
        #     print("missing values")
        # else:
        #     print(" np missing is therere")
df=pd.DataFrame({'Product_name':products,'Product_URL':url,'Real_price':real_prices,'Modified_price':modified_price,'image_URL' : img_url



,'Image Status':image_status})
df.to_excel('outputfinalone.xlsx',index=False,encoding='utf-8')

print("file created....")
