from model import YoutubeBot


def main(url):
    bot = YoutubeBot()
    title, content = bot.get_transcript(url)
    return title, content



if __name__ == "__main__":
    title, content = main("https://www.youtube.com/watch?v=qzD4fcd-FBY")
