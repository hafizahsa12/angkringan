from tkinter import * 
from tkinter import messagebox 
import mysql.connector 
from tkinter import ttk 

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
 
class Data_angkringan(Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("Registrasi Data angkringan") 
        self.geometry("850x600") 
 
        # Koneksi ke database 
        self.db = mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="", 
            database="angkringan" 
        )
 # Membuat kursor 
        self.cursor = self.db.cursor() 
 
        # Membuat dan menampilkan GUI 
        self.tampilan_gui() 
 
    def tampilan_gui(self): 
 
        Label(self, text="no_antri").grid(row=0, column=0, padx=10, pady=10) 
        self.no_antri_entry = Entry(self, width=50) 
        self.no_antri_entry.grid(row=0, column=1, padx=10, pady=10) 
 
        Label(self, text="nama").grid(row=1, column=0, padx=10, pady=10) 
        self.nama_entry = Entry(self, width=50) 
        self.nama_entry.grid(row=1, column=1, padx=10, pady=10) 
 
        Label(self, text="menu").grid(row=2, column=0, padx=10, pady=10) 
        self.menu_entry = Entry(self, width=50) 
        self.menu_entry.grid(row=2, column=1, padx=10, pady=10) 
 
        Label(self, text="harga_total").grid(row=3, column=0, padx=10, pady=10) 
        self.harga_total_entry = Text(self, width=37, height=5) 
        self.harga_total_entry.grid(row=3, column=1, padx=10, pady=10) 
 
        Button(self, text="Simpan Data",  
               command=self.simpan_data).grid(row=4, column=0, columnspan=2, pady=10) 
         
        # Menambahkan Treeview 
        self.tree = ttk.Treeview(self, columns=("no_antri", "nama", "menu", "harga_total"), show="headings") 
        self.tree.heading("no_antri", text="no_antri") 
        self.tree.heading("nama", text="nama") 
        self.tree.heading("menu", text="menu") 
        self.tree.heading("harga_total", text="harga_total") 
        self.tree.grid(row=5, column=0, columnspan=6, pady=10, padx=10) 
 
        # Menambahkan tombol refresh data 
        Button(self, text="Refresh Data", command=self.tampilkan_data).grid(row=6, column=0, columnspan=2, pady=10, padx=10) 
 
        # Menambahkan tombol delete data 
        Button(self, text="Delete Data", command=self.hapus_data).grid(row=6, column=1, columnspan=2, pady=10, padx=10) 
 
        # Menambahkan tombol update data 
        Button(self, text="Update Data", command=self.update_data).grid(row=6, column=2, columnspan=2, pady=10, padx=10)
        # Menambahkan tombol print data 
        Button(self, text="Print Data", command=self.cetak_ke_pdf).grid(row=6, column=3, columnspan=2, pady=10, padx=10)
        self.tampilkan_data() 
        
 
    def simpan_data(self): 
        no_antri = self.no_antri_entry.get() 
        nama= self.nama_entry.get() 
        menu = self.menu_entry.get() 
        harga_total = self.harga_total_entry.get("1.0", END) 
 
        query = "INSERT INTO angkringan (no_antri, nama, menu, harga_total) VALUES (%s, %s, %s, %s)" 
        values = (no_antri, nama, menu, harga_total) 
 
        try: 
            self.cursor.execute(query, values) 
            self.db.commit() 
            messagebox.showinfo("Sukses", "Data berhasil disimpan!") 
        except Exception as e: 
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}") 
 
        self.no_antri_entry.delete(0, END) 
        self.nama_entry.delete(0, END) 
        self.menu_entry.delete(0, END) 
        self.harga_total_entry.delete("1.0", END) 
     
    def tampilkan_data(self): 
        # Hapus data pada treeview 
        for row in self.tree.get_children(): 
            self.tree.delete(row) 
 
        # Ambil data dari database 
        self.cursor.execute("SELECT * FROM angkringan") 
        data = self.cursor.fetchall() 
 
        # Masukkan data ke treeview 
        for row in data: 
            self.tree.insert("", "end", values=row) 
     
    def hapus_data(self): 
        selected_item = self.tree.selection() 
 
        if not selected_item: 
            messagebox.showwarning("Peringatan", "Pilih data yang akan dihapus.") 
            return 
 
        confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?") 
        if confirmation:
         for item in selected_item: 
                data = self.tree.item(item, 'values') 
                no_antri_to_delete = data[0] 
                 
                query = "DELETE FROM angkringan WHERE no_antri = %s" 
                values = (no_antri_to_delete,) 
 
                try: 
                    self.cursor.execute(query, values) 
                    self.db.commit() 
                    messagebox.showinfo("Sukses", "Data berhasil dihapus!") 
                except Exception as e: 
                    messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}") 
 
                    self.tampilkan_data() 
         
    def update_data(self): 
        selected_item = self.tree.selection() 
 
        if not selected_item: 
            messagebox.showwarning("Peringatan", "Pilih data yang akan diupdate.") 
            return 
 
        # Ambil data terpilih dari treeview 
        data = self.tree.item(selected_item[0], 'values') 
 
        # Tampilkan form update dengan data terpilih 
        self.no_antri_entry.insert(0, data[0]) 
        self.nama_entry.insert(0, data[1]) 
        self.menu_entry.insert(0, data[2]) 
        self.harga_total_entry.insert("1.0", data[3]) 
 
        # Menambahkan tombol update di form 
        Button(self, text="Update", command=lambda: 
self.proses_update(data[0])).grid(row=4, column=1, columnspan=2, pady=10) 
 
    def proses_update(self, no_antri_to_update): 
        no_antri = self.no_antri_entry.get() 
        nama = self.nama_entry.get() 
        menu = self.menu_entry.get() 
        harga_total = self.harga_total_entry.get("1.0", END) 
 
        query = "UPDATE angkringan SET no_antri=%s, no_antri=%s, menu=%s, harga_total=%s WHERE no_antri=%s" 
        values = (no_antri, nama, menu, harga_total, no_antri_to_update) 
 
        try: 
            self.cursor.execute(query, values)
            self.db.commit() 
            messagebox.showinfo("Sukses", "Data berhasil diupdate!") 
        except Exception as e: messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}") 

# Bersihkan form setelah update 
        self.no_antri_entry.delete(0, END) 
        self.nama_entry.delete(0, END) 
        self.menu_entry.delete(0, END) 
        self.harga_total_entry.delete("1.0", END) 
# Tampilkan kembali data setelah diupdate 
        self.tampilkan_data() 

    def cetak_ke_pdf(self):
        doc = SimpleDocTemplate("data_angkringan.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
# Membuat data untuk tabel PDF
        data = [["no_antri", "no_antri", "Jurusan", "Alamat"]]

        for row_id in self.tree.get_children():
            row_data = [self.tree.item(row_id, 'values')[0],
                        self.tree.item(row_id, 'values')[1],
                        self.tree.item(row_id, 'values')[2],
                        self.tree.item(row_id, 'values')[3]]

            data.append(row_data)
# Membuat tabel PDF
        table = Table(data)
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

# Menambahkan tabel ke dokumen PDF
        doc.build([table])
        messagebox.showinfo("Sukses", "Data berhasil dicetak ke PDF(data_angkringan.pdf).")

if __name__ == "__main__": 
    app = Data_angkringan() 
    app.mainloop()