

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

def getNumberInput(num_list=[]):
    e = False
    print('If you wish to exit please type exit')
    while not e:
        num = input('Please enter a number or exit: ')
        if num == 'exit':
            e = True
            break
        elif isInt(num):
            num_list.append(int(num))
        else:
            print('You did not input a number!!')
            return getNumberInput(num_list)
    return num_list

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
    return top/len(l)

def compareListSum(l1, l2):
    sl1 = sumList(l1)
    sl2 = sumList(l2)
    return sl1 == sl2

def commonNums(l1, l2):
    common_nums = []
    print(l1, l2)
    for num1 in l1:
        for num2 in l2:
            if num1 == num2:
                print(num1, num2)
                common_nums.append(num1)
    return remove_duplicates(common_nums)

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
    
    print(sumList(num_input1))
    print(avgList(num_input1))
    print(compareListSum(num_input1, num_input2))
    print(commonNums(num_input1, num_input2))
if __name__ == "__main__":
    main()
