number_of_snowballs = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0
best_value = 0
for i in range(number_of_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())
    snowball_value = weight / time_to_target
    snowball_quality = int(snowball_value ** quality)
    if best_quality < snowball_quality:
        best_weight = weight
        best_time = time_to_target
        best_quality = quality
        best_value = snowball_quality
print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")
