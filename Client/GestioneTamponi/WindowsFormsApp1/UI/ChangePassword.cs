using GestioneTamponi.Class;
using Newtonsoft.Json;
using System;
using System.Windows.Forms;

namespace GestioneTamponi
{
    public partial class ChangePassword : Form
    {
        object logged;
        public ChangePassword(object log)
        {
            this.logged = log;
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == textBox2.Text && textBox1.Text != "")
            {
                string response;
                if (logged.GetType() == typeof(user))
                {
                    response = ((user)logged).ChangePassword(textBox2.Text);
                }
                else
                {
                    response = ((medical)logged).ChangePassword(textBox2.Text);
                }
                switch (response)
                {
                    case "0":
                        MessageBox.Show("Password aggiornata");
                        break;
                    case "-2":
                        MessageBox.Show("Autenticazione fallita");
                        break;
                    case "-1":
                        MessageBox.Show("Errore durante l'aggiornamento");
                        break;
                }
                this.Hide();
            }
            else
            {
                MessageBox.Show("Password don't match");
            }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            this.Hide();
        }
    }
}
