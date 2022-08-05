import aiohttp

async def postToCta(session, path, payload):
    async with session.post(path, data=payload) as r:
        if (r.status != 200):
            print('An error occurred')
            print(r.status)
            print(await r.text())
            exit()
        response = await r.json()
        return response

async def login(session, playerIdString):
    path = '/site/api/user/login'
    payload = {'pidCode': playerIdString}
    return await postToCta(session, path, payload)

async def claim(session, freeGiftId, pid):
    path = '/site/api/user/gift/claim'
    payload = {'id': freeGiftId, 'pid': pid}
    return await postToCta(session, path, payload)

async def claimFreeGift(playerIdString):
    async with aiohttp.ClientSession('https://gzidlerpg.appspot.com') as session:
        print(f'Logging in with player id \'{playerIdString}\'')
        response = await login(session, playerIdString)
        if (response['success']):
            pid = response['data']['user']['pid']
            userName = response['data']['user']['name']
            if (response['data']['user']['hasChestToClaim']):
                giftId = response['data']['data']['giftId']
                chestName = response['data']['data']['chestName']
        else:
            print('Could not login')
            print(response)
            exit()

        print(f'Got pid {pid} ({userName})')

        if (response['data']['user']['hasChestToClaim']):
            print(f'Claiming gift {chestName}')
            response = await claim(session, giftId, pid)
            if(response['success']):
                print('Claimed gift successfully')
        else:
            print('Daily gift not available (anymore)')
            exit()
