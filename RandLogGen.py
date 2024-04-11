import random

def generate_ipv4():
    ip_address = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    return ip_address


# Генерация случайного времени в формате yyyy-MM-dd HH:mm:ss
def generate_date_time():
    year = random.randint(2009, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Февраль не всегда 29 дней
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    date_time = f'{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
    return date_time

f = open('log.txt', 'w')
# Генерация адреса и времени
for i in range(1000000):
    random_ipv4 = generate_ipv4()
    random_date_time = generate_date_time()

    f.write(random_ipv4+":"+random_date_time+"\n")
f.close()

