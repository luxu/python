import os

from carpet import async_get_pyjob_codes, async_get_pyjob_content

JOBS_DIRECTORY = 'jobs/pyjobs'

if __name__ == '__main__':

    pyjob_codes = async_get_pyjob_codes(initial_page=1, final_page=7)
    contents = async_get_pyjob_content(pyjob_codes)

    for pyjob_code, content in contents:
        if not content:
            continue

        filename = 'job{}.txt'.format(pyjob_code)
        full_filename = os.path.join(JOBS_DIRECTORY, filename)

        with open(full_filename, 'w') as pyjob_file:
            pyjob_file.write(content)
