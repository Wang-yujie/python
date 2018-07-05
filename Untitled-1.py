import sys
# import re# import re
# # numRegex = re.compile(r'''(
# #     ((\d)*)?
# #     ((\,)*)?
# #     (\d{3})*
# #     ((\,)*)?
# #     ((\d)*)?
# #     )''',re.VERBOSE)
# # numRegex = re.compile(r'
# #     [A-Z][a-zA-Z]* '
# #     re.VERBOSE)
# # re = numRegex.sub('Hei ','Satoshi Nakamoto' 'Alice Nakamoto' 'RoboCop Nakamoto' ' satoshi Nakamoto ' ' Mr. Nakamoto ' 'Nakamoto ' ' Satoshi nakamoto ')
# numRegex = re.compile(r'[Alice|Bob|Carol] [eats|pets|throws] [apples|cats|baseballs]\.')
# # re = numRegex.sub('Hei','Satoshi Nakamoto       Alice Nakamoto       RoboCop Nakamoto        satoshi Nakamoto        Mr. Nakamoto       Nakamoto         Satoshi nakamoto')
# ok =numRegex.findall('Alice eats apples.       Bob pets cats.       Carol throws baseballs.     Alice throws Apples.    BOB EATS CATS.     RoboCop eats apples.    ALICE THROWS FOOTBALLS.    Carol eats 7 cats.')
# print(ok)
result = []
with open sys.argv[1] as txt:
    lines = txt.readlines()
    num = 0
    times = 0
    length = len(lines)
    while True:
        lis = []
        out_line = []
        if num == length:
            break
        else:
            target = lines[num]
            gene = target.split("\t")[0]
            lis.append(gene)
            out_line.append(target)
            times += 1
            while True:
                num +=1
                line = lines[num]
                gene2 = line.split("\t")
                if gene2 in lis:
                    times +=1
                    out_line.append(line)
                else:
                    break
            if times > 3:
                for i in out_line:
                    result.append(i)
            else:
                pass
    re = "\n".join(result)
print(re)


