'''
비교 코드: 멀티스레드 vs 멀티프로세싱
- 멀티스레드: GIL(Global Interpreter Lock)로 인해 CPU 바운드 작업에 비효율적
- 멀티프로세싱: 각 프로세스가 독립된 메모리 공간을 가지므로 CPU 바운드 작업에 적합
'''

import threading
import multiprocessing
import time

# CPU에 부담을 줄 계산 함수
def cpu_task(n):
    total = 0
    for i in range(1, n+1):
        total += i*i
    return total

# ----- 멀티스레드 -----
def multithread_test(n, num_threads):
    threads = []
    start = time.time()
    for _ in range(num_threads):
        t = threading.Thread(target=cpu_task, args=(n,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print(f"[멀티스레드] 시간: {end - start:.3f}초")

# ----- 멀티프로세싱 -----
def multiprocessing_test(n, num_processes):
    processes = []
    start = time.time()
    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_task, args=(n,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end = time.time()
    print(f"[멀티프로세싱] 시간: {end - start:.3f}초")

if __name__ == "__main__":
    N = 10_000_000       # 계산량
    NUM = 4              # 스레드/프로세스 수

    print("=== CPU 연산 병렬성 테스트 ===")
    multithread_test(N, NUM)
    multiprocessing_test(N, NUM)
