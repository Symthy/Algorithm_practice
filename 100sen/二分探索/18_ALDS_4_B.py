"""
2分探索
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
"""


def binary_search(array, search_value):
    left = 0               # 左端を設定
    right = len(array) - 1  # 右端を設定
    while left < right:
        mid = (left + right) // 2  # 中央位置
        if array[mid] < search_value:  # 探索値が中央値より大きいなら右へ
            left = mid + 1
        elif array[mid] > search_value:  # 探索値が中央値より小さいなら左へ
            right = mid - 1
        else:
            return mid
    return -1


def main():
    n = int(input())
    S_array = sorted(list(map(int, input().split())))
    q = int(input())
    T_array = sorted(list(map(int, input().split())))

    count = 0
    for t in T_array:
        if binary_search(S_array, t) != -1:
            count += 1
    print(count)


main()
