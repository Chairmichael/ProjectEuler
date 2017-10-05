#!/usr/bin/env 
# Get_Problem.py


def get_prob(num, url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    prob_title = tree.xpath('//h2/text()')[0]
    prob_desc = tree.xpath('//div[@class="problem_content"]/p/text()')
    print(prob_title)
    prob_desc = [textwrap.fill(p, 78) for p in prob_desc]
    prob_desc = '\n'.join(prob_desc)
    print(prob_desc)
    return prob_title, prob_desc

def select_prob(ext, num):
    if num is not None:
        return num
    # path for the complete and incomplete directories
    dirs = [starting_dir + '\\Complete', starting_dir + '\\Incomplete']
    largest = 0
    try:
        for d in dirs:
            for filename in os.listdir(d):
                if filename.endswith(ext):
                    num = int(filename[0:4])
                    if int(filename[0:4]) > largest:
                        largest = num
    except Exception as e:
        raise e
    finally:
        return largest + 1

def create_prob_file(num, content):
    pass

def get_file_ext(lang):
    if lang is None:
        # use the name of the root dir
        lang = starting_dir.split('\\')[-1]
    lang = ''.join(lang.lower().split(' ')) # lowercase and remove spaces
    if lang == 'python': return '.py'
    elif lang == 'java': return '.java'
    elif lang == 'c': return '.c'
    elif lang in ('cpp', 'c++', 'cplusplus'): return '.cpp'
    elif lang == 'go': return '.go'

def main(cl_args):
    basic_code = ("#!/usr/bin/env\n# {fn}.py\n{desc}\n\ndef main():\n"
                "    pass\n\nif __name__ == '__main__':\n"
                "    import os, sys\n    main()\n")
    global starting_dir
    starting_dir = os.getcwd()

    extention = get_file_ext(lang=cl_args.l)
    target = select_prob(ext=extention, num=cl_args.n)
    print(f'\nProblem __{target}__ selected\n')

    print('Connecting to projecteuler.net')
    prob_url = f'https://projecteuler.net/problem={target}'
    desc_text = get_prob(num=target, url=prob_url)
    create_prob_file(num=target, content=desc_text)

    if cl_args.o:
        #open problem webpage
        pass
    

if __name__ == '__main__':
    import os, sys, argparse, textwrap
    from lxml import html
    import requests
    
    # setup command-line arguments
    description_text = (
        'Initializes a file for an Euler Problem, with the problem\'s '
        'description via web-scraping.\n'
        'When ran without any arguments, this will figure '
        'out what the next problem is from the contents of '
        'the "Complete" and "Incomplete" directories.\n'
        'If needed, this will accept an integer to manually select the problem.'
        )
    parser = argparse.ArgumentParser(description=description_text)

    n_helptext = 'an integer of the problem to initialize with a file'
    parser.add_argument('-n', metavar='N', type=int, 
                        nargs='?', help=n_helptext)

    t_helptext = 'the programming language to initialize (default is python)'
    parser.add_argument('-l', metavar='L', type=str, 
                        nargs='?', help=t_helptext)

    o_helptext = 'provide this to not open the problem\'s webpage by default'
    parser.add_argument('-o', metavar='O', default=True, help=t_helptext)

    args = parser.parse_args()
    main(args)
