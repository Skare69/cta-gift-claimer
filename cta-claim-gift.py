import gift_claimer
import asyncio
import sys

if (len(sys.argv) < 2):
    print("Please provide your player ID as the first parameter")
    exit()

playerIdString = sys.argv[1]
if (sys.platform == 'win32'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(gift_claimer.claimFreeGift(playerIdString))
