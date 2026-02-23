N, M = map(int, input().split())

site_dict = dict()

for _ in range(N):
    site, pw = input().split()
    site_dict[site] = pw

for _ in range(M):
    site = input()
    print(site_dict[site])