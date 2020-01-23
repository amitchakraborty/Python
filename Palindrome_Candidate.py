def f_cnt_odd(plst_unique, plst_full):
    #Get count of character's odd times and even times appearence
    veven = vodd = 0;
    for ch in plst_unique:
        if plst_full.count(ch) % 2 == 1:
            vodd+=1
    return vodd

def f_detect_palindrome(pstr):
    #Detect input string can be palindrome or not
    vlst_str = list(pstr)
    vlst_str_unique = list(set(vlst_str))
    vodd = f_cnt_odd(vlst_str_unique, vlst_str)
    print(vodd)
    if vodd <= 1:
        return "Can be Palindrome"
    else:
        return "Can't be Palindrome"

print(f_detect_palindrome("never odd or even"));