import base64
import re


def encode(text):
    return base64.b64encode(text.encode("ASCII")).decode()


def enhanceText(text):
    text = text.replace('.', '.', text.count('.')).replace(',', ', ', text.count(','))
    text = " ".join(text.split()).replace(" . ", ". ")
    return text


def stylish_text(text):
    text = text.lower()
    style_text = list('๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐')
    normal_text = list('abcdefghijklmnopqrstuvwxyz')

    result = []

    for char in list(text):
        if char in normal_text:
            result.append(style_text[normal_text.index(char)])
        else:
            result.append(char)

    return ''.join(result)


def checkForURLs(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?ยซยปโโโโ]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def replace_special_slash(text):
    characters = '!@#$%^&*()-+?_=,<>/".' + "''"

    new_string = ""
    for i in text:
        if i in characters:
            new_string += '\\'
        new_string += i
    return new_string
