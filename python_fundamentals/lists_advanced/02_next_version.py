version = input().split(".")
new_version = []
small = int(version[2])
sub = int(version[1])
main = int(version[0])

small += 1

if small > 9:
    small = 0
    sub += 1
    if sub > 9:
        main += 1
        sub = 0

new_version.append(str(main))
new_version.append(str(sub))
new_version.append(str(small))

print('.'.join(new_version))
