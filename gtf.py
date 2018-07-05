import  re
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))? # area code
#     (\s|-|\.)? # separator
#     (\d{3}) # first 3 digits
#     (\s|-|\.) # separator
#     (\d{4}) # last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
#     )''', re.VERBOSE)
# # Create email regex.
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+ # username
#     @ # @ symbol
#     [a-zA-Z0-9.-]+ # domain name
#     (\.[a-zA-Z]{2,4}) # dot-something
#     )''', re.VERBOSE)
# # Find matches in clipboard text.
# text = "324234435556"+"(112)-234-2233 ext 3345"+" yujie@163.com"
# # print(text)
# matches = []
# line = phoneRegex.findall(text)
# # print(line)
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#     print(groups)
# #     if groups[8] != '':
# #         phoneNum += ' x' + groups[8]
# #         matches.append(phoneNum)
# # for groups in emailRegex.findall(text):
# #     matches.append(groups[0])
# # # print(phoneNum)

# # if len(matches) > 0:
# #     print('Copied to clipboard:')
# #     print('\n'.join(matches))
# # else:
# #     print('No phone numbers or email addresses found.')

def strip_test(st):
    RE = re.compile(r'^\s[a-zA-Z0-9._%+-]*\s$')
    if RE:
        st.sub('',st)
    return st
if __name__ == "__main__":
    # print("yes")
    strip_test(" djdiedieidj ")