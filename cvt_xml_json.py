import xmltodict
import json
import os


def xml_to_dict(xmlstr):
    """convert xml file to json file"""
    convertjson = xmltodict.parse(xmlstr,encoding='utf-8')
    jsonstr = json.dumps(convertjson,indent=4)
    return jsonstr


def json_to_xml(jsonstr):
    """convert json file into xml"""
    xmlstr = ''
    jsdict = json.loads(jsonstr)
    try:
        xmlstr = xmltodict.unparse(jsdict,encoding='utf-8')
    except:
        xmlstr = xmltodict.unparse({'request':jsdict}, encoding='utf-8')
    finally:
        return xmlstr


def batch_convert(dir_path):
    """convert all the file in a directory """
    filelist = os.listdir(dir_path)
    total_num = len(filelist)
    for item in filelist:
        if item.endswith('.xml'):
            # item is img_dir,item[:] is number; this is the xml path
            xml_path = os.path.join(dir_path,item[:4]+'.xml')
            with open(xml_path,'r') as f:
                xml_str = f.read()
            json_str = xml_to_dict(xml_str)

            # json path
            json_path = os.path.join('test/test_json/',item[:4]+'.json') # adjust here
            json_file = open(json_path,'w')
            json_file.write(json_str)
            json_file.close()
            print ('total %d to convert & converted %d xmls' % (total_num,int(item[:4])))


batch_convert('test/test/')  # the xml file dir





