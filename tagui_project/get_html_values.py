import requests
from bs4 import BeautifulSoup

url_link = 'https://campaigns.hkjc.com/goracing/ch/'


def get_video_names() -> list:
    r = requests.get(url_link)

    Soup = BeautifulSoup(r.text, 'lxml')

    # creating a list of all common heading tags
    heading_tags = ["h3"]
    video_names = []
    for tags in Soup.find_all(heading_tags):
        if tags.text.strip() == '賽馬 101':
            break
        video_names.append(tags.text.strip())
    return video_names


if __name__ == '__main__':
    # user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    #
    # # header variable
    # headers = {'User-Agent': user_agent}
    #
    # request = requests.get(url_link, cookies={'ev_sync_dd': '20221011'}, headers=headers)
    #
    # soup = BeautifulSoup(request.content, 'html.parser')
    #
    # print(soup.get_text)
    #
    # tags = soup.find_all('span', {'class': 'viewcount'})
    # t = tags[0]
    pass
