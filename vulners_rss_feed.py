import feedparser
from bs4 import BeautifulSoup
import time


class Color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


def strip_html_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def print_rss_feed(url):
    feed = feedparser.parse(url)
    num_posts = int(
        input(f"{Color.GREEN}[+]{Color.RESET} Enter the number of posts to retrieve: "))
    time.sleep(1)
    print(
        f"{Color.GREEN}[+]{Color.RESET} Printing {Color.YELLOW}{num_posts}{Color.RESET} Posts.")
    print("\n"f"{Color.GREEN}{Color.UNDERLINE}Feed Title:{Color.RESET}",
          f"{Color.CYAN}", feed.feed.title)
    print(f"{Color.GREEN}{Color.UNDERLINE}Feed Description:{Color.RESET}",
          f"{Color.CYAN}", feed.feed.description)

    for entry in feed.entries[:num_posts]:
        print("\n"f"{Color.BLUE}{Color.UNDERLINE}Title:{Color.RESET}",
              f"{Color.YELLOW}{Color.BOLD}", entry.title, f"{Color.RESET}")
        print("\n"
              f"{Color.BG_CYAN}{Color.BLACK}Published Date{Color.RESET}:", entry.published)
        summary = strip_html_tags(entry.summary)
        # print("Summary:", entry.summary)
        print("\n"f"{Color.RED}{Color.BOLD}Summary:{Color.RESET}", summary)
        print("\n"f"{Color.BOLD}{Color.GREEN}LINK:{Color.RESET}", entry.link)
        print("\n\f")


# Example usage
rss_feed_url = "https://vulners.com/rss.xml?query=(type:thn%20OR%20type:threatpost)%20order:published"
print_rss_feed(rss_feed_url)
                            
