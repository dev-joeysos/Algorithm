import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# 입력 리스트 생성
N = 100
arr = [random.randint(1, N) for _ in range(N)]

# merge 함수


def merge(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    left_arr.append(float('inf'))  # 마지막에 무한대 값을 추가하여 비교가능하도록 함
    right_arr.append(float('inf'))  # 마지막에 무한대 값을 추가하여 비교가능하도록 함
    i, j = 0, 0
    for k in range(left, right+1):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        yield arr  # 애니메이션을 위해 현재 리스트를 반환

# merge_sort 함수


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(arr, left, mid)
        yield from merge_sort(arr, mid+1, right)
        yield from merge(arr, left, mid, right)

# 애니메이션 함수


def animate(frame):
    plt.cla()  # 이전 플롯 지우기
    plt.bar(range(len(frame)), frame)  # 막대그래프 플롯
    plt.title('Merge Sort')


# 애니메이션 실행
fig = plt.figure()
ani = animation.FuncAnimation(
    fig, animate, frames=merge_sort(arr, 0, len(arr)-1), repeat=False)
plt.show()
