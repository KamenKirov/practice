def messages_manager(capacity):
    users = {}

    while True:
        command = input()
        if command == "Statistics":
            break

        parts = command.split("=")
        action = parts[0]

        if action == "Add":
            username = parts[1]
            sent = int(parts[2])
            received = int(parts[3])

            if username not in users:
                users[username] = {"sent": sent, "received": received}

        elif action == "Message":
            sender = parts[1]
            receiver = parts[2]

            if sender in users and receiver in users:
                users[sender]["sent"] += 1
                users[receiver]["received"] += 1

                if users[sender]["sent"] >= capacity:
                    print(f"{sender} reached the capacity!")
                    del users[sender]
                if users[receiver]["received"] >= capacity:
                    print(f"{receiver} reached the capacity!")
                    del users[receiver]

        elif action == "Empty":
            username = parts[1]

            if username == "All":
                users.clear()
            elif username in users:
                del users[username]

    print(f"Users count: {len(users)}")
    sorted_users = sorted(users.items(), key=lambda x: (-x[1]['received'], x[0]))

    for username, info in sorted_users:
        total_messages = info['sent'] + info['received']
        print(f"{username} - {total_messages}")


if __name__ == "__main__":
    capacity = int(input())
    messages_manager(capacity)
