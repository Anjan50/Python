import feedparser
import webbrowser


def main():
    print("--Security News Website List--")
    print("[0]: TheHackerNews")
    print("[1]: ThreatPost")
    print("[2]: NakedSecurity")

    website_list = ("https://feeds.feedburner.com/TheHackersNews",
                    "https://threatpost.com/feed",
                    "https://nakedsecurity.sophos.com/feed")

    website_input = int(input("Enter website by number (0-2): "))

    NewsFeed = feedparser.parse(website_list[website_input])
    article_list = []
    article_link = []
    for i in range(5):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num = 1
    for article in article_list:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_link_click = False
    while not article_link_click:
        user_click = int(input("Choose the link you want to open (1-5): "))
        webbrowser.open(article_link[user_click - 1])
        article_link_click = True


main()
