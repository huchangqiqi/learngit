import os

cst_dict = {}
new_dict = {}


def main():
    with open("E:/c_scenic_type.txt", 'r', encoding='utf-8') as cst_f:
        for line in cst_f.readlines():
            s_line = line.split()
            k = s_line[1]
            v = s_line[0]
            cst_dict[k] = v
            #   print(cst_dict)
    with open("E:/新景点补全.txt", 'r', encoding='utf-8') as new_f:
        for line in new_f.readlines():
            s_line = line.split()
            k = s_line[0]
            v = s_line[1].split('，')
            new_dict[k] = v


    for (numId, cstypes) in new_dict.items():
        for cstype in cstypes:
            cst_id = cst_dict[cstype]
            if cst_id:
                # print( "num_id:" + k + " cst_id:" + cst_id)
                sql = "insert into c_scenic_type_mapping (num_id,cst_id,source_id,create_time) VALUE ({0},{1},{2},{3})".format(
                    numId, cst_id, 2, "now()")
                print(sql)
            else:
                print(cstype)


if __name__ == '__main__':
    main()
