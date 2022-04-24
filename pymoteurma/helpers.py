from bs4 import BeautifulSoup
import functools
import re



def string_to_soup( html_str ):
    soup =  BeautifulSoup(html_str, 'html.parser')
    [ s.extract() for s in soup(['iframe', 'script', 'style']) ]
    return soup


# removes all the unnecessary white space
# it is used as a wrapper around other functions ( it's applied on their output )
def sanitize(func):
    def replace_space(t):
        if t.isspace() and t != ' ':
            return ' '
        return t

    def sanitized(t):
        if type(t) == list:
            return list(map(sanitized, t))
        elif type(t) == dict:
            tt = {}
            for k in t:
                tt[sanitized(k)] = sanitized(t[k])
            return tt
        elif type(t) == str:
            t = ''.join(map(replace_space, t))
            t = t.strip()
            t = t.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').replace('\xa0', ' ')
            t = re.sub(' +', ' ', t)
            return t
        else:
            return t

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = sanitized(original_result)
        return modified_result

    return wrapper


