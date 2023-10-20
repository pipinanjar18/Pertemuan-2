import numpy as np

# Contoh array NumPy
array = np.array([[1,2,3,4], [5,6,7,8]])

# Atribut shape (bentuk)
bentuk = array.shape
print("Bentuk array :", bentuk)
# Outputnya (2,4) karena terdiri dari 2 baris dan 4 kolom


# Atribut ndim (jumlah dimensi)
dimensi = array.ndim
print("Jumlah dimensi array :", dimensi)
# Outputnya 2 karena array 2 dimensi


# Atribut dtype (tipe data)
tipe_data = array.dtype 
print('Tipe data array :', tipe_data)
# Output : int32 karena tipe data elemen bilangan bulat 32-bit


# Atribut nbytes (alokasi memori)
memori = array.nbytes
print("Alokasi memori array :", memori, "byte")
# Output : 32 byte karena total elemen * ukuran tipe data ( 4 * 8 byte)