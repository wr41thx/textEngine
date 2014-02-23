#!/usr/bin/env python

'''
The Littlest Blood Cell
'''
character = {'stage': 'Begin'}
choice = {
    'Begin': {
        'description': 'You have made it to the heart.',
        'options': '1) Enter the right atrium\n2) Go back',
        'exits': {'1':'one', '2':'ten'}
    },
    'one': {
        'description': 'You have entered the right atrium.',
        'options': '1) Enter the right ventricle\n2) Go back',
        'exits': {'1':'two', '2':'ten'}
    },
    'two': {
        'description': 'You have entered the right ventricle',
        'options': '1) Go through the pulmonary valve\n2) Go back',
        'exits': {'1':'three', '2':'ten'}
    },
    'three': {
        'description': 'You have passed through the pulmonary valve',
        'options': '1) Go through the pulmonary artery\n2) Go back',
        'exits': {'1':'four', '2':'ten'}
    },
    'four': {
        'description': 'You have gone through the pulmonary artery',
        'options': '1) Enter the lungs\n2) Go back',
        'exits': {'1':'five', '2':'ten'}
    },
    'five': {
        'description': 'You have entered the lungs',
        'options': '1) Go through the left atrium\n2) Go back',
        'exits': {'1':'six', '2':'ten'}
    },
    'six': {
        'description': 'You have gone through the left atrium',
        'options': '1) Go through the left ventricle\n2) Go back',
        'exits': {'1':'seven', '2':'ten'}
    },
    'seven': {
        'description': 'You have gone through the left ventricle',
        'options': '1) Go through the aortic valve\n2) Go back',
        'exits': {'1':'eight', '2':'ten'}
    },
    'eight': {
        'description': 'You have gone through the aortic valve',
        'options': '1) Go to the rest of the body\n2) Go back',
        'exits': {'1':'nine', '2':'ten'}
    },
    'nine': {
        'description': 'You have gone through the body. Go blood cell!',
        'options': 'Enter "quit" to quit',
        'exits': {}
    },
    'ten': {
        'description': 'You went back. RIP',
        'options': 'Enter "quit" to quit',
        'exits': {}
    }
}
while True:
    next = choice[character['stage']]
    if not next['exits']:
	print next['description']
	break
    command = raw_input(next['description'] + ' > ')
    command_parts = command.split(None, 1)
    next_stage = command_parts[0]
    if next_stage in ['1', '2']:
        if next_stage in next['exits']:
            character['stage'] = next['exits'][next_stage]
            next = choice[character['stage']]
        else:
            print 'You cannot do that. Enter "o" for options.'
    elif next_stage not in ['o', 'quit', 'exit', 'stop']:
            print 'You cannot do that. Enter "o" for options.'
    if next_stage == 'o':
	print next['options']
    if next_stage in ['quit', 'exit', 'stop']:
        print 'Goodbye'
        break
