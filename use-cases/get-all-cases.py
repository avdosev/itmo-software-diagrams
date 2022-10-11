with open('full-use-case.puml', encoding='utf-8') as f, open('result.txt', 'w', encoding='utf-8') as out:
    for line in f:
        line = line.strip()
        if line.startswith('usecase'):
            print(line[line.find('"')+1:line.rfind('"')], file=out)
