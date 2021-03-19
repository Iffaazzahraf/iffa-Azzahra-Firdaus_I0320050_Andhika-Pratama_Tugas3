

# mulai

list= ['daffa', 'yasmin', 'irna', 'felicia', 'fidely', 'aurora', 'therecia', 'ghina', 'kirana', 'shafa']
print("list 4,6,7:", list[4], list[6], list[7])

print("nama pada list 3,5,9:", list[3], list[5], list[9])
list[3]='ivashka'
list[5]='andreea'
list[9]='luthfiyyah'
print("list 3,5,9 setelah diganti adalah:",list[3], list[5], list[9])



#menambah nama
list.extend(['musdalifah','hero'])
for teman in list:
    print(teman, " teman saya")

print([list]*2)


print("panjang list adalah", len(list))
#selesai


