import requests
import re
import threading
lock = threading.Lock()
def GET_URL(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.raise_for_status
        return r.text
    except:
        print("")

def Deal_Url(mylist,url):
    r = GET_URL(url)
    txt = re.findall(r'<li>.*?<a href=.*?</li>',r,re.DOTALL)
    
    for item in txt:
        
        name = re.findall(r'<h3><a.*?>(.*?)"',item,re.DOTALL)
        try:
            pic = re.findall(r'<img src="(.+?)"',item,re.DOTALL)[0]
            #print(pic)
            mylist.append([pic])
        except:
            continue

class Mythead(theading.Thread):
    url = 'http://www.umei.cc/meinvtupian/'
    def run(self):
        for page in range(1,15):
        print(page)
        mylist = []
        Deal_Url(mylist,url+str(page)+'.htm')
        try:
            Deal_Url(mylist,url+str(page)+'.htm')
            for item in mylist:
                lock.acquire()
                a = requests.get(item[0])
                print(item[0])
                with open('F://233/'+item[0].split('/')[-1],'wb') as d:
                    d.write(a.content)
                    d.close()
                lock.release()
        
        
    
def main():
    
    url = 'http://www.umei.cc/meinvtupian/'
    for page in range(1,15):
        print(page)
        mylist = []
        Deal_Url(mylist,url+str(page)+'.htm')
        try:
            Deal_Url(mylist,url+str(page)+'.htm')
            for item in mylist:
                a = requests.get(item[0])
                print(item[0])
                with open('F://233/'+item[0].split('/')[-1],'wb') as d:
                    d.write(a.content)
                    d.close()
        except:
            print('erro')
main()
