from pathlib import Path


# Розділяємо рядок: дата, час, рівень, повідомлення
def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)

    if len(parts) < 4:
        return {}

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3].strip(),
    }

# Завантаження лог-файлів
def load_logs(file_path: str) -> list:
    logs = []
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        print(f"Error: File hasnt been found at path: {path}")
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
        return logs
    except Exception as ex:
        print(f"Error: {ex}")
        return []

# Фільтрацію за рівнем логування
def filter_logs_by_level(logs: list, level: str) -> list:
    filter_logs = filter(lambda log: log["level"] == level.upper(), logs)
    return list(filter_logs)

# Підрахунок записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

# Вивід результатів
def display_log_counts(counts: dict):
    print(f"\n{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 30)

    for level, count in counts.items():
        count = counts.get(level, 0)
        print(f"{level:<17} | {count:<10}")
