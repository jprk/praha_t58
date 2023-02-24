import os

FILE_FROM = '../palmovka_cakovice_v2.net.xml'
FILE_TO = '../palmovka_cakovice.net.xml'
TYPE_MAP = dict()

with open(FILE_FROM, 'r', encoding='utf8') as fin:
    for line in fin.readlines():
        if '<edge' in line:
            # Trimp whitespaces
            line = line.strip()
            # Remove trailing >
            if line[-1] == '>':
                line = line[:-1]
            else:
                raise ValueError(f'Line does not end with >: `{line}`')
            # print(line)
            attribs = line.split()[1:]
            elem_id = None
            elem_type = None
            for a in attribs:
                idx = a.find('=')
                if idx:
                    aid = a[:idx]
                    aval = a[idx+1:].strip('"')
                    if aid == 'id':
                        elem_id = aval
                    elif aid == 'type':
                        elem_type = aval
            if elem_id is not None and elem_type is not None:
                TYPE_MAP[elem_id] = elem_type
                print(f'{elem_id} type {elem_type}')


with open(FILE_TO + '.new.xml', 'w', encoding='utf8') as fout:
    with open(FILE_TO, 'r', encoding='utf8') as fin:
        for line in fin.readlines():
            if '<edge' in line:
                # Trimp whitespaces
                tline = line.rstrip()
                # Remove trailing >
                if tline[-1] == '>':
                    tline = tline[:-1]
                else:
                    raise ValueError(f'Line does not end with >: `{line}`')
                # print(line)
                attribs = tline.split()[1:]
                elem_id = None
                elem_has_type = False
                elem_func_ok = False
                for a in attribs:
                    idx = a.find('=')
                    if idx:
                        aid = a[:idx]
                        aval = a[idx+1:].strip('"')
                        if aid == 'id':
                            elem_id = aval
                        elif aid == 'type':
                            elem_has_type = True
                        elif aid == 'function':
                            elem_func_ok = ( aval == 'internal' or aval == 'walkingarea' or aval == 'crossing' )
                #
                if elem_id is not None and not elem_has_type:
                    if not elem_func_ok:
                        elem_type = 'highway.secondary'
                        if elem_id in TYPE_MAP:
                            elem_type = TYPE_MAP[elem_id]
                            print(f'{elem_id} will get type `{elem_type}`')
                        else:
                            print(f'{elem_id} has no type and is not internal, crossing, or walkingarea, adding `{elem_type}`')
                            # print('  -->', tline)
                        line = f'{tline} type="{elem_type}">'
                        print(line)
                        line += '\n'
            # write it out
            fout.write(line)
