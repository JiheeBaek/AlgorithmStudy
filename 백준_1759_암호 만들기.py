L, C = list(map(int, input().split(' ')))
alphabet=sorted(list(input().split(' ')))

def dfs(index, cnt, vowel, consonant, password):
    if cnt==L: #길이가 L인 암호
        if vowel>=1 and consonant>=2:
            print(password)
        return
    if index==C: #더이상 고를 수 있는 알파벳이 없다면 return
        return
    else:
        #현재 알파벳을 선택하는 경우
        if alphabet[index] in ['a', 'e', 'i', 'o', 'u']: #모음
            dfs(index+1, cnt+1, vowel+1, consonant, password+alphabet[index])
        else: #자음
            dfs(index+1, cnt+1, vowel, consonant+1, password+alphabet[index])
        # 현재 알파벳을 선택하지 않는 경우
        dfs(index+1, cnt, vowel, consonant, password)

dfs(0, 0, 0, 0, '')