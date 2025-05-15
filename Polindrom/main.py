def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            continue
        else:
            return False

    return True

if __name__ == '__main__':
    str1 = 'довод'
    str2 = 'доход'
    str3 = 'завод'
    print(is_palindrome(str1))
    print(is_palindrome(str2))
    print(is_palindrome(str3))