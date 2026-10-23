from datetime import datetime
import time
import csv
from csv import DictReader, DictWriter
from selenium import webdriver
PATH = "chromedriver.exe"  # Supply a compatible local driver; binary is not included.

#open chrome incognito window
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--incognito")
#open chrom in incognito window
driver = webdriver.Chrome(PATH, options=chrome_option)
#url1=("https://www.cse.lk/")
url2=("https://www.investing.com/indices/cse-all-share")
ACL=("https://www.investing.com/equities/acl-cables-ratios")
AHUN=("https://www.investing.com/equities/aitken-spence-hotel-holdings-ratios")
CHL=("https://www.investing.com/equities/ceylon-hospitals-ratios")
COCO=("https://www.investing.com/equities/renuka-shaw-wallace-ratios")
COMB=("https://www.investing.com/equities/commercial-bank-of-ceylon-ratios")
DIAL=("https://www.investing.com/equities/dialog-axiata-ratios")
DIPD=("https://www.investing.com/equities/dipped-products-ratios")
ELPL=("https://www.investing.com/equities/elpitiya-plantations-ratios")
EXPO=("https://www.investing.com/equities/expolanka-hldg-ratios")
KVAL=("https://www.investing.com/equities/kelani-valley-plantations-ratios")
LFIN=("https://www.investing.com/equities/lb-finance-ratios")
LLUB=("https://www.investing.com/equities/chevron-lubricants-lanka-ratios")
LMF=("https://www.investing.com/equities/lanka-milk-foods-(cwe)-ratios")
MELS=("https://www.investing.com/equities/melstacorp-ltd-ratios")
OSEA=("https://www.investing.com/equities/overseas-realty-(ceylon)-ratios")
SUN=("https://www.investing.com/equities/sunshine-holdings-ratios")
TKYO=("https://www.investing.com/equities/tokyo-cement-co-(lanka)-ratios")

#creat timme
now = datetime.now()
tnd = now.strftime("%d/%m/%Y %H:%M:%S")


driver.get(url2)
time.sleep(1)
ASPI2 = driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
#print (ASPI2.text)

#driver.get(url1)
#time.sleep(3)
#ASPI1 = driver.find_element_by_xpath('/html/body/app-root/div/app-home-page/div/div[2]/div/div/div[1]/div/p[2]')
#print (ASPI1.text)

data1 = ["ASPI",ASPI2.text]
with open("stock update.csv","w",encoding='utf-8', newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)


#Creat CSV file
colom = { "Date and Time" , "company Name" , "Last Price" , "P/E Ratio" , "Price to Book" }
with open("stock update.csv" , "a" , newline='' ) as csvfile:
    writer = csv.writer (csvfile)
    writer.writerow (colom)
    

#ACL
driver.get(ACL)
#time.sleep(1)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')
#print(name.text)
#print(price.text)
#print(PE.text)
#print(PB.text)

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#AHUN
driver.get(AHUN)
#time.sleep(1)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')
#print(name.text)
#print(price.text)
#print(PE.text)
#print(PB.text)

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#CHL
driver.get(CHL)
#time.sleep(1)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')
#print(name.text)
#print(price.text)
#print(PE.text)
#print(PB.text)

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#COCO
driver.get(COCO)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#COMB
driver.get(COMB)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#DIAL
driver.get(DIAL)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#DIPD
driver.get(DIPD)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#ELPL
driver.get(ELPL)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#EXPO
driver.get(EXPO)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#KVAL
driver.get(KVAL)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#LFIN
driver.get(LFIN)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#LLUB
driver.get(LLUB)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#LMF
driver.get(LMF)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#MELS
driver.get(MELS)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#OSEA
driver.get(OSEA)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#SUN
driver.get(SUN)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)

#TKYO
driver.get(TKYO)
name=driver.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
price=driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[1]')
PE=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]')
PB=driver.find_element_by_xpath('/html/body/div[5]/section/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]')

data1 = [tnd ,name.text, price.text, PE.text, PB.text]
with open("stock update.csv","a", newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data1)


driver.quit()