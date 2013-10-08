import re

def parse_emails(emails_string):
    """
    Parse valid email addresses from string.

    :param emails_string: The text to parse
    :returns: A string of valid email addresses
    """
    regex = '[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}'
    return re.findall(regex, emails_string)
