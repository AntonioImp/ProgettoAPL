using GestioneTamponi.Class;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GestioneTamponi
{
    public partial class Modifica_info_MC : Form
    {
        medical mc_logged;
        MedicalCenterview mc_view;
        public Modifica_info_MC(medical mc, MedicalCenterview view)
        {
            this.mc_logged = mc;
            this.mc_view = view;
            InitializeComponent();
        }

        private void Modifica_info_MC_Load(object sender, EventArgs e)
        {
            textBox1.Text = mc_logged.p_IVA;
            textBox7.Text = mc_logged.mail;
            textBox6.Text = mc_logged.phone;
            textBox3.Text = mc_logged.street;
            textBox2.Text = mc_logged.city;
            textBox4.Text = mc_logged.n_cv;
            textBox5.Text = mc_logged.CAP;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            medical m = mc_logged;
            m.p_IVA = textBox1.Text;
            m.street = textBox3.Text;
            m.city = textBox2.Text;
            m.CAP = textBox5.Text;
            m.n_cv = textBox4.Text;
            m.phone = textBox6.Text;
            m.mail = textBox7.Text;
            string response = mc_logged.Modify(m);
            switch (response)
            {
                case "0":
                    MessageBox.Show("Modifica avvenuta");
                    mc_logged = m;
                    // mc_logged.setInformationMedical(mc_logged.medName, textBox3.Text, textBox7.Text, textBox2.Text, textBox6.Text, textBox4.Text, textBox5.Text);
                    mc_view.Show();
                    this.Hide();
                    break;
                case "-2":
                    MessageBox.Show("Autenticazione fallita");
                    break;
                case "-1":
                    MessageBox.Show("Errore durante la modifica");
                    break;
            }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            mc_view.Show();
            this.Hide();
        }
    }
}
