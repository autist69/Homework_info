import numpy as np

n, m = map(int, input().split())
answer = np.full((n, m), 0)
n_start, m_start = 0, 0
n_end, m_end = n, m
counter, i = 0, 0
while i < n:
    for j in range(m_start, m_end):
        answer[n_start, j] = counter
        counter += 1

    n_start += 1

    if n_start >= n_end:
        break

    for j in range(n_start, n_end):
        answer[j, m_end - 1] = counter
        counter += 1

    m_end -= 1

    if m_start >= m_end:
        break

    for j in range(m_end - 1, m_start - 1, -1):
        answer[n_end - 1, j] = counter
        counter += 1

    n_end -= 1

    if n_start >= n_end:
        break

    for j in range(n_end - 1, n_start - 1, -1):
        answer[j, m_start] = counter
        counter += 1

    m_start += 1

    if m_start >= m_end:
        break

    i += 2

print(answer)
