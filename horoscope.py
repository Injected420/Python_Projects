import requests
from bs4 import BeautifulSoup


def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    return soup.find("div", class_="main-horoscope").p.text


if __name__ == "__main__":
    print("[+]Daily Horoscope. \n")
    print(
        "[+]Enter your Zodiac sign's number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n",
    )
    zodiac_sign = int(input("[+]Choose your Sign's Number: ").strip())
    print("[+]Choose a Number:\n", "1.) yesterday\n", "2.) today\n", "3.) tomorrow\n")
    day_num = int(input("[+]Enter Number for the Day you want:  "))
    if day_num == 1:
        day = "Yesterday"
    elif day_num == 2:
        day = "Today"
    elif day_num == 3:
        day = "Tomorrow"
    else:
        print("[-]Error, please choose either 1, 2, or 3")
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)
