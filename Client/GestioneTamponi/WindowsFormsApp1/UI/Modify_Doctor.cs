using GestioneTamponi.Class;
using System;
using System.Windows.Forms;

namespace GestioneTamponi
{
    public partial class Modify_Doctor : Form
    {

        MedicalCenterview view;
        medical mc_logged;
        doctor mc_d;
        public Modify_Doctor(doctor d, medical mcLogged, MedicalCenterview view)
        {
            this.view = view;
            mc_d = d;
            this.mc_logged = mcLogged;
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            doctor nd = new doctor(textBox2.Text, textBox4.Text, mc_d.CF, textBox3.Text, textBox6.Text);
            string response = mc_logged.UpdateDoctor(nd);
            Console.WriteLine(nd.toString());
            switch (response)
            {
                case "0":
                    MessageBox.Show("Modificato");
                    this.view.DoctorLoad();
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

        private void Modify_Doctor_Load(object sender, EventArgs e)
        {
            textBox2.Text = mc_d.name;
            textBox4.Text = mc_d.surname;
            textBox3.Text = mc_d.phone;
            textBox6.Text = mc_d.mail;
        }

    }
}
