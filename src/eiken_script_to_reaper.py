#! /usr/local/bin/python3
# coding=utf-8
"""A module to generate a REAPER Clip Splicer json file from a .txt file
specification.
"""

import argparse
import json
import sys
import jsonschema
import eiken_script_to_json
# pylint: disable = E0401
from beaunus_clip_splicer_tools import make_media_item, make_track, make_region

PAUSES = {
    'after_choice': 0.2,
    'after_instructions': 0.2,
    'after_three_choices': 0.2,
    'after_number': 0.2,
    'after_prompt': 0.2,
    'after_question': 0.2,
    'after_question_number': 0.2,
    'after_sentence': 0.2,
    'beginning_of_track': 0.2
}


def parse_args():
    """Parse and return the command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=('''Generate a REAPER Clip Splicer json file from a
        .json file specification.'''))
    parser.add_argument('-v', action='store_true', help='Show verbose output')
    parser.add_argument(
        '-schema', dest='schema', help='JSON schema to validate against')
    parser.add_argument(
        '-script_file',
        help='The file that represents the Eiken listening test information.')
    args = parser.parse_args()
    return args


def add_line_to_question(question, line):
    """Given a beaunus_clip_splicer question object and a dict that
    represents an Eiken line, adds the line to the question.
    """
    line_type = line['type']
    if line_type == 'silent':
        return

    # If this is a choice with a number, add the spoken number.
    if line_type == 'choice':
        if 'choice_number' in line:
            this_component = make_media_item(
                name='I/' + line['choice_number'],
                track='I',
                filename='I/' + line['choice_number'] + '.wav')
            question['components'].append(this_component)
            this_component = make_media_item(
                name='Pause after_number',
                track='Pauses',
                length=PAUSES['after_number'])
            question['components'].append(this_component)

    # If this is a question, add the 'Question' prompt.
    if line_type == 'question':
        this_component = make_media_item(
            name='I/Question.',
            track='I',
            filename='I/Question.wav')
        question['components'].append(this_component)
        this_component = make_media_item(
            name='Pause after_choice',
            track='Pauses',
            length=PAUSES['after_choice'])
        question['components'].append(this_component)

    # Add text for main component.
    if 'vocalist' in line:
        vocalist = line['vocalist']
    else:
        vocalist = 'I'
    this_component = make_media_item(
        name=vocalist + '/' + line['text'],
        track=vocalist,
        filename=vocalist + '/' + line['text'] + '.wav')
    question['components'].append(this_component)

    pause_name = 'after_' + line_type
    pause_after = make_media_item(
        name='Pause ' + pause_name,
        track="Pauses",
        length=PAUSES[pause_name])
    question['components'].append(pause_after)


def get_question(question):
    """Given a dict that represents an Eiken question, returns a
    beaunus_clip_splicer region that contains all the clips.
    """
    this_question = make_track(
        name='Question ' + question['question_number'],
        pre_track_pause_length=PAUSES['beginning_of_track'])
    this_question_number = make_media_item(
        name='Number ' + str(question['question_number']).strip().zfill(2),
        filename='I/Number ' +
        str(question['question_number']).strip().zfill(2) + '.wav',
        track='I'
    )
    pause_after = make_media_item(
        name='Pause after_question_number',
        track="Pauses",
        length=PAUSES['after_question_number'])
    this_question['components'].append(this_question_number)
    this_question['components'].append(pause_after)
    for _ in range(2):
        for line in question['lines']:
            add_line_to_question(this_question, line)

        pause_after = make_media_item(
            name='Pause after_question',
            track="Pauses",
            length=PAUSES['after_question'])
        this_question['components'].append(pause_after)
    return this_question


def get_section(section):
    """Given a dict that represents a section from an Eiken test,
    returns a beaunus_clip_splicer region that contains all the clips
    for that section.
    """
    this_section = make_region(
        name=section['name'])
    this_section_ids = section['name'].split('.')
    # Add the practice test instructions if this is section 1 of a test.
    if this_section_ids[1] == '1':
        practice_test_instructions_track = make_track(
            name='Practice Test ' + this_section_ids[0] + ' Instructions',
            pre_track_pause_length=PAUSES['beginning_of_track'])
        practice_test_instructions_item = make_media_item(
            name='Practice Test ' + this_section_ids[0] + ' Instructions',
            filename='JI/Instructions Practice Test ' + this_section_ids[0] + '.wav',
            track='JI'
        )
        pause_after = make_media_item(
            name='Pause after_instructions',
            track="Pauses",
            length=PAUSES['after_instructions'])
        practice_test_instructions_track['components'].append(practice_test_instructions_item)
        practice_test_instructions_track['components'].append(pause_after)
        this_section['components'].append(practice_test_instructions_track)
    # Add the section instructions
    section_instructions_track = make_track(
        name='Section ' + this_section_ids[1] + ' Instructions',
        pre_track_pause_length=PAUSES['beginning_of_track'])
    section_instructions_item = make_media_item(
        name='Section ' + this_section_ids[1] + ' Instructions',
        filename='JI/Instructions Section ' + this_section_ids[1] + '.wav',
        track='JI'
    )
    pause_after = make_media_item(
        name='Pause after_instructions',
        track="Pauses",
        length=PAUSES['after_instructions'])
    section_instructions_track['components'].append(section_instructions_item)
    section_instructions_track['components'].append(pause_after)
    this_section['components'].append(section_instructions_track)
    for question in section['questions']:
        this_section['components'].append(get_question(question))
    return this_section


def get_eiken_reaper_object(eiken_object):
    '''Given a dict that represents an eiken test, returns a dict that
    represents a beaunus_clip_splicer object.
    '''
    result = make_region(
        name=eiken_object['title'], path=eiken_object['path'])
    disc_instructions_track = make_track(
        name='Disc Instructions',
        pre_track_pause_length=PAUSES['beginning_of_track'])
    disc_instructions_item = make_media_item(
        name='Disc Instructions',
        filename='JI/Instructions Disc.wav',
        track='JI'
    )
    pause_after = make_media_item(
        name='Pause after_instructions',
        track="Pauses",
        length=PAUSES['after_instructions'])
    disc_instructions_track['components'].append(disc_instructions_item)
    disc_instructions_track['components'].append(pause_after)
    result['components'].append(disc_instructions_track)
    # pylint: disable = too-many-nested-blocks
    for section in eiken_object['sections']:
        result['components'].append(get_section(section))
    return result


def main():
    """Reads the command-line arguments and prints the JSON representation of
    the data for this project.
    """
    args = parse_args()
    if args.script_file:
        eiken_object = eiken_script_to_json.read_file_into_object(
            args.script_file)
    else:
        eiken_object = json.loads(sys.stdin.read())

    if args.v:
        print(
            json.dumps(obj=eiken_object, ensure_ascii=False,
                       sort_keys=False, indent=2),
            file=sys.stderr)

    eiken_reaper_object = get_eiken_reaper_object(
        eiken_object)

    # Validate the output
    if args.schema:
        with open(args.schema) as schema_file:
            schema = json.load(schema_file)
            jsonschema.validate(eiken_reaper_object, schema)

    eiken_reaper_json = json.dumps(
        obj=eiken_reaper_object, ensure_ascii=False, sort_keys=False, indent=2)

    print(eiken_reaper_json)


if __name__ == '__main__':
    main()
