import settings
from website.models import Website
from requests_html import HTMLSession
import threading
from time import time

session = HTMLSession()


def parse_website(link: str):
    print(f"Visiting website: {link}")

    website: Website
    try:
        r = session.get(link)
        links = r.html.absolute_links
        title = r.html.find('title', first=True)
        body = r.html.find('body', first=True)

        title = title.text if title else ''
        body = body.text if body else ''

        if not Website.objects.filter(link=link).exists():
            website = Website(title=title, content=body, link=link)
        else:
            website = Website.objects.filter(link=link).first()
            website.title = title
            website.content = body

        website.has_visited = True
        website.save()

        for l in links:
            if not Website.objects.filter(link=l).exists():
                Website.objects.create(link=l)
    except Exception as e:
        print(e)
        website = Website.objects.filter(link=link)
        website.delete()


if __name__ == '__main__':
    threads = []
    while Website.objects.filter(has_visited=False).exists():
        start_time = time()
        print(f'# of websites: {Website.objects.count()}')
        next_websites: [Website] = Website.objects.filter(has_visited=False)[:3]
        for w in next_websites:
            t = threading.Thread(target=parse_website, args=(w.link,))
            threads.append(t)
            t.start()

        for th in threads:
            th.join()

        print(f'Total time {time() - start_time}')
