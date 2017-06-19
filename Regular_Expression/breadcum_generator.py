# -*- coding: utf-8 -*-
"""
Created: 30/05/2017
Author: Amartya Gupta
"""
from re import findall


def clean(url):
    test = ["html", "htm", "php", "asp"]
    u = findall(r"(/([\w-]+)\.?(\w+)?)", url)
    if u:
        if "." in u[0][0] and u[0][2] not in test:
            u.pop(0)
    u = [i[1] for i in u if i[1].lower() != "index"]
    u.insert(0, "home")
    return u


def shortner(tag):
    no_words = ["the", "of", "in", "from", "by", "with", "and",
                "or", "for", "to", "at", "a"]
    if len(tag) <= 30:
        return ' '.join(tag.split("-")).upper()
    else:
        tag = [i[0].upper() for i in tag.split("-") if i not in no_words]
        return ''.join(tag)


def generate_bc(url, separator):
    url = clean(url)
    result = []
    a_tag = '''<a href="{}">{}</a>'''
    span_tag = '''<span class="active">{}</span>'''
    
    for j, i in enumerate(url):
        if j == 0 and len(url) > 1:
            result.append(a_tag.format("/", i.upper()))
        else:
            if j < len(url) - 1:
                result.append(a_tag.format("/{}/".format('/'.join(url[1:(j + 1)])), shortner(i)))
            else:
                result.append(span_tag.format(shortner(i)))

    return separator.join(result)


print(generate_bc("pippi.pi/test.php", " - "))