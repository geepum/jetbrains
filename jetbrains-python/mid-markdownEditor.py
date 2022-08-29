#!/opt/homebrew/opt/python@3.10/bin/python3

lst = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line', '!help']
white_board = ''

def help():
    print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done''')


def header():
    while True:
        level = int(input('Level: '))
        if 1 <= level <= 6:
            break
        else:
            print('The level should be within the range of 1 to 6')
    
    text = input('Text: ')

    return f"{'#' * level} {text}"


def bold():
    text = input('Text: ')

    return f"**{text}**"


def plain():
    text = input('Text: ')
    return text


def inline_code():
    text = input('Text: ')
    return f"`{text}`"


def new_line():
    return '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f"[{label}]({url})"


def italic():
    text = input('Text: ')
    return f"*{text}*"


while True:
    init_q = input('Choose a formatter: ')

    if init_q == '!done':
        break

    else:
        if init_q not in lst:
            print('Unknown formatting type or command')

        elif init_q == '!help':
            help()

        elif init_q == 'header':
            white_board += header() + '\n'

        elif init_q == 'bold':
            white_board += bold()

        elif init_q == 'plain':
            white_board += plain()
        
        elif init_q == 'inline-code':
            white_board += inline_code()

        elif init_q == 'new-line':
            white_board += new_line()

        elif init_q == 'link':
            white_board += link()

        elif init_q == 'italic':
            white_board += italic()


    print(white_board)