import side
print("Tugas modul 4 kelompok 42")
print("Alif Nabil Musyaffa")
print("Syekh Seif Izzul Khaq\n")
tkt = side.Confirm()

loop = True
while loop:
	def menu() :
		print("\n========================================")
		print("SELAMAT DATANG DI LAYANAN E-TICKET KONSER")
		print("==========================================")
		print("1. Sheila on 7")
		print("2. Hindia")
		print("3. Naif")
		print("4. Pamungkas")
		print("5. Exit")
		print("\n========================================")
		
	def pesan():
		jmlh_tiket = int(input("Masukan jumlah tiket : "))
		num_array = list()
		num = input("Berapa orang yang ingin memesan tiket ? : ")
		print ("Masukan nama Pemesan : ")
		for i in range (int(num)):
			i += 1
			n = input("orang ke {} :".format(i))
			num_array.append(str(n)) 
		total_tiket = jmlh_tiket*harga

		tkt.konfirmasi()

		choice = int(input("Pilih 1 untuk lanjut untuk mencetak tiket [1/2] :"))
		if (choice == 1):
			print("\n--------------------------------------------")
			print("Anda telah berhasil melakukan pembelian tiket ")
			print("----------------E - TICKET -------------------")
			print ("Nama Pemesan :".format(len(num_array)))
			for a in num_array:
				print (("- {}").format(a))
				print("Total Harga","Rp.",(total_tiket))
				break
		else :
			pesan()

	menu()
	tiket = int(input("Masukan Pilihan [1-5] : "))
		
	if ((tiket) == 1):
		print("\n-------------------------------------------------------")
		print("\nKode\tVarian\tHarga")
		print("Tiket\tTiket\tTiket")
		print("\n-------------------------------------------------------")
		print("\n101.  Silver\tRp.300.000")
		print("\n102.  Gold\tRp.700.000")
		print("\n103.  Platinum\tRp.1.000.000")
		print("\n-------------------------------------------------------")
		no_tiket = int(input("Masukan kode tiket : "))
		
		if ((no_tiket) == 101):
			harga = 300000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
				
		elif ((no_tiket) == 102):
			harga = 700000
			print("")
			print("---------------------------------")
			print("anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 103):
			harga = 1000000
			print("")
			print("---------------------------------")
			print("anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		else :
			print("kode tiket tidak ada dalam daftar")
			break

	elif ((tiket) == 2):
		print("\n----------------------------------------------------------")
		print("\nKode\tVarian\tHarga")
		print("Tiket\tTiket\tTiket")
		print("\n----------------------------------------------------------")
		print("\n201. Silver\tRp.200.000")
		print("\n202. Gold\tRp.350.000")
		print("\n203. Platinum\tRp.600.000")
		print("\n----------------------------------------------------------")
		no_tiket = int(input("Masukan kode tiket :"))
		
		if ((no_tiket) == 201):
			harga = 200000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 202):
			harga = 350000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 203):
			harga = 600000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()

		else:
			print("Kode tiket tidak ada dalam daftar")
			break
			
	elif ((tiket) == 3):
		print("\n-------------------------------------------------------")
		print("\nKode\tVarian\tHarga")
		print("Tiket\tTiket\tTiket")
		print("\n-------------------------------------------------------")
		print("\n301. Silver\tRp.300.000")
		print("\n302. Gold\tRp.600.000")
		print("\n303. Platinum\tRp.1.000.000")
		print("\n-------------------------------------------------------")
		no_tiket = int(input("Masukan kode tiket :"))
		
		if ((no_tiket) == 301):
			harga = 300000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 302):
			harga = 600000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 303):
			harga = 1000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		else :
			print("Kode tiket tidak ada dalam daftar")

		break	
			
	elif ((tiket) == 4):
		print("\n-------------------------------------------------------")
		print("Kode\tVarian\tHarga")
		print("Tiket\tTiket\tTiket")
		print("\n-------------------------------------------------------")
		print("\n401.   Silver  \tRp.200.000")
		print("\n402.   Gold  \tRp.350.000")
		print("\n403.   Platinum \tRp.500.000")
		print("\n-------------------------------------------------------")
		no_tiket = int(input("Masukan kode tiket :"))
		
		if ((no_tiket) == 401):
			harga = 200000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 402):
			harga = 350000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		elif ((no_tiket) == 403):
			harga = 500000
			print("")
			print("---------------------------------")
			print("Anda memilih kode tiket",+int(no_tiket))
			print("---------------------------------")
			pesan()
			
		else :
			print("Kode tiket tidak ada dalam daftar")

		break	
			
	elif ((tiket) == 5):
		exit()
	else :
		print("***Pilihan tidak ada dalam daftar***")