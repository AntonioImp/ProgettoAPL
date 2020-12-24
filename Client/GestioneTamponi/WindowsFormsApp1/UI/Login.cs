using System;
using System.Windows.Forms;
using Newtonsoft.Json;
using GestioneTamponi.Class;
using RDotNet;
namespace GestioneTamponi
{

    public partial class Login : Form
    {

        public Login()
        {
            InitializeComponent();
        }


        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            new SignupMC().Show();
            this.Hide();
        }


        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            new SignupUser().Show();
            this.Hide();
        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            textBox3.Text = "";

            if (CheckRoles.CheckedItems.Count != 0 && usernameBox.Text.Trim() != "")
            {
                
                string postData = JsonConvert.SerializeObject(new { username = usernameBox.Text });
                string response = webapi.Post(postData, "http://localhost:5000/user/passreset");
                switch (response)
                {
                    case "0":
                        MessageBox.Show("E' stata mandata una email contente la nuova password");
                        break;
                    case "-1":
                        MessageBox.Show("Problemi col server, impossibile resettare la password");
                        break;
                    case "-2":
                        MessageBox.Show("Utente con codice fiscale:" + usernameBox.Text + " non trovato");
                        break;
                    case "-3":
                        MessageBox.Show("Problemi col server, impossibile resettare la password");
                        break;
                }
            }
            else
            {
                textBox3.Text = "Inserire username o check non selezionata";
            }

        }

        private void checkedListBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            int index = CheckRoles.SelectedIndex;
            int count = CheckRoles.Items.Count;
            for (int x = 0; x < count; x++)
            {
                if (index != x)
                {
                    CheckRoles.SetItemChecked(x, false);
                }
            }
        }

        private void Signin_Click(object sender, EventArgs e)
        {
            textBox3.Text = "";
            Object res;
            if (CheckRoles.CheckedItems.Count != 0 && usernameBox.Text.Trim() != "" && passBox.Text.Trim() != "")
            {
                string JsonName = ((string)CheckRoles.SelectedItem == "User" ? "user" : "medical");
                if (JsonName == "user")
                {
                    user newUs = new user();
                    user us = newUs.Login(usernameBox.Text, passBox.Text);
                    switch (us)
                    {
                        case null:
                            textBox3.Text = "User name or password is incorrect";
                            break;
                        default:
                            new Userview(us).Show();
                            this.Hide();
                            break;
                    }
                }else
                {
                    medical newB = new medical();
                    medical m = newB.Login(usernameBox.Text, passBox.Text);
                    switch (m)
                    {
                        case null:
                            textBox3.Text = "User name or password is incorrect";
                            break;
                        default:
                            new MedicalCenterview(m).Show();
                            this.Hide();
                            break;
                    }
                }
            }else
            {
                textBox3.Text = "Input non validi o check non selezionata";
            }
        }

        private void Login_Load(object sender, EventArgs e)
        {
            usernameBox.Text = "E";
            passBox.Text = "E";
            CheckRoles.SetItemChecked(0, true);
        }

    }
}