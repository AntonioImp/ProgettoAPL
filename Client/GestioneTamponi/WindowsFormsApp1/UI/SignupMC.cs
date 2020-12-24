using GestioneTamponi.Class;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Net;
using System.Windows.Forms;

namespace GestioneTamponi
{
    public partial class SignupMC : Form
    {
        public SignupMC()
        {
            InitializeComponent();
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            new Login().Show();
            this.Hide();
        }

        private void SignUp_Click(object sender, EventArgs e)
        {

            try
            {
                medical m = new medical();
                string json_data = JsonConvert.SerializeObject(new { pass = Password.Text, p_IVA = P_iva.Text, medical_name = Medical_name.Text, street = Street.Text, mail = Mail.Text, city = City.Text, phone = Phone.Text, n_cv = Int32.Parse(N_cv.Text), CAP = CAP.Text });
                string response = m.Signup(json_data);
                if (response != "-1")
                {
                    new Login().Show();
                    this.Hide();
                }
                else
                {
                    MessageBox.Show("Errore durante la registrazione!");
                }
            }
            catch (FormatException)
            {
                MessageBox.Show("Nc must be an integers");
            }

        }

        private void SignupMC_Load(object sender, EventArgs e)
        {

        }
    }
}
