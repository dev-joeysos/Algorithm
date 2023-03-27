import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# 입력 리스트 생성
N = 100
arr = [random.randint(1, N) for _ in range(N)]

# 삽입정렬 함수


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        yield arr  # 애니메이션을 위해 현재 리스트를 반환

# 애니메이션 함수


def animate(frame):
    plt.cla()  # 이전 플롯 지우기
    plt.bar(range(len(frame)), frame)  # 막대그래프 플롯
    plt.title('Insertion Sort')


# 애니메이션 실행
fig = plt.figure()
ani = animation.FuncAnimation(
    fig, animate, frames=insertion_sort(arr), repeat=False)
plt.show()
