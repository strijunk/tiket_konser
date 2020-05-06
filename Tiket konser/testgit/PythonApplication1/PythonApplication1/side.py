import Tiket_Konser
class Confirm:
    def konfirmasi(self):
        print("----------K O N F I R M A S I----------")
        print("Mohon cek sekali lagi kevalidan data Anda")
        print("Anda memesan kode tiket :" +int(no_tiket))
        print("Data pemesan :")
        for a in num_array:
            print (("- {}").format(a))