#!/usr/bin/python

'''A module for parsing an Eiken Script text file into a REAPER Clip
Splicer JSON string.
'''

import argparse
import json
import random
import re


def parse_args():
    '''Parses and returns the command line arguments.
    '''
    parser = argparse.ArgumentParser(
        description='''Parse the given file into a json file that
        represents it.''')
    parser.add_argument('filename',
                        help='''The file to parse.
                        The file should be a .txt file whose format is 
                        specified in README.md. ''')
    args = parser.parse_args()
    return args


def read_file_into_object(filename):
    '''Reads an Eiken listening test file into an Python dictionary and
    returns the object.

    Args:
        filename: The file that describes the Eiken listening test.

    Returns:
        An object that represents the Eiken listening test.
    '''
    with open(filename, encoding='utf-8') as script_file:
        lines = script_file.readlines()
        # Determine the project title.
        project_title = lines.pop(0).partition('//')[0].strip()
        # Initialize a list of sections to be parsed later.
        sections = []

        # Iterate over the lines, creating a new list of lines for each
        # section within the text.
        this_section = None
        for line in lines:
            # Ignore // comments
            line = line.partition('//')[0].strip()
            # Ignore empty lines
            if not line:
                continue
            if line.startswith('[Section]'):
                # This line begins a new section.
                if this_section is not None:
                    sections.append(this_section)
                this_section = {}
                title = line.partition('[Section]')[2].strip()
                this_section['title'] = title
                this_section['lines'] = list()
            else:
                this_section['lines'].append(line)
        # Add the most recently created section to the result.
        if this_section is not None:
            sections.append(this_section)
    return parse_sections(project_title, sections)


def parse_sections(project_title, sections):
    '''Parses a list of sections and returns an Python dictionary that
    contains the same information.

    Args:
        project_title: The title of the project.
        sections: A list of sections.

    Returns:
        A dict that contains all the information in the sections.
    '''
    result = {}
    result['title'] = project_title
    result['path'] = 'clips'
    components = []
    for section in sections:
        components.append(parse_section(section))
    result['sections'] = components
    return result


def parse_section(section):
    '''Parses a list of lines that represent a section and returns an
    object.

    Args:
        section: A list of lines for each section.

    Returns:
        A dict that contains all the data for the given section.
    '''
    # Initialize the result.
    result = {}
    result['name'] = section['title']

    # Initialize a list of questions that belong to this section.
    questions = []

    # Iterate over all the lines and parse them accordingly.
    this_question = None
    for line in section['lines']:
        if line.startswith('#'):
            # This line contains question-specific data.
            # E.g. the question number and optional vocalist genders.
            if this_question is not None:
                # Add the previously read question to the result.
                questions.append(parse_question(this_question))

            # Initialize a new question to contain the following lines.
            this_question = {}
            number_and_vocalists = line.partition('#')[2].strip()
            partition = number_and_vocalists.partition('[')
            this_question['question_number'] = partition[0]
            if partition[2]:
                # If the vocalists are specified, parse them.
                vocalist_list = partition[2].partition(']')[0].split(',')
            else:
                # Randomize the vocalists.
                vocalist_list = ['M', 'F']
                random.shuffle(vocalist_list)
            # Create a map of vocalist names.
            # 'A' and 'B' --> genders 'M' and 'F'
            vocalists = {}
            # pylint: disable=consider-using-enumerate
            for i in range(len(vocalist_list)):
                vocalists[chr(65 + i)] = vocalist_list[i]
            this_question['vocalists'] = vocalists
            # Initialize a list of lines that will be added later.
            this_question['lines'] = list()
        else:
            # This is not the first line in a question.
            # Simply add the line to the result.
            this_question['lines'].append(line)
    # Parse and add the most recently read question.
    if this_question is not None:
        questions.append(parse_question(this_question))
    result['questions'] = questions
    return result


def parse_question(question):
    '''Parse a question and return an object.

    Args:
        question: A list of lines to be parsed.

    Returns:
        A dict containing all the data for the question.
    '''
    # Initialize a list of spoken lines for this question.
    lines = []
    for line in question['lines']:
        vocalist = None
        if line.startswith('[Question]'):
            # This line contains the text for a spoken question.
            line_type = 'question'
            line = line.partition('[Question]')[2].strip()
            lines.append({'type': 'question', 'text': line.strip()})
        elif line.startswith('[Choices - Not spoken]'):
            # The following lines are unspoken choices.
            line_type = 'silent'
        elif line.startswith('[Choices]'):
            # The following lines are spoken choices.
            line_type = 'choice'
        else:
            choice_number = None
            if re.search(r'\d', line):
                # This line begins with a digit --> It is a choice.
                line_type = 'choice'
                partition = line.partition('.')
                choice_number = partition[0]
                line = partition[2]
            else:
                # This line does not begin with a digit --> It is not a choice.
                line_type = 'prompt'
            if re.search(r'.*:', line):
                # This line has a colon --> There is a specified vocalist.
                partition = line.partition(':')
                vocalist = partition[0].strip()
                line = partition[2]
            line_object = {'type': line_type, 'text': line.strip()}
            # If the vocalist is specified, look up its gender.
            print('line => ' + line)
            print('question => ' + json.dumps(question))
            if vocalist:
                line_object['vocalist'] = question['vocalists'][vocalist]
            # If there is a choice number, add its data to the result.
            if choice_number:
                line_object['choice_number'] = choice_number
            lines.append(line_object)
    result = {
        'question_number': question['question_number'],
        'lines': lines
    }
    return result


def main():
    '''Parse the given file and print a JSON representation of Python
    dict object that represents the same data.
    '''
    args = parse_args()
    test_object = read_file_into_object(args.filename)
    print(json.dumps(test_object, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
