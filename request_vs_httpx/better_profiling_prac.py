import cProfile
import pstats
import httpx
import asyncio
import re
async def my_func():
    with open('top15USWebsites.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]
    
    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print('finished parsing')
    print(f'{count_https=}')
    print(f'{count_http=}')
    print(f'{count_https/count_http=}')


def main():
    with cProfile.Profile() as pr:
        asyncio.run(my_func())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='needs_profiling_prac.prof')  
    
if __name__=="__main__":
    main()
    
    
 