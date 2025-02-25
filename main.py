from model import YoutubeBot
import json

def main(urls):
    bot = YoutubeBot()
    output = {}
    for url in urls:
        title, content = bot.get_transcript(url)

        output[title] = content
    
    bot.quit()

    
    return output



if __name__ == "__main__":
    links = []
    
    output = main(links)

    with open('output.json', 'w') as f:
        json.dump(output, f, indent = 4)
    