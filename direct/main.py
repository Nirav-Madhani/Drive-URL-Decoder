import re
import base64


'''
Google-
Docs - doc,pdf
Slide - pdf,pptx
Sheet - xlsx,pdf,csv
'''
def one_drive(onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl
def dropbox(url):
    return url[:-1]+'1'
def google(url,format=None):
    fileId = re.search('[-\w]{25,}',url).group()
    if "/document/" in url:
        if format == None:
            return "https://docs.google.com/document/d/{0}/export?format=doc".format(fileId)
        else:
            return   "https://docs.google.com/document/d/{0}/export?format={1}".format(fileId,format)  
    elif "spreadsheets" in url:
        if format == None:
            return "https://docs.google.com/spreadsheets/d/{0}/export?format=xlsx".format(fileId) 
        else:
            return "https://docs.google.com/spreadsheets/d/{0}/export?format={1}".format(fileId,format) 
    elif "presentation" in url:
        if format == None:
            return "https://docs.google.com/presentation/d/{0}/export/pptx".format(fileId)
        else:
            return "https://docs.google.com/presentation/d/{0}/export/{1}".format(fileId,format)
    else:
        return "https://drive.google.com/uc?export=download&id={0}".format(fileId)

def getLink(url,format=None):

    if('google' in url):
        return google(url,format)    
    elif "1drv.ms" in url:
        return one_drive(url)
    elif "dropbox" in url:
        return dropbox(url)
    else:
        return "url pattern recognized"
print(getLink('https://docs.google.com/document/d/1cFs5CgPktVwdv1akoipa-egELkk5mVk7dU2ZOOmrxyA/edit?usp=sharing','pdf'))
