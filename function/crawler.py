#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests
from bs4 import BeautifulSoup
from reurl import reurl


target_search_temp = ""

def search(data):
    global target_search_temp
    target_search_temp="https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXW.mI4ddaGgAMYp7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3R3LmRpY3Rpb25hcnkuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNARxdWVyeQN5cnJyBHRfc3RtcAMxNTY5MTM3NjE5?p=%s&fr=sfp&iscqry="%(data)
    r = requests.get(target_search_temp) #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    composing = soup.prettify() #排版 測試用
    # print(composing)


    # In[54]:


    web_div = soup.find(id='web') #以id搜尋 web , 搜尋結果的div
    search = web_div.find("div",class_="dd cardDesign dictionaryWordCard sys_dict_word_card")
    # print(search.prettify())


    # In[55]:


    voc_info = {} # 建立字典

    #抓單字名
    word = search.span # 抓單字名
    voc_info.update({"word":word.text})  
    # print(voc_info)


    # In[69]:


    # KK、DJ音標 
    phonetic = search.find_all("div",class_="compList ml-25 d-ib")[0].find_all("span")
    print(phonetic)
    voc_info.update({"KK":phonetic[0].text,"DJ":phonetic[1].text})
    # print(voc_info)



    # In[88]:


    #詞性、中文
    speech = search.find_all("div",class_="compList mb-25 ml-25 p-rel")[0].find_all("li")
    list_speech_1 = []#詞性
    list_speech_2 = []#翻譯
    list_ans = ""
    for i in range(0,len(speech)):
        temp =speech[i].find_all("div")
        temp1 = temp[0].text#詞性
        temp2 = temp[1].text#翻譯
        list_speech_1.append(temp1)
        list_speech_2.append(temp2)
        list_ans += "("+str(i+1) + ") " + temp1 + " " + temp2 +  "\n" 
    # print(list_speech_1)
    # print(list_speech_2)

    s_url = reurl(target_search_temp)
    answer = "單字：" + voc_info["word"] + "\n" + "發音：" + voc_info["KK"] + " " + voc_info["DJ"] + "\n說明：\n" +list_ans + "\n\n資料來源：\n"+ s_url +"\nyahoo 字典"
    return answer
    # In[ ]:



