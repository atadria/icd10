import re

ICD_FILE = 'icd10.txt'

ICD_CODE_REGEX = re.compile('[A-Z][0-9]{2}')
ICD_GROUP_REGEX = re.compile(r'\([A-Z][0-9]{2}–[A-Z][0-9]{2}\)')


def file2dict(file):
    icd = {}
    with open(file, encoding='UTF-8') as f:
        for line in f:
            code = line[:3]
            if re.fullmatch(ICD_CODE_REGEX, code) is not None:
                icd[code] = line[3:].strip()
    return icd


def get_groups(file):
    groups = []
    with open(file, encoding='UTF-8') as f:
        for line in f:
            code = line[:3]
            if re.fullmatch(ICD_CODE_REGEX, code) is None:
                name = line.strip()[:-9].strip()
                group_code = line.strip()[-9:]
                if re.fullmatch(ICD_GROUP_REGEX, group_code) is None:
                    group_code = line.strip()[-5:]
                groups.append((name, group_code))
    return groups
