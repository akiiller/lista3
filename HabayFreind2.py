unique_yes_names = set()
unique_no_names = set()
all_yes_registrations = [] # To store (name, original_order) for tie-breaking

registration_order_counter = 0

while True:
    line = input()
    if line == "FIM":
        break

    registration_order_counter += 1
    parts = line.split()
    name = parts[0]
    choice = parts[1]

    if choice == "YES":
        unique_yes_names.add(name)
        all_yes_registrations.append((name, registration_order_counter))
    elif choice == "NO":
        unique_no_names.add(name)

# --- Determine the winner ---
habay_winner_name = ""
max_len = -1
winner_registration_order = float('inf') # Initialize with infinity

for name, order in all_yes_registrations:
    current_len = len(name)
    if current_len > max_len:
        max_len = current_len
        habay_winner_name = name
        winner_registration_order = order
    elif current_len == max_len:
        # Tie-breaker: check original registration order
        if order < winner_registration_order:
            habay_winner_name = name
            winner_registration_order = order

# --- Prepare names for printing ---
sorted_yes_names = sorted(list(unique_yes_names))
sorted_no_names = sorted(list(unique_no_names))

# --- Print output ---

# Print sorted YES names
for name in sorted_yes_names:
    print(name)

# Print sorted NO names
for name in sorted_no_names:
    print(name)

# Print blank line
print()

# Print winner
print("Amigo do Habay:")
print(habay_winner_name)

#esse é o certo porque trata os casos de empate