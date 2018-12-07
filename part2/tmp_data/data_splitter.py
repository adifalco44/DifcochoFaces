import os, sys

### INITS ###
method = "FEATURE_METHOD"

### FOR EVERY SUBJECT ###
for i in range(1,16):

    pre = ''
    if i < 10:
        pre= '0'
    file_stem = 'subject{0}{1}.'.format(pre,i)

    ### SPLIT BY SUBJECT ###
    if method=="SUBJECT_METHOD":
        for emote in ['centerlight','glasses','happy','leftlight','noglasses','normal','rightlight','sad','sleepy','surprised','wink']:
            file_name = file_stem+emote
            ### TRAINING ###
            if i < 6:
                print('move {0} training'.format(file_name))
                os.system('move {0} training'.format(file_name))
            ### VALIDATION ###
            elif i > 5 and i <11:
                print('move {0} validation'.format(file_name))
                os.system('move {0} validation'.format(file_name))
            ### TESTING ###
            else:
                print('move {0} testing'.format(file_name))
                os.system('move {0} testing'.format(file_name))

    ### SPLIT BY FEATURE ###
    elif method=="FEATURE_METHOD":
        ### TRAINING ###
        for emote in ['centerlight','glasses','happy','leftlight']:
            file_name = file_stem+emote
            print('move {0} training'.format(file_name))
            os.system('move {0} training'.format(file_name))
        ### VALIDATION ###
        for emote in ['noglasses','normal','rightlight','sad']:
            file_name = file_stem+emote
            print('move {0} validation'.format(file_name))
            os.system('move {0} validation'.format(file_name))
        ### TESTING ###
        for emote in ['sleepy','surprised','wink']:
            file_name = file_stem+emote
            print('move {0} validation'.format(file_name))
            os.system('move {0} validation'.format(file_name))
