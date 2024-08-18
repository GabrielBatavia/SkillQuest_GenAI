import json


def check_duplicates(data):
    value_to_ids = {}
    human_to_gpt = {}

    # Mengumpulkan semua value dan ID dari seluruh percakapan
    for entry in data:
        entry_id = entry["id"]
        conversation = entry["conversations"]
        human_value = None
        gpt_value = None

        for conv in conversation:
            value = conv["value"].strip()
            if conv["from"] == "human":
                human_value = value
            elif conv["from"] == "gpt":
                gpt_value = value

        if human_value:
            if human_value in human_to_gpt:
                human_to_gpt[human_value].append((entry_id, gpt_value))
            else:
                human_to_gpt[human_value] = [(entry_id, gpt_value)]

        if gpt_value:
            if gpt_value in value_to_ids:
                value_to_ids[gpt_value].append(entry_id)
            else:
                value_to_ids[gpt_value] = [entry_id]

    # Menyaring nilai yang muncul lebih dari sekali
    duplicate_values = {}
    for human_value, ids_gpts in human_to_gpt.items():
        ids = set()
        gpt_values = set()
        for entry_id, gpt_value in ids_gpts:
            ids.add(entry_id)
            gpt_values.add(gpt_value)

        # Cek jika nilai gpt unik
        if len(gpt_values) == 1:
            gpt_value = next(iter(gpt_values))
            if len(ids) > 1:
                duplicate_values[human_value] = ids

    return duplicate_values


def preview_value(value, max_words=7):
    words = value.split()
    if len(words) > max_words:
        return ' '.join(words[:max_words]) + '...'
    return value


def print_table(duplicates):
    print("-" * 80)
    print(f"{'Value':<60} {'IDs':<15}")
    print("-" * 80)

    for value, ids in duplicates.items():
        preview = preview_value(value)
        ids_str = ', '.join(ids)
        print(f"{preview:<60} {ids_str:<15}")

    print("-" * 80)
    print(f"Total Duplicates Found: {len(duplicates)}")
    print("-" * 80)


def main(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        duplicates = check_duplicates(data)

        if duplicates:
            print_table(duplicates)
        else:
            print("No duplicates found.")
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")

if __name__ == "__main__":
    file_path = "./output3.json"  # Ganti dengan path ke file JSON Anda
    main(file_path)
