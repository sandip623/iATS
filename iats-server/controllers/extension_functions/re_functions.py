""" functions that depend on re (regexp) module i.e., stripping sub-strings from a string """
import re 

def extract_email_prefix(email: str) -> str:
    """ regex pattern (r -> raw string i.e., treats backslashes as literal characters) """
    pattern = r'^([^@]+)@'
    # use re.match() to find the first occurence of the pattern in the email
    match = re.match(pattern, email)
    if match:
        prefix = match.group(1)
    else:
        prefix = None
    return prefix