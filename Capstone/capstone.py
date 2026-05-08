# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Capstone Project: Social Network Explorer (SNE)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

import collections

class SocialNetwork:
    def __init__(self):
        # Experiment 26: Hashing for Profile Storage
        self.profiles = {}  # Stores {username: {"bio": str, "interests": set}}
        # Experiment 23: Adjacency List for Graph Representation
        self.adj_list = collections.defaultdict(set)

    # --- Profile Operations ---
    def add_user(self, username, bio, interests):
        self.profiles[username] = {"bio": bio, "interests": set(interests)}
        if username not in self.adj_list:
            self.adj_list[username] = set()
        print(f"[System] Profile created for {username}")

    def update_profile(self, username, bio=None, interests=None):
        if username in self.profiles:
            if bio: self.profiles[username]["bio"] = bio
            if interests: self.profiles[username]["interests"] = set(interests)
            print(f"[System] Updated {username}'s profile.")
        else:
            print("[Error] User not found.")

    # --- Graph Operations ---
    def add_friendship(self, u, v):
        if u in self.profiles and v in self.profiles:
            self.adj_list[u].add(v)
            self.adj_list[v].add(u)
            print(f"[System] {u} and {v} are now friends.")

    def remove_friendship(self, u, v):
        if v in self.adj_list[u]: self.adj_list[u].remove(v)
        if u in self.adj_list[v]: self.adj_list[v].remove(u)
        print(f"[System] Friendship between {u} and {v} removed.")

    # --- Discovery (Experiment 24: BFS) ---
    def shortest_path(self, start, target):
        """Finds degrees of separation using BFS"""
        if start not in self.adj_list or target not in self.adj_list:
            return None
        
        queue = collections.deque([(start, [start])])
        visited = {start}

        while queue:
            current, path = queue.popleft()
            if current == target:
                return path
            
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    # --- Exploration (Experiment 25: DFS) ---
    def explore_friends(self, start, depth):
        """Finds friends-of-friends up to depth 'd' using DFS logic"""
        discovered = set()
        
        def dfs(user, current_depth):
            if current_depth > depth:
                return
            discovered.add(user)
            for neighbor in self.adj_list[user]:
                if neighbor not in discovered:
                    dfs(neighbor, current_depth + 1)
        
        dfs(start, 0)
        discovered.remove(start) # Don't suggest self
        return discovered

    # --- Recommendation (Experiment 19: Sorting/Benchmarking Logic) ---
    def recommend_friends(self, user):
        """Rank non-friends by common interests"""
        if user not in self.profiles: return []
        
        user_interests = self.profiles[user]["interests"]
        suggestions = []
        
        for potential in self.profiles:
            if potential != user and potential not in self.adj_list[user]:
                common = user_interests.intersection(self.profiles[potential]["interests"])
                if common:
                    suggestions.append((potential, len(common)))
        
        # Sort by most common interests (Descending)
        suggestions.sort(key=lambda x: x[1], reverse=True)
        return suggestions

# --- CLI Implementation & Demo Checklist ---
def main():
    sne = SocialNetwork()

    # 1. Add 6-8 Users
    users = [
        ("Anveshna", "CS Student", ["Python", "React", "AI"]),
        ("Deepak_Sir", "Faculty", ["Data Structures", "Algorithms", "Python"]),
        ("Rahul", "Web Dev", ["React", "JavaScript", "HTML"]),
        ("Sneha", "Data Scientist", ["Python", "AI", "Math"]),
        ("Amit", "Backend Dev", ["Python", "SQL", "Algorithms"]),
        ("Priya", "UI Designer", ["Figma", "HTML", "React"])
    ]
    for u, b, i in users:
        sne.add_user(u, b, i)

    # 2. Update Profiles
    sne.update_profile("Anveshna", interests=["Python", "React", "AI", "Cloud"])

    # 3. Create Connections (8-12)
    connections = [
        ("Anveshna", "Deepak_Sir"), ("Anveshna", "Rahul"), ("Rahul", "Priya"),
        ("Deepak_Sir", "Amit"), ("Amit", "Sneha"), ("Sneha", "Anveshna"),
        ("Priya", "Rahul"), ("Amit", "Deepak_Sir")
    ]
    for u1, u2 in connections:
        sne.add_friendship(u1, u2)

    # 4. Remove a connection
    sne.remove_friendship("Anveshna", "Sneha")

    print("\n--- BFS: Shortest Path (Degrees of Separation) ---")
    path = sne.shortest_path("Anveshna", "Amit")
    print(f"Path from Anveshna to Amit: {' -> '.join(path) if path else 'No Path'}")

    print("\n--- DFS: Discovery (Depth 2) ---")
    discovered = sne.explore_friends("Anveshna", 2)
    print(f"Users discovered within 2 steps of Anveshna: {discovered}")

    print("\n--- Recommendations (Sorted by Common Interests) ---")
    recs = sne.recommend_friends("Anveshna")
    for name, score in recs:
        print(f"Suggesting {name} (Common Interests: {score})")

if __name__ == "__main__":
    main()

# <===================== CODE ENDS ============================>