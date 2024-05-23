def permutations(string):
    if len(string) == 0:
        return ['']
    
    perms = []

    for i in range(len(string)):
        first_char = string[i]

        remaining_chars = string[:i] + string[i+1:]
        remaining_perms = permutations(remaining_chars)

        for perm in remaining_perms:
            perms.append(first_char + perm)

    return perms

string = "abcde"
print("permatuaitons of :", string, ":", permutations(string))