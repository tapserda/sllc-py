class Node(object):
    def __init__(self, data, nobuk):
        self.head = None
        self.data = data
        self.nobuk = nobuk


class sllc:
    def __init__(self):
        self.head = None

    def prepend(self, data, nobuk):
        newno = Node(data, nobuk)
        cur = self.head
        newno.next = self.head

        if not self.head:
            newno.next = newno
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newno
        self.head = newno

    def cetak(self):
        cur = self.head

        while cur:
            print(cur.data, cur.nobuk)
            cur = cur.next
            if cur == self.head:
                break

    def edit(self):
        cur = self.head
        buk = input("Nomor buku yang ingin di edit : ")
        while cur.nobuk != buk:
            cur = cur.next
        nambuk = input("Ketik nama buku baru update : ")
        cur.data = nambuk
        print(cur.data)

    def menu(self):
        slect = input("pilih menu\n3list\n2edit\n1tambah\n4keluar")
        if slect == "1":
            namru = input("nama buku baru : ")
            nomru = input("nomor buku baru : ")
            x.prepend(namru, nomru)
            x.menu()
        elif slect == "2":
            x.edit()
            x.menu()
        elif slect == "3":
            x.cetak()
            x.menu()
        elif slect == "4":
            print("okey")


x = sllc()
x.prepend("yeyeye", "102")
x.prepend("ttuueueue", 101)
x.prepend("newbuee", "100")
x.menu()