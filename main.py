from io import BytesIO
import amino
import asyncio
import requests

email = input("input email >")
password = input("input password >")






google = "https://www.google.com/logos/doodles/2021/fathers-day-2021-august-08-6753651837109004-law.gif"
print("starting")

def upload(url):
    link = requests.get(url)
    content = link.content
    result = BytesIO(content)
    return result



async def main():
    client = amino.Client()
    await client.login(email=email, password=password)
    comid = input ("community link >")
    comid = client.get_from_code(comid).objectId
    chatId = input("chat link >")
    z = client.get_from_code(chatId)
    x = upload(google)
    thelink = client.upload_media(file=x,fileType='image')
    print(thelink)
    sc = await amino.SubClient(aminoId=comid, profile=client.profile)
    print(client.profile.nickname)
    await subclient.send_message(chatId="CHAT ID", message="MESSAGE",linkSnippet=thelink,linkSnippetImage=x)






loop = asyncio.get_event_loop()
loop.run_until_complete(main())


print("started")