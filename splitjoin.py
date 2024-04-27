# def split_and_join(line):
#     line=line.split()
#     line="-".join(line)
#     return line

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

l=(input().split())
l=(l[::-1])
l=" ".join(l)
print(l)
