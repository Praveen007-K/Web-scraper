from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'


#opening up connection and grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

#converting to csv
filename = "products.csv"
f = open(filename,"w")

headers = "Brand, Product_name, Shipping_rate\n"

f.write(headers)


for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container=container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping_rate = shipping_container[0].text
    
    print("Brand: " + brand)
    print("Product_name: " + product_name)
    print("Shipping_rate: " + shipping_rate)
    
    f.write(brand + "," + product_name  + "," + shipping_rate + "\n")
    
f.close()