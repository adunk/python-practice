from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start Tag: {tag}')
        for attr in attrs:
            print(f'attr: {attr}')

    def handle_endtag(self, tag):
        print(f'End tag: {tag}')

    def handle_comment(self, data):
        print(f'Comment: {data}')

    def handle_data(self, data):
        print(f'Data: {data}')

parser = HTMLParser()
parser.feed('<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder!</h1></body></html>')
print()


html_file = open('sample.html', 'r')
s = ''
for line in html_file:
    s += line

parser.feed(s)
