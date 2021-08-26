import requests
import urllib
username="Arghya Sarkar"
password="secretmeh"
userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.134 Safari/537.36"
data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
#List all the memes
print('Here is the list of available memes : \n')
ctr = 1
for img in images:
    print(ctr,img['name'])
    ctr = ctr+1
id = int(input('Enter the serial number of the meme : '))
text0 = input('Enter first text : ')
text1 = input('Enter second text : ')
URL = 'https://api.imgflip.com/caption_image'
params = {
    'username':username,
    'password':password,
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1
}
response = requests.request('POST',URL,params=params).json()
print(response)
opener = urllib.request.URLopener()
opener.addheader('User-Agent', userAgent)
print(response['data']['url'])
filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')
