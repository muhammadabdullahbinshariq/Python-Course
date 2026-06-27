file = open('Folder.txt', 'r')

print(f"This file is about {file.read(10)}")

file.seek(0)
lines = file.readlines()
print(f"\nThe file has {len(lines)} lines")

print("\nThis file consists of:")
file.seek(0)
for i in lines:
    cleaned_line = i.strip()
    if cleaned_line:
        print(cleaned_line)
        print("")

print("\nNotes starting with Pakistan :")
for i in lines:
    if i.startswith("Pakistan"):
        print(i.strip())

file.close()