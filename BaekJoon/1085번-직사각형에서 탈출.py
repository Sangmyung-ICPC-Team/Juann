x, y, w, h = map(int, input().split())

# 나의 상, 하, 좌, 우 의 값 중 가장 작은 값이 경계까지의 최소 거리이다.
arr = [h-y, w-x, y, x]
print(min(arr))
