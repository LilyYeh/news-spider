from datetime import datetime

def time_format(time_str):
    formats = [
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M",
        "%m/%d %H:%M",   # 補今年
        "%H:%M"          # 補今天
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(time_str, fmt)
            if fmt == "%m/%d %H:%M":
                dt = dt.replace(year=datetime.now().year)
            elif fmt == "%H:%M":
                now = datetime.now()
                dt = dt.replace(year=now.year, month=now.month, day=now.day)
            return dt.strftime("%Y/%m/%d %H:%M")
        except ValueError:
            continue

    return time_str