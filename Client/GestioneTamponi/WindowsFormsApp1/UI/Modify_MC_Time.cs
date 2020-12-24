using GestioneTamponi.Class;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GestioneTamponi.UI
{
    public partial class Modify_MC_Time : Form
    {
        medical medical;
        MedicalCenterview view;
        public Modify_MC_Time(medical m, MedicalCenterview view)
        {
            InitializeComponent();
            medical = m;
            this.view = view;
        }

        private void Modify_MC_Time_Load(object sender, EventArgs e)
        {
            start_timeInput.Text = medical.start_time;
            end_timeInput.Text = medical.end_time;
            default_timeInput.Text = medical.default_interval;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string response = medical.SetMedicalTime(start_timeInput.Text, end_timeInput.Text, default_timeInput.Text);
            switch (response)
            {
                case "0":
                    MessageBox.Show("Modifica effettuata");
                    this.Hide();
                    break;
                case "-1":
                    MessageBox.Show("Errore modifica");
                    break;
                case "-2":
                    MessageBox.Show("Autenticazione fallita");
                    break;
                case "-3":
                    MessageBox.Show("Formato orario errato");
                    break;
            }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            this.Hide();
        }
    }
}
