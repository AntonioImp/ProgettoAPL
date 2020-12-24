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
using GestioneTamponi.Class;

namespace GestioneTamponi
{
    
    public partial class Modifica_info_U : Form
    {
        user userLogged;
        public Modifica_info_U(user u)
        {
            userLogged = u;
            InitializeComponent();
        }
        private void Modifica_info_U_Load(object sender, EventArgs e)
        {
            tName.Text = userLogged.name;
            tSurname.Text = userLogged.surname;
            tMail.Text = userLogged.mail;
            tAge.Text = userLogged.age.ToString();
            tPhone.Text = userLogged.phone;
            tCity.Text = userLogged.city;
            tStreet.Text = userLogged.street;
            tCAP.Text = userLogged.CAP;
            tN_cv.Text = userLogged.n_cv.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            user u = new user(tName.Text,tSurname.Text,userLogged.cf,tStreet.Text,tMail.Text,tCity.Text,tPhone.Text, Int32.Parse(tAge.Text), Int32.Parse(tN_cv.Text),tCAP.Text,userLogged.token);
            switch (userLogged.Modify(u))
            {
                case "0":
                    MessageBox.Show("Modifica avvenuta");
                    userLogged = u;
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
            new Userview(userLogged).Show();
            Console.WriteLine("Esco1");

            this.Hide();
            Console.WriteLine("Esco2");
        }

    }
}
