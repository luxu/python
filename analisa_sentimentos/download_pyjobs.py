import os
import re
from carpet import get_pyjob_codes, get_pyjob_content

JOBS_DIRECTORY = 'jobs/pyjobs'

if __name__ == '__main__':

    pyjob_codes = []
    for page in range(1, 7):
        if get_pyjob_codes(page=page):
            pyjob_codes += get_pyjob_codes(page=page)

    for pyjob_code in pyjob_codes[:5]:
        print('Downloading pyjob {}'.format(pyjob_code))
        _, content = get_pyjob_content(pyjob_code)

        if not content:
            continue

        filename = 'job{}.txt'.format(pyjob_code)
        full_filename = os.path.join(JOBS_DIRECTORY, filename)
        content = re.sub('\n+', " ", content)
        content = re.sub(' +', " ", content)
        print(content)
        with open(full_filename, 'w', encoding="utf8") as pyjob_file:
            pyjob_file.write(content)
