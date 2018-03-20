with open("2a_raw.txt") as fh:
    lines = fh.readlines()
    #print(len(lines))
    print(lines)
    
'''
['40523115\t40523108\t40523116\t40523144\t40523111\t40523141\t40523104\t40523102\t40523123\n', 
'40523137\t40523117\t40523135\t40523147\t40523146\t40523145\t40523122\t40523136\t40523132\n', 
'40523127\t40523126\t40523125\t40523124\t40523118\t40523131\t40523121\t40523120\t40523119\n', 
'40523105\t40523106\t40523107\t40523143\t40523128\t40523129\t40523130\t40523139\t40523133\n', 
'40523142\t40523148\t40523140\t40523113\t40523138\t40523134\t\t\t\n']
'''
with open("2a_raw.txt") as fh:
    # 逐行讀出檔案資料, 並放入數列中
    lines = fh.readlines()
    # 設法用迴圈逐數列內容取出字串
    # 組序變數 g 起始值設為 0
    g = 0
    for i in range(len(lines)):
        # 利用 strip() 去除各行字串最末端的跳行符號
        #print(lines[i].strip())
        line = lines[i].strip()
        # 利用 split() 將以 \t 區隔的字串資料分離後納入 groups 字串
        groups = line.split("\t")
        #print(groups)
        for i in range(len(groups)):
            # 每組有三名組員
            if i%3 == 0:
                # 每三位組員組序增量 1
                g += 1
                print()
                print("第" + str(g) + "組:")
                print(groups[i])
            else:
                print(groups[i])