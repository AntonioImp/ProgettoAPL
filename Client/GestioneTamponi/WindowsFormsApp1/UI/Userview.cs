using System;
using System.Collections.Generic;
using System.Windows.Forms;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using GestioneTamponi.Class;
using RDotNet;
using System.IO;

namespace GestioneTamponi
{
    public partial class Userview : Form
    {
        REngine engine; //REngine per utilizzare R
        private readonly RGraphAppHook cbt; //Tool per intrappolare la finestra di R
        private readonly RGraphAppHook cbt2; //Tool per intrappolare la finestra di R

        user userLogged = new user();
        private Dictionary<string, medical> medical = new Dictionary<string, medical>();
        private Dictionary<string, string[]> time_doctor = new Dictionary<string, string[]>();
        
        public Userview(user us)
        {
            InitializeComponent();
            REngine.SetEnvironmentVariables(rPath: "C:\\Program Files\\R\\R-3.4.3\\bin\\i386", rHome: "C:\\Program Files\\R\\R-3.4.3");
            engine = REngine.GetInstance();
            cbt = new RGraphAppHook { GraphControl = panel2 };
            cbt2 = new RGraphAppHook { GraphControl = panel3 };
            userLogged = us;
            userLogged.GetBooked();
            
        }

        private void MedicalLoad()
        {
            string response = userLogged.GetMedical();
            if (response == "-2") { MessageBox.Show("Impossibile caricare i Medical disponibili per problemi di autenticazione"); }
            else 
            {
                JObject jo = JObject.Parse(response);
                foreach (var mc in jo)
                {
                    medical m = mc.Value.ToObject<medical>();
                    medical.Add(m.ID, m);
                    SelectMedicalC.Items.Add(m.ID);
                }
            }
        }

        public void InfoMedicalLoad()
        {
            foreach (KeyValuePair<string, medical> entry in medical)
            {
                var row = new string[] { entry.Value.medical_name, entry.Value.CAP, entry.Value.mail, entry.Value.phone, entry.Value.city, entry.Value.street+" - NC:"+entry.Value.n_cv };
                var newItem = new ListViewItem(row);
                medicalList.Items.Add(newItem);
            }
        }

        private void BookedLoad()
        {
            listP.Items.Clear();
            List<booking> pp;
            if (CheckBooked.Checked == true) pp = userLogged.Complete_booked; else pp = userLogged.Incomplete_booked;
            
            foreach (booking p in pp)
            {
                var row = new string[] { p.practical_num, p.id, p.CF_M, p.date, p.time, (CheckBooked.Checked == true)? "Eseguito" : "Non eseguito", p.time_taken, p.result };
                var newItem = new ListViewItem(row);
                newItem.Tag = p.practical_num;
                listP.Items.Add(newItem);
            }
        }
 
        private void Userview_Load(object sender, EventArgs e)
        {
            Date.Text = webapi.Get("http://localhost:5000/getday");
            MedicalLoad();
            BookedLoad(); 
            InfoMedicalLoad();
            StatLoad();
            StatLoad2();
        }

        


        private void modificaInformazioniToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new Modifica_info_U(userLogged).Show();
            this.Hide();
        }

        private void logoutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (userLogged.Logout() == "0")
            {
                new Login().Show();
                this.Close();

            }
        }

        private void modificaPasswordToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new ChangePassword(userLogged).Show();
        }

        private void confirmToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (toolStripTextBox2.Text == "")MessageBox.Show("Inserisci prima la password");
            else
            {
                switch (userLogged.Delete(toolStripTextBox2.Text))
                {
                    case "0":
                        MessageBox.Show("Eliminato");
                        new Login().Show();
                        this.Hide();
                        break;
                    case "-1":
                        MessageBox.Show("Errore eliminazione");
                        break;
                    case "-2":
                        MessageBox.Show("Autenticazione fallita");
                        break;
                    case "-3":
                        MessageBox.Show("Password errata");
                        break;
                    default:
                        new Login().Show();
                        this.Hide();
                        break;
                }
            }
        }

        


        private void CheckBooked_CheckedChanged(object sender, EventArgs e)
        {
            BookedLoad();
        }

        private void DeleteLabel_Click(object sender, EventArgs e)
        {
            if (listP.SelectedItems.Count != 0)
            {
                string response = userLogged.DeleteBooked(listP.SelectedItems[0].SubItems[0].Text);
                if (response == "0") BookedLoad();
                else MessageBox.Show("Errore durante l'eliminazione. Inoltre non è possibile eliminare una prenotazione con stato 'Eseguita'");
            }
        }

        private void LogoutLabel_Click(object sender, EventArgs e)
        {
            if (userLogged.Logout() == "0")
            {
                new Login().Show();
                this.Close();
            }
        }

        private void Booked_Click(object sender, EventArgs e)
        {
            string response = userLogged.InsertBooking((string)SelectMedicalC.SelectedItem, (string)SelectDoctor.SelectedItem, (string)SelectTime.SelectedItem);
            if (response == "0") BookedLoad();
            else if (response == "-6") MessageBox.Show("Hai già effettuato una prenotazioni per questo giorno, prova ad eliminare la prenotazione precedente.");
            else MessageBox.Show("Errore durante la prenotazione/Autenticazione fallita");
        }

        private void BackBottom_Click(object sender, EventArgs e)
        {
            InfoMedicalPanel.Visible = false;
            panel3.Visible = true;
        }

        private void InfoMedical_Click(object sender, EventArgs e)
        {
            InfoMedicalPanel.Visible = true;
            panel3.Visible = false;
        }

        private void SelectMedicalC_SelectedIndexChanged(object sender, EventArgs e)
        {
            time_doctor.Clear();
            SelectDoctor.Items.Clear();
            SelectDoctor.Text = "";
            SelectTime.Items.Clear();
            SelectTime.Text = "";
            
            string json_data = JsonConvert.SerializeObject(new { token = userLogged.token, id = SelectMedicalC.SelectedItem });
            string response = webapi.Post(json_data, "http://localhost:5000/user/getcalendar");
            switch (response)
            {
                case "-3":
                    SelectDoctor.Text = "Nessun dottore disponibile";
                    break;
                case "-1":
                    SelectDoctor.Text = "Disponibilità esaurita";
                    break;
                case "-2":
                    MessageBox.Show("Autenticazione fallita");
                    break;
                default:
                    JObject jo = JObject.Parse(response);
                    time_doctor = jo.ToObject<Dictionary<string, string[]>>();
                    foreach (KeyValuePair<string, string[]> entry in time_doctor)
                    {
                       SelectDoctor.Items.Add(entry.Key);
                    }
                    break;
            }

        }

        private void SelectDoctor_SelectedIndexChanged(object sender, EventArgs e)
        {
            SelectTime.Text = "";
            SelectTime.Items.Clear();
            string[] time;
            time_doctor.TryGetValue((string)SelectDoctor.SelectedItem, out time);
            if (time.Length != 0)
            {
                foreach (string t in time)
                {
                    SelectTime.Items.Add(t);
                }
            }
        }

        public void StatLoad()
        {
            engine.Evaluate("graphics.off()");
            cbt.Install();
            engine.Evaluate("library(jsonlite)");
            engine.Evaluate("library(httr)");
            engine.Evaluate("res <- GET('http://localhost:5000/getallbooked')");
            engine.Evaluate("data <- fromJSON(rawToChar(res$content))");
            engine.Evaluate("info <- data$booked[c(-4)]");
            engine.Evaluate("label <- c(\"Positivo\", \"Negativo\")");
            var n = engine.Evaluate("nvn <-  nrow(subset(info, info$result == \"negativo\"))").AsNumeric();
            var m = engine.Evaluate("nvp <-  nrow(subset(info, info$result == \"positivo\"))").AsNumeric();
            engine.Evaluate("values <- c(nvp,nvn)");
            if (n[0] != 0 || m[0] != 0)
            {
                engine.Evaluate("percent <- round(values / sum(values) * 100)");
                engine.Evaluate("label <- paste(label, percent)");
                engine.Evaluate("label <- paste(label, \" % \", sep = \"\")");
                engine.Evaluate("par(mar=c(1,1,1,1),col.main = \"Dimgray\", col.axis = \"Dimgray\",bg = \"LightSteelBlue\", col.lab = \"red\" )");
                engine.Evaluate("pie(values,labels = label, main = \"Grafico andamento tamponi\",  cex.lab= 0.3,cex.main=1,cex.axis = 9, cex.names=0.5)");
            }
            else
            {
                MessageBox.Show("Non ci sono statistiche.");
            }
            cbt.Uninstall();
        }

        public void StatLoad2() 
        {
            cbt2.Install();
            engine.Evaluate("win.graph()");
            var f = File.OpenRead("StatisticTamponi.R");
            engine.Evaluate(f);
            cbt2.Uninstall();
        }

    }
}
