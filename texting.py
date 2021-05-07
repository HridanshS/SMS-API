import requests
#list_names = ['Mr XYZ', 'Hridansh'] 
#list_ph_nos = [RAN-DOM-NUMB, 8722337968]

if len(list_names) == len(list_ph_nos):
  for i in range(len(list_names)):
    resp = requests.post('https://textbelt.com/text', {
      'phone': list_ph_nos[i],
      'message': f'Hi {list_names[i]} (again haha). \nMESSAGE HERE',
      'replyWebhookUrl':f'https://my.site/api/handleSmsReply',
      'key': '4e849094e47307148a0332ca914d027cd08d1b6axBOXp6mLbCMUBvOUT6jW0QFK6', #Buy an API key from textbelt.com (this one has expired)  https://textbelt.com/
    })
    print(resp.json())


#b25fd2f6134f0c42d63ec586399102f67557dc2cdARhR5izAU7j0EPqY5qpSjkJt
#4e849094e47307148a0332ca914d027cd08d1b6axBOXp6mLbCMUBvOUT6jW0QFK6
