

def getNameInput():
    name_list = []
    e = False
    print('If you wish to exit please type exit')
    while not e:
        name=input('Enter a name or exit: ')
        if name == 'exit':
            e = True
            break
        else:
            name_list.append(name)
    return name_list

def isInt(s):
    negative = True if s[:1] == '-' else False
    if negative:
        if len(s) == 1:
            return False
        s = s[1:]
        for c in s:
            if not(c>='0' and c<='9'):
                return False
        return True
    else:
        for c in s:
            if not(c>='0' and c<='9'):
                return False
        return True

def getNumberInput():
    print('Please enter a list of numbers for your first list. Each number should be seperated by a comma')
    user_in = input('Numbers: ')
    uia = user_in.split(',')
    nums = []
    for l in uia:
        n = l.strip()
        if not len(n) == 0:
            if isInt(n):
                nums.append(int(n))
    return nums

def letterFrequency(l):
    all_freq = {}
    for s in l:
        for iw in s:
            i = iw.lower()
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    return all_freq

def compareListLength(l1, l2):
    ll1 = len(l1)
    ll2 = len(l2)
    return ll1 == ll2

def sumList(l):
    return sum(l)

def avgList(l):
    top = sumList(l)
    if len(l) > 0:
        return top/len(l)
    return None

def compareListSum(l1, l2):
    sl1 = sumList(l1)
    sl2 = sumList(l2)
    return sl1 != sl2

def commonNums(l1, l2):
    common_nums = []
    for num1 in l1:
        for num2 in l2:
            if num1 == num2 and num1 not in common_nums:
                common_nums.append(num1)
    return common_nums

def remove_duplicates(l):
    flist = []
    for n in l:
        if n not in flist:
            flist.append(n)
    return flist

def main():
    ninput1 = getNameInput()
    print(letterFrequency(ninput1))

    num_input1 = getNumberInput()
    num_input2 = getNumberInput()

    print('The lists are the same length: ', len(num_input1) == len(num_input2))

    print('Sum of List 1: ', sumList(num_input1))
    print('Average of List 1: ', avgList(num_input1))
    
    print('Sum of List 2: ', sumList(num_input2))
    print('Average of List 2: ', avgList(num_input2))
    
    print('Sum\'s of List 1 and 2 Are Different: ', compareListSum(num_input1, num_input2))
    print('Common Numbers between the two lists: ', commonNums(num_input1, num_input2))
if __name__ == "__main__":
    main()
