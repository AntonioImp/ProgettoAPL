using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.IO;
using Newtonsoft.Json;
using GestioneTamponi.Class;

namespace GestioneTamponi
{
    public partial class SignupUser : Form
    {
        public SignupUser()
        {
            InitializeComponent();
        }

        private void pictureBox2_Click_1(object sender, EventArgs e)
        {
            new Login().Show();
            this.Hide();

        }

        private void SignUp_Click(object sender, EventArgs e)
        {
            try
            {
                user u = new user();
                string json_data = JsonConvert.SerializeObject(new { pass = Password.Text, name = Name.Text, surname = Surname.Text, CF = CF.Text, street = Street.Text, mail = Mail.Text, city = City.Text, phone = Phone.Text, age = Int32.Parse(Age.Text), n_cv = Int32.Parse(N_cv.Text), CAP = CAP.Text });
                string response = u.Signup(json_data);
                if (response == "0")
                {
                    new Login().Show();
                    this.Hide();
                }
                else
                {
                    MessageBox.Show("Errore durante la registrazione!");
                }
            }
            catch (FormatException) {
                MessageBox.Show("Nc e Age must be an integers");
            }
        }

        private void SignupUser_Load(object sender, EventArgs e)
        {

        }
    }
}
