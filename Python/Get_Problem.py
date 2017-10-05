#!/usr/bin/env 
# Get_Problem.py


def main(cl_args):
    basic_code = ("#!/usr/bin/env\n# {}.py\n\n\ndef main():\n"
                "    pass\n\nif __name__ == '__main__':\n"
                "    import os, sys\n    main()")
    # print(basic_code)
    # TODO: Get target problem
    # TODO: Web-scrape to get the problem description
    

if __name__ == '__main__':
    import os, sys, argparse
    
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
    parser.add_argument('-n', metavar='N', type=int, nargs='+', help=n_helptext)

    t_helptext = 'the programming language to initialize (default is python)'
    parser.add_argument('-t', metavar='t', type=int, nargs='+', help=t_helptext)

    args = parser.parse_args()
    main(args)