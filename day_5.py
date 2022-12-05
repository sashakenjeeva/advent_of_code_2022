crates={
"crate_1":["T","P","Z","C","S","L","Q","N"],
"crate_2":["L","P","T","V","H","C","G"],
"crate_3":["D","C","Z","F"],
"crate_4":["G","W","T","D","L","M","V","C"],
"crate_5":["P","W","C"],
"crate_6":["P","F","J","D","C","T","S","Z"],
"crate_7":["V","W","G","B","D"],
"crate_8":["N","J","S","Q","H","W"],
"crate_9":["R","C","Q","F","S","L","V"]}

import re
with open("/Users/sashakenjeeva/Desktop/Advent of code/2022/input_5.txt", "r") as f:
    read=f.read()
    instructions=read.split("\n")
    new_instr=[]
    for x in instructions:
        new_x=[int(x) for x in re.findall(r'\d+', x)]
        new_instr.append(new_x)
        
def crate_mover(rule):
    for instr in rule:
        from_crate=crates[f'crate_{instr[1]}']
        print(instr[0], "from", f'crate_{instr[1]}', from_crate)
        to_crate=crates[f'crate_{instr[2]}']
        print("to", f'crate_{instr[2]}', to_crate)
        reverse=list(reversed(from_crate))
        how_many=reverse[0:instr[0]]
        to_crate.extend(how_many)
        crates[f'crate_{instr[1]}'] = reverse[::-1][:-instr[0]]
        print("final", f'crate_{instr[2]}', to_crate)
        print("final",f'crate_{instr[1]}', crates[f'crate_{instr[1]}'])
        
  crate_mover(new_instr)
  
  crates
