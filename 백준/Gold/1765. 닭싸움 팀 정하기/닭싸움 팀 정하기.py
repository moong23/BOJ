import sys
input = sys.stdin.readline

num_people = int(input())
num_relationships = int(input())


parent = list(range(num_people))


def find(person):
    if person == parent[person]:
        return person
    parent[person] = find(parent[person])
    return parent[person]


def merge(person_a, person_b):
    root_a = find(person_a)
    root_b = find(person_b)

    if root_a <= root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


def init():
    enemies = {person: [] for person in range(num_people)}

    for _ in range(num_relationships):
        relationship_type, person_a, person_b = input().split()
        person_a, person_b = int(person_a) - 1, int(person_b) - 1

        if relationship_type == 'F':
            merge(person_a, person_b)
        else:
            enemies[person_a].append(person_b)
            enemies[person_b].append(person_a)

    return enemies


def union(person_a, person_b, enemy_map):
    for enemy_of_a in enemy_map[person_a]:
        for enemy_of_b in enemy_map[person_b]:
            if enemy_of_a == enemy_of_b:
                return True
    return False


def calc(enemy_map):
    for person_a in range(num_people - 1):
        for person_b in range(person_a + 1, num_people):
            if parent[person_a] != parent[person_b] and union(person_a, person_b, enemy_map):
                merge(person_a, person_b)

    for person in range(num_people):
        find(person)

    distinct_groups = len(set(parent))
    print(distinct_groups)


enemy_map = init()
calc(enemy_map)
