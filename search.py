import webbrowser
# Taking input from user
def search(question):
        line = 'http://api.wolframalpha.com/v1/simple?appid=VKY3JH-44A8L5PK3X&i=%3F'
        index = line.find('%3F')
        output_line = line[:index] + question + line[index:]
        webbrowser.open(output_line)
        return



