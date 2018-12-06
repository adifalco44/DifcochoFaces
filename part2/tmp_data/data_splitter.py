import os, sys

file_stems_training = []
file_stems_validation = []
file_stems_testing = []

for i in range(1,16):
    pre = ''
    if i < 10:
        pre= '0'
    file_stem = 'subject{0}{1}.'.format(pre,i)
    ### TRAINING ###
    if i < 6:
        for emote in ['centerlight','glasses','happy','leftlight','noglasses','normal','rightlight','sad','sleepy','surprised','wink']:
            file_name = file_stem+emote
            print(file_name)
            print('move {0} training'.format(file_name))
            os.system('move {0} training'.format(file_name))
    ### VALIDATION ###
    elif i > 5 and i <11:
        for emote in ['centerlight','glasses','happy','leftlight','noglasses','normal','rightlight','sad','sleepy','surprised','wink']:
            file_name = file_stem+emote
            print('move {0} validation'.format(file_name))
            os.system('move {0} validation'.format(file_name))
    ### TESTING ###
    else:
        for emote in ['centerlight','glasses','happy','leftlight','noglasses','normal','rightlight','sad','sleepy','surprised','wink']:
            file_name = file_stem+emote
            print('move {0} testing'.format(file_name))
            os.system('move {0} testing'.format(file_name))

'''
for emote in
    for set in [file_stems_training,file_stems_validation,file_stems_testing]:
        for stem in set:
            try:
                file_names_dict[stem].append('{0}.{1}'.format(stem,emote))
            except KeyError:
                file_names_dict[stem] = ['{0}.{1}'.format(stem,emote)]

            file_names_list.append('{0}.{1}'.format(stem,emote))

print(file_names_dict)
print(file_names_list)


for key in file_names_dict.keys():
    for i in range(0,len(file_names_dict[key])/3):

'''
