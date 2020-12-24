using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Windows.Forms;
using GestioneTamponi.Class;
using RDotNet;
using GestioneTamponi.UI;
using System.IO;

namespace GestioneTamponi
{
    public partial class MedicalCenterview : Form
    {
        medical medicalLogged;
        private readonly RGraphAppHook cbt;
        REngine engine;

        public MedicalCenterview(medical mc)
        {

            InitializeComponent();
            REngine.SetEnvironmentVariables(rPath: "C:\\Program Files\\R\\R-3.4.3\\bin\\i386", rHome: "C:\\Program Files\\R\\R-3.4.3");
            engine = REngine.GetInstance();
            cbt = new RGraphAppHook { GraphControl = Graph };
            medicalLogged = mc;
            medicalLogged.mc_doctor = new List<doctor>();
            medicalLogged.GetBooked();
            medicalLogged.GetDoctor();
            Console.WriteLine("MED:"+medicalLogged.medical_name);
        }

        private void MedicalCenterview_Load(object sender, EventArgs e)
        {
            GetDay();
            DoctorLoad();
            BookedLoad();
            GraphCombobox.SelectedIndex = 1;
        }

        public void DoctorLoad()
        {
            listDoctor.Items.Clear();
            foreach (doctor doc in medicalLogged.mc_doctor) { 
                var row = new string[] { doc.name, doc.surname, doc.CF, string.Join("/", doc.days), (doc.avarage_time != "None")?doc.avarage_time : ""};
                var lvi = new ListViewItem(row);
                lvi.Tag = doc;
                listDoctor.Items.Add(lvi);
            }
        }

        public void GetDay() 
        {
            label2.Text = webapi.Get("http://localhost:5000/getday");
        }

        public void BookedLoad() {
            listP.Items.Clear();
            ID_Pr_ComboBox.Items.Clear();
            ID_Pr_ComboBox.Text = "";
            if (CheckEseguite.Checked == true)
            {
                foreach (booking p in medicalLogged.Complete_booked)
                {
                    var row = new string[] { p.practical_num, p.id, p.CF_M, p.date, p.time, "ESEGUITA", p.time_taken, p.result };
                    var lvi = new ListViewItem(row);
                    if (checkTutte_Odierne.Checked == false && p.date == label2.Text) listP.Items.Add(lvi);
                    else if (checkTutte_Odierne.Checked == true) listP.Items.Add(lvi);
                }
            }
            else if (CheckEseguite.Checked == false)
            {

                foreach (booking p in medicalLogged.Incomplete_booked)
                {
                    var row = new string[] { p.practical_num, p.id, p.CF_M, p.date, p.time, "NON ESEGUITA", p.time_taken, p.result };
                    var lvi = new ListViewItem(row);
                    bool d = p.date.ToString() == label2.Text;
                    if (checkTutte_Odierne.Checked == false && p.date == label2.Text) listP.Items.Add(lvi);
                    else if (checkTutte_Odierne.Checked == true) listP.Items.Add(lvi);

                }
            }
            foreach (booking p in medicalLogged.Incomplete_booked)
            {
                ID_Pr_ComboBox.Items.Add(p.practical_num);
            }
        }

        private void modificaInformazioniToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new Modifica_info_MC(medicalLogged, this).Show();
            this.Hide();
        }


        private void modificaPasswordToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new ChangePassword(medicalLogged).Show();
        }
  
        //DELETE MEDICAL CENTER
        private void confirmToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            if (InputPassword.Text == "")
            {
                MessageBox.Show("Inserire prima la password");
            }
            else
            {
                switch (medicalLogged.Delete(InputPassword.Text))
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
                }
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            new AddNewDoctor(medicalLogged, this).Show();
            this.Hide();
        }


        private void button3_Click(object sender, EventArgs e)
        {
            if (listDoctor.SelectedItems.Count == 0) MessageBox.Show("Seleziona un dottore.");
            else
            {
                MessageBox.Show(listDoctor.SelectedItems[0].SubItems[2].Text);
                new Modify_Doctor((doctor)listDoctor.SelectedItems[0].Tag, medicalLogged, this).Show();

            }
        }

        private void listOfDoctorsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            panel1.Visible = true;
        }
      private void DeleteDoctorButton_Click(object sender, EventArgs e)
        {
            if (listDoctor.SelectedItems.Count == 0) { MessageBox.Show("Seleziona un dottore."); }
            else
            {
                string response = medicalLogged.DeleteDoctor((doctor)listDoctor.SelectedItems[0].Tag);
                switch (response)
                {
                    case "0":
                        MessageBox.Show("Dottore Eliminato");
                        DoctorLoad();
                        break;
                    case "-1":
                        MessageBox.Show("Errore eliminazione");
                        break;
                    case "-2":
                        MessageBox.Show("Autenticazione fallita");
                        break;
                    case "-3":
                        MessageBox.Show("Dottore impagnato in una prenotazione, verrà eliminato dopo aver eseguito la prenotazione");
                        break;
                }
            }
        }


        private void label3_Click(object sender, EventArgs e)
        {
            if (medicalLogged.Logout() == "0")
            {
                new Login().Show();
                this.Hide();
                this.Close();
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            BookedLoad();
        }

        private void CheckEseguite_CheckedChanged(object sender, EventArgs e)
        {
            BookedLoad();
        }

        private void GraphCombobox_SelectedIndexChanged(object sender, EventArgs e)
        {
            StatisticLoad();
        }

        private void ExecBooking_Click(object sender, EventArgs e)
        {
            if (ID_Pr_ComboBox.SelectedIndex > -1)
            {
                string time_exec = Hour.Text + ":" + Minute.Text + ":" + Seconds.Text;


                string response = medicalLogged.SetExec(Int32.Parse(ID_Pr_ComboBox.SelectedItem.ToString()), time_exec, (string)EsitoCombobox.SelectedItem);
                switch (response)
                {
                    case "0":
                        MessageBox.Show("Prenotazione eseguita");
                        BookedLoad();
                        StatisticLoad();
                        break;
                    case "-1":
                        MessageBox.Show("Errore durante l'esecuzione della prennotazione");
                        break;
                    case "-2":
                        MessageBox.Show("Autenticazione fallita");
                        break;
                    case "-3":
                        MessageBox.Show("Formato orario non valide");
                        break;
                    case "-4":
                        MessageBox.Show("Risultato non valido");
                        break;
                }
            }
        }

        private void modificaOrariMCToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new Modify_MC_Time(medicalLogged, this).Show();
        }

        public void StatisticLoad()
        {
            if (GraphCombobox.SelectedIndex == 2)
            {
                cbt.Install();
                var f = File.OpenRead("StatisticTamponi.R");
                engine.Evaluate(f);
                cbt.Uninstall();
            }
            else
            {
                engine.Evaluate("graphics.off()");
                cbt.Install();
                engine.Evaluate("library(jsonlite)");
                engine.Evaluate("data <- fromJSON('http://localhost:5000/getallbooked')");
                engine.Evaluate("info <- data$booked[c(-4)]");
                engine.Evaluate("label <- c(\"Positivo\", \"Negativo\")");
                engine.Evaluate("s <- \"globali\"");
                if (GraphCombobox.SelectedIndex == 0)
                {
                    engine.Evaluate("info <- subset(info, info$ID_M ==" + medicalLogged.ID + ")");
                    engine.Evaluate("s <- \"medical: " + medicalLogged.medical_name + "\"");
                }
                var n = engine.Evaluate("nvn <-  nrow(subset(info, info$result == \"negativo\"))").AsNumeric();
                var m = engine.Evaluate("nvp <-  nrow(subset(info, info$result == \"positivo\"))").AsNumeric();
                engine.Evaluate("values <- c(nvp,nvn)");
                if (n[0] != 0 || m[0] != 0)
                {
                    engine.Evaluate("percent <- round(values / sum(values) * 100)");
                    engine.Evaluate("label <- paste(label, percent)");
                    engine.Evaluate("label <- paste(label, \" % \", sep = \"\")");
                    engine.Evaluate("par(mar=c(1,1,1,1),col.main = \"Dimgray\", col.axis = \"Dimgray\",bg = \"LightSteelBlue\", col.lab = \"red\" )");
                    engine.Evaluate("pie(values,labels = label, main = paste(\"Grafico andamento tamponi \",s),  cex.lab= 0.3,cex.main=1,cex.axis = 9, cex.names=0.5)");
                }
                else
                {
                    MessageBox.Show("Non ci sono statistiche.");
                }
                cbt.Uninstall();
            }
        }
    }
}
