# 구현할 기능
# 등장인물 리스트 제공되면, 원하는 인물의 대사 조회
# 특정 단어가 들어간 script lines 출력

import os, re

# 파일 가져오고 내용 저장
f = open('./pracdir_doit_py_living_programming/rickandmorty_script.txt', 'r', encoding='UTF8')
script = f.read()
f.seek(0)
sentences = f.readlines()
character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script)))]


def run():
    print('Rick and Morty Season 1 Episode 1 - <Pilot> 스크립트를 살펴보자!')

    while True:
        print('---------------------------------------------------')
        print('1. 특정 인물 대사 조회', '2. 특정 단어가 포함된 대사 조회', '3. 종료', sep='\n')
        ans = input('위의 메뉴 중 선택해 주세요! >> ')
        if ans == '1':
            character_search()
        elif ans == '2':
            word_search()
        elif ans == '3':
            print('안녕히 가세요!')
            exit()
        else:
            print('메뉴 중에 입력해 주세요.')


def character_search():
    for index, character_name in enumerate(character):
        print(str(index+1) + ". " + character_name)

    character_name = character[int(input('위 목록 중 검색하고자 하는 인물 번호를 입력해주세요! >> ')) - 1]

    character_pattern = character_name + ':.+'
    lines = re.findall(character_pattern, script)
    for line in lines:
        print(line)


def word_search():
    word = input('검색하고자 하는 단어를 입력해주세요! >> ')
    lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search(word, i)]

    if not lines:
        print('해당 단어가 포함된 대사가 없습니다!')
        return

    for line in lines:
        print(line)


run()

