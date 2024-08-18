import json
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageSequence
import requests
from io import BytesIO
import random


def check_duplicates(data):
    value_to_ids = {}
    human_to_gpt = {}

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

    duplicate_values = {}
    for human_value, ids_gpts in human_to_gpt.items():
        ids = set()
        gpt_values = set()
        for entry_id, gpt_value in ids_gpts:
            ids.add(entry_id)
            gpt_values.add(gpt_value)

        if len(gpt_values) == 1:
            gpt_value = next(iter(gpt_values))
            if len(ids) > 1:
                duplicate_values[human_value] = ids

    return duplicate_values


def delete_duplicates(data, duplicates):
    unique_data = []
    seen_ids = set()

    for entry in data:
        entry_id = entry["id"]
        conversation = entry["conversations"]
        human_value = None

        for conv in conversation:
            if conv["from"] == "human":
                human_value = conv["value"].strip()

        if human_value in duplicates and entry_id not in seen_ids:
            if entry_id == min(duplicates[human_value]):
                unique_data.append(entry)
            seen_ids.add(entry_id)
        elif human_value not in duplicates:
            unique_data.append(entry)

    return unique_data


def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("Success", f"File has been saved as {filename}")


def shuffle_and_save(data, filename):
    for entry in data:
        original_id = entry["id"]
        new_id = str(random.randint(1000, 9999))
        entry["id"] = new_id

    save_json(data, filename)


def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not file_path:
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load the file: {e}")
        return None


def handle_check_duplicates():
    data = load_data()
    if data is None:
        return
    duplicates = check_duplicates(data)
    if duplicates:
        msg = "\n".join([f"{value}: {len(ids)} duplicates" for value, ids in duplicates.items()])
        messagebox.showinfo("Duplicates Found", msg)
    else:
        messagebox.showinfo("No Duplicates", "No duplicates found.")


def handle_delete_duplicates():
    data = load_data()
    if data is None:
        return
    duplicates = check_duplicates(data)
    if not duplicates:
        messagebox.showinfo("No Duplicates", "No duplicates to delete.")
        return
    unique_data = delete_duplicates(data, duplicates)
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        save_json(unique_data, filename)


def handle_save_json():
    data = load_data()
    if data is None:
        return
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        save_json(data, filename)


def handle_shuffle_save_json():
    data = load_data()
    if data is None:
        return
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        shuffle_and_save(data, filename)


def fetch_gif():
    url = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTlkazZpdHg2ZmVhOGY4NjR0emhvYWk2Y2d4djM5MGMyd2RuOHdseSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4RKhOL0xiBdbgglFi/giphy.gif"
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return img


def animate_gif(label, img, frames, count):
    frame = frames[count]
    count += 1
    if count == len(frames):
        count = 0
    label.configure(image=frame)
    label.after(50, animate_gif, label, img, frames, count)


def create_gui():
    root = tk.Tk()
    root.title("GIF Display GUI")

    img = fetch_gif()
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(img)]

    # Label untuk menampilkan GIF
    gif_label = tk.Label(root)
    gif_label.pack()

    # Memulai animasi GIF
    animate_gif(gif_label, img, frames, 0)

    # Menambahkan judul
    title_label = tk.Label(root, text="Duplicate Data Handler", font=('Helvetica', 18, 'bold'), bg='#80c1ff')
    title_label.pack(pady=20)

    # Tombol-tombol
    frame = tk.Frame(root, bg='#80c1ff')
    frame.pack(pady=10)

    tk.Button(frame, text="Check Duplicates", font=('Helvetica', 14), command=handle_check_duplicates).pack(fill="x",
                                                                                                            pady=5)
    tk.Button(frame, text="Delete Duplicates", font=('Helvetica', 14), command=handle_delete_duplicates).pack(fill="x",
                                                                                                              pady=5)
    tk.Button(frame, text="Save Dataset as JSON", font=('Helvetica', 14), command=handle_save_json).pack(fill="x",
                                                                                                         pady=5)
    tk.Button(frame, text="Shuffle and Save as JSON", font=('Helvetica', 14), command=handle_shuffle_save_json).pack(
        fill="x", pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
