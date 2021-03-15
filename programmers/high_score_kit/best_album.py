from collections import defaultdict


def solution(genres, plays):
    answer = []
    genres_plays = defaultdict(int)
    genres_songs = defaultdict(lambda: [])

    i = 0
    for g, p in zip(genres, plays):
        genres_plays[g] += p
        genres_songs[g].append((i, p))
        i += 1

    # print(genres_plays.items())
    # print(genres_songs)

    sorted_genres = sorted(genres_plays.items(), key=(lambda x: x[1]), reverse=True)
    # print(sorted_genres)

    for g in sorted_genres:
        sorted_songs = sorted(genres_songs[g[0]], key=(lambda x: x[1]), reverse=True)
        # print(sorted_songs)
        answer.append(sorted_songs[0][0])
        if len(sorted_songs) > 1:
            answer.append(sorted_songs[1][0])

    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
