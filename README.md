<img width="134" height="202" alt="image" src="https://github.com/user-attachments/assets/ab6cd9ef-0998-44fa-a0e0-f840ad7a1324" />

# Tictactoe_cli (Command Line Interface)
Permainan Tictactoe sederhana menggunakan python dan berbasis command line interface, untuk tugas pengenalan pemrograman

## Fitur-fitur

- Command line menu
- Lightweight
- Prompt untuk bermain lagi jika permainan sebelumnya sudah selesai
- Built-in rulebook sederhana dalam menu sebelum bermain

## Installasi dan penjalanan program

not my part

## Cara bermain dalam program
- Saat program pertama kali dijalankan, Anda akan melihat menu utama seperti ini :
  Welcome to TictacToe
  Insert the number corresponding to the action:
  1 - Play
  2 - Ruleset
  3 - Exit
- Untuk bermain, masukkan '1' dan tekan Enter.
- Program akan membersihkan layar, menampilkan papan, dan menentukan giliran pemain.
  =============
  -------------
  | 1 | 2 | 3 |
  -------------
  | 4 | 5 | 6 |
  -------------
  | 7 | 8 | 9 |
  -------------
  =============
- *Pemain* *1* menggunakan simbol *O.*
- *Pemain* *2* menggunakan simbol *X.*
- Secara default, *Player* *1* *(O)* akan bermain pertama.
- Di bawah papan, program akan menunjukkan giliran pemain saat ini:
  Current player's turn = Player 1 (O)
- Program akan meminta masukan:
  insert number of the space which you want to fill:
- Anda harus memasukkan angka dari *1* *hingga* *9* yang sesuai dengan kotak yang ingin Anda tempatkan simbol ( O atau X).
- Jika Anda memasukkan angka yang sudah terisi oleh simbol lain, atau jika Anda memasukan *angka yang tidak vailid*(bukan 1-9), program akan menampilkan pesan keasalahan dan meminta Anda untuk memasukkan input lagi.
- Setelah masukan valid, giliran pemain akan bermain secara bergantian.
- Program akan mengulang proses sampai ada pemenang atau seri.
- Jika salah satu pemain berhasil mendapatkan tiga simbol secara horizontal, vertikal atau diagonal, program akan mendeklarasikan pemenang,
- Jika semua kotak terisi dan tidak ada pemenang, program akan mendeklarasikan seri.
- Setelah permainan berakhir, Anda akan ditanya apakah ingin bermain lagi ('y' untuk ya, 'n' untuk kembali ke menu).
  
### Penjelasan fungsi dalam program
- `clear_output()`: membersihkan command line setiap kali dijalankan.
- `tictactoe_visual()`: Memunculkan display visual (papan bermain) tictactoe saat dijalankan, setiap angka merupakan posisi setiap kotak yang masih belum diambil.
- `tictactoe_player_control()`: mengatur siapa yang akan bermain pada giliran tertentu. ketika dijalankan, jika sebelumnya merupakan player 1 maka akan diubah menjadi player 2, dan sebaliknya. jika pada awal permainan (belum ada player sebelum), maka akan set giliran ke player1
- `tictactoe_win_detection()`: fungsi ini melihat apakah sudah ada salah satu pemain yang membentuk suatu garis menggunakan 3 simbol. jika sudah, maka fungsi akan return nilai player yang membentuk garis tersebut. jika semua kotak sudah terisi namun tidak ada player yang membentuk garis menggunakan 3 simbol, maka fungsi akan return "DRAW". jika tidak ada pemain yang membentuk garis menggunakan 3 simbol namun masih ada kotak yang belum terisi, maka program akan return "ONGOING" untuk memberitahu sistem untuk lanjutkan permainan.
- `tictactoe_start()`: fungsi ini akan memulai permainan. ketika dijalankan, fungsi akan membersihkan (mereset) semua variabel penting, lalu menjalankan permainan menggunakan while-loop.
