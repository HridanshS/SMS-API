def split_csv(file_name):
    ip_fd = open(file_name, 'r')
    writer = open('file_name_write.txt', 'w')
    values = ip_fd.readlines()
    for val in values:
        if val:
            writer.write(f"\'{val}\', ") #print(val.split(","))
    ip_fd.close()
    writer.close()

if __name__ == "__main__":
    split_csv('file_name.txt')

#Use readlines and you will get a list with all the names
