def main():
    k = 52.4
    c = 0.12
    p = 0.321
    
    init_temp = 0.0
    left_temp = 0.0
    right_temp = 100

    length = 10.0
    sections = 10

    time_int = 50
    deltat = 0.000335

    deltax = length / sections

    const = (k*deltat)/(deltax**2 * c * p)

    u = []

    uold = [init_temp]*sections
    uold[0] = left_temp
    uold[sections-1] = right_temp

    unew = [init_temp]*sections
    unew[0] = left_temp
    unew[sections-1] = right_temp

    for i in range(time_int):
        for x in range(1, sections - 1):
            top = (uold[x+1]-2*uold[x]+uold[x-1])
            unew[x]=const*top + uold[x]
        u.append(unew)
        print(u[i])
        uold = u[-1]




main()
