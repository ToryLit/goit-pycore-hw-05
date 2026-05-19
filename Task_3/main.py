import sys
from logger_logic import load_logs, count_logs_by_level, filter_logs_by_level,display_log_counts


def main():
    if len(sys.argv) < 2:
        print("Error: Path is not available.")
        return

    file_path = sys.argv[1]
    
    logs = load_logs(file_path)
    
    if not logs:
        return

    # Рахуємо статистику
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Перевіряємо наявність другого аргументу (рівень логування)
    if len(sys.argv) > 2:
        level_to_filter = sys.argv[2]
        # Фільтруємо за рівнем
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        
        if filtered_logs:
            print(f"\nDetails for level '{level_to_filter.upper()}':")
            for entry in filtered_logs:
                print(f"{entry['date']} {entry['time']} - {entry['message']}")
        else:
            print(f"\nDetails '{level_to_filter.upper()}' hasnt been found")


if __name__ == "__main__":
    main()