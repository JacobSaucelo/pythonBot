from selenium import webdriver
import time
import json

driver = webdriver.Firefox()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScwnHxuyLNGVHxArHYl3I6q0XLf2DRVL3hYtWk32bPQv4XSAA/viewform?usp=sf_link")


def main():
    f = open('./data.json')
    fData = json.load(f)


    for i in fData:
        time.sleep(1)
        
        nameBot = driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        nameBot.send_keys(i["name"])
        
        genderBot = driver.find_element('xpath', gender(i["gender"]))
        genderBot.click()

        occupationBot = driver.find_element('xpath', occupation(i["occupation"]))
        occupationBot.click()

        preferenceBot = driver.find_element('xpath', wtPref(i["wtPref"]))
        preferenceBot.click()

        shiftPrefBot = driver.find_element('xpath',sPref(i["sPref"]) )
        shiftPrefBot.click()

        submitBtn = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submitBtn.click()
        resetForm()

    f.close()    

def resetForm():
    submitAnother = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submitAnother.click()

def gender(g):
    match  g:
        case 2:
            return '//*[@id="i12"]'
        case default:
            return '//*[@id="i9"]'

def occupation(o):
    match  o:
        case 2:
            return '//*[@id="i25"]'
        case default:
            return '//*[@id="i22"]'
        
def wtPref(w):
    match  w:
        case 2:
            return '//*[@id="i38"]'
        case 3:
            return '//*[@id="i41"]'
        case default:
            return '//*[@id="i35"]'

def sPref(w):
    match  w:
        case 2:
            return '//*[@id="i54"]'
        case default:
            return '//*[@id="i51"]'


main()