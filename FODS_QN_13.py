from collections import Counter

likes = [100, 200, 150, 300, 250, 200, 150, 100, 200, 300, 400, 250, 200]

likes_frequency_distribution = Counter(likes)

print("Frequency distribution of likes among the posts:")
for like, frequency in likes_frequency_distribution.items():
    print(f"Likes: {like}, Frequency: {frequency}")
