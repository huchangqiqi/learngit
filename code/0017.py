from lxml import etree
import xlrd,codecs,json

def load_data(path):
    xls = xlrd.open_workbook(path);
    sheet = xls.sheet_by_index(0)

    data = {}
    for x in range(sheet.nrows):
        detail = []
        length = len(sheet.row_values(x))
        for y in range(1,length):
            detail.append(sheet.row_values(x)[y])
        data[str(sheet.row_values(x)[0])] = detail
        #print(str(sheet.row_values(x)[1].encode("utf-8")))
    print(data)
    return json.dumps(data,ensure_ascii=False)

def write_data_to_xls(data):
    xml = codecs.open("student.xml","w",encoding="utf-8")
    ele_root = etree.Element("root")
    xml_root = etree.ElementTree(ele_root)
    xml_student = etree.SubElement(ele_root,"students")
    xml_student.text = str(data)

    xml.write(etree.tounicode(xml_root.getroot()))
    xml.close()
if __name__ == '__main__':
    data = load_data("student.xls")
    write_data_to_xls(data)

