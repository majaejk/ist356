import beautiful_date as bd
today = bd.BeautifulDate.fromisoformat('2026-09-08')
six_mo = today + 6 * bd.months
print(today)
print(six_mo)

# parse the date like Jan 14, 2024
jan_14_2024 = bd.BeautifulDate.strptime('Jan 14, 2024', '%b %d, %Y')
print(jan_14_2024)
