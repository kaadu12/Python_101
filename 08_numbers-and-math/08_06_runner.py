# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

miles = 10
seconds = 1830
km = 1.6

total_km = miles * km
hours = seconds / 60 / 60
print(hours)
kph = total_km / hours
print(kph)