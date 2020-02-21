def hanoi(n, rod_from, rod_middle, rod_to):
    #when n-1 plates are in the final position
    if n==1:
        print("%s placas, desde %s hacia %s"%(n, rod_from, rod_to))
        print("plate 1 from %s to %s "%(rod_from, rod_to))
        return
    else:
        print("%s placas, desde %s hacia %s con la ayuda de %s"%(n, rod_from, rod_to, rod_middle))

    #moving n-1 plates off the largest one to be able to move that
    hanoi(n-1, rod_from, rod_to, rod_middle)
    #moving actual largest one
    print("plate %s from %s to %s "%(n, rod_from, rod_to))
    #placing n-1 plates on the top of the largest one
    hanoi(n-1, rod_middle, rod_from, rod_to)

if __name__ == "__main__":
    hanoi(3, 'a', 'b', 'c')   