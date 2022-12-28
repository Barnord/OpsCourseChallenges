import requests

print('Please enter an html address.')
adrs = input()

options = ['1. GET', '2. POST', '3. PUT', '4. DELETE', '5. HEAD', '6. PATCH', '7. OPTIONS', '8. EXIT']
selection = ''

def printOptions():
  print('Please select a selection option:')
  for i in options:
    print(i)
  global selection
  selection = input()

def translate(res):
  if res.status_code == 200:
    print('Request successful.')
  elif res.status_code == 400:
    print("Bad request. This script probably isn't capable of handling it.")
  elif res.status_code == 403:
    print("Forbidden. Forever. I don't want to add auth to this.")
  elif res.status_code == 404:
    print("Site not found.")
  elif res.status_code == 408:
    print("Request timeout. Probably wasn't my code.")
  elif res.status_code == 500:
    print("The server is confused by what you're doing. This is the worst response code.")
  else:
    print("You found a response code I didn't make a reponse for. Congrats?\n",res)

printOptions()

while (selection !=8):
  confirm = input('Are you sure? [y/n]\n')
  if confirm !='y':
    selection = "9"
  elif selection=='1':
    translate(requests.get(adrs))
  elif selection=='2':
    translate(requests.post(adrs))
  elif selection=='3':
    translate(requests.put(adrs))
  elif selection=='4':
    translate(requests.delete(adrs))
  elif selection=='5':
    translate(requests.head(adrs))
  elif selection=='6':
    translate(requests.patch(adrs))
  elif selection=='7':
    translate(requests.options(adrs))
  elif selection=='8':
    print('goodbye')
  else:
    print("Try a number between 1-8.")
  printOptions()