# https://www.hackerrank.com/challenges/py-the-captains-room/problem

fam_members = int(input())
room_nums = list(map(int, input().split(' ')))
rooms = set(room_nums)

print((sum(rooms)*fam_members - sum(room_nums))//(fam_members-1))