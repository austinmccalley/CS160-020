user_in = int(input("Please enter the decimal number which you would like to convert to binary: "));

curr_num = user_in

bin_num = []


while True:
    if curr_num == 0:
        break
    quotient = curr_num // 2
    bin_num.append(curr_num % 2)

    curr_num = quotient


bin_num.reverse()
bin_num = ''.join(str(e) for e in bin_num)
print("We got the binary number %s" % str(bin_num))
#print("What binary number should be %s" % str(bin(user_in))[2:])


print("\n\n")

user_in = int(input("Please enter the binary number which you would like to convert to decimal: "));
#print(user_in)
bin_arr = list(str(user_in))
bin_arr.reverse()
#print(bin_arr)


bin_len = len(bin_arr)


curr_num = user_in

decm_num = []

for x in range(0, bin_len):
    #print(bin_arr[x])
    #print(x)
    #print(str(int(bin_arr[x])*2**x))
    decm_num.append(int(bin_arr[x])*2**x)
    #print('\n')

#print(decm_num)
decm_total = sum(decm_num)
print("We got the decimal number: " + str(decm_total))

