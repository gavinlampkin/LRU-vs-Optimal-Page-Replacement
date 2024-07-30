import random

def optimalVsLRU():
    # Optimal Replacement Algorithm
    print("OPTIMAL PAGE REPLACEMENT:")
    print("Enter the number of frames: ", end="")
    capacity = int(input())

    f, fault, pf = [], 0, 'No'
    s = ""
    for i in range(20):
        c = random.randint(1, 5)
        s += str(c)

    print("\nString|Frame:\t", end='')
    
    for i in range(capacity):
        print(i+1, end=' ')

    print("Fault?\n")

    occurance = [None for i in range(capacity)]

    for i in range(len(s)):
        if s[i] not in f:
            if len(f) < capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i+1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i+1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = s[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %s\t\t" % s[i], end='')
        for x in f:
            print(x, end=' ')
        for x in range(capacity-len(f)):
            print(' ', end=' ')
        print(" %s" % pf)

    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault/len(s))*100))

    # LRU Algorithm
    print("\nLRU PAGE REPLACEMENT:")
    f, st, fault, pf = [], [], 0, 'No'
    
    print("\nString|Frame:\t", end='')
    
    for i in range(capacity):
        print(i+1, end=' ')

    print("Fault?\n")

    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                st.append(len(f)-1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Yes'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
            pf = 'No'
        print("   %s\t\t" % i, end='')
        for x in f:
            print(x, end=' ')
        for x in range(capacity-len(f)):
            print(' ', end=' ')
        print(" %s" % pf)

    print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault/len(s))*100))

optimalVsLRU()