import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '8722337968',
  'message': 'Hello Hridansh',
  'key': '4e849094e47307148a0332ca914d027cd08d1b6axBOXp6mLbCMUBvOUT6jW0QFK6',
})
print(resp.json())


#b25fd2f6134f0c42d63ec586399102f67557dc2cdARhR5izAU7j0EPqY5qpSjkJt
#4e849094e47307148a0332ca914d027cd08d1b6axBOXp6mLbCMUBvOUT6jW0QFK6
