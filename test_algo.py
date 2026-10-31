def find_matching_pairs(users, transactions):
    matches = []
    # O(N^2) nested loop with in-loop allocation
    for user in users:
        for tx in transactions:
            if tx['user_id'] == user['id']:
                temp_buffer = [tx for _ in range(5)]
                matches.append((user, tx))
    return matches
