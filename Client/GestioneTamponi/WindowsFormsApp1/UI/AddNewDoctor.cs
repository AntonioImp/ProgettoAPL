using GestioneTamponi.Class;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace GestioneTamponi
{
    public partial class AddNewDoctor : Form
    {

        medical mc_logged;
        MedicalCenterview mc_view;
 
        public AddNewDoctor(medical mc, MedicalCenterview mc_view)
        {
            this.mc_view = mc_view;
            mc_logged = mc;
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            List<string> list = ListWeek.CheckedItems.OfType<string>().ToList();
            doctor doc = new doctor(textBox2.Text, textBox4.Text, textBox1.Text, textBox3.Text, textBox6.Text, ListWeek.CheckedItems.OfType<string>().ToList());//, ListWeek.CheckedItems.Cast<List>().Select(item => item.Text).ToList());
            string response = mc_logged.NewDoctor(doc);
            switch (response)
            {
                case "0":
                    MessageBox.Show("Dottore registrato nel sistema");
                    mc_view.DoctorLoad();
                    break;
                case "-2":
                    MessageBox.Show("Autenticazione fallita");
                    break;
                case "-1":
                    MessageBox.Show("Errore durante l'inserimento");
                    break;
                case "1":
                    MessageBox.Show("Dottore già esistente in db, inserita affiliazione al medical");
                    break;
            }
            new MedicalCenterview(mc_logged).Show();
            this.Hide();
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            this.Hide();
            mc_view.Show();

        }

    }
}
