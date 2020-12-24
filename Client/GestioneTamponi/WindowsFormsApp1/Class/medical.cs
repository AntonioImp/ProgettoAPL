using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestioneTamponi.Class
{
    public class medical : ClientInterface<medical>
    {
        private string id;
        public string ID { get { return id; } set { id = value; } }
        public string medical_name;
        public string p_IVA;
        public string phone;
        public string street;
        public string city;
        public string n_cv;
        public string mail;
        public string CAP;
        public string default_interval;
        public string start_time;
        public string end_time;

        public List<doctor> mc_doctor;
        public List<booking> mc_practices;
        public List<booking> Complete_booked;
        public List<booking> Incomplete_booked;
        public medical() : base()
        {
            this.pathApi = "http://localhost:5000/medical";
        }

        public void setInformationMedical(string medName,string street, string mail, string city, string phone, string n_cv, string CAP)
        {
            this.medical_name = medName;
            this.mail = mail;
            this.street = street;
            this.city = city;
            this.phone = phone;
            this.CAP = CAP;
            this.n_cv = n_cv;
        }
        public string SetMedicalTime(string start_time, string end_time, string default_time ) 
        {
            string postData = JsonConvert.SerializeObject(new { token = this.token, start_time = start_time, end_time = end_time, default_interval = default_time });
            Console.WriteLine(postData);
            string response = webapi.Post(postData, pathApi+"/timeupdate");
            return response;
        }

        public void GetDoctor()
        {
            string postData = JsonConvert.SerializeObject(new { token = this.token });
            string response = webapi.Post(postData, pathApi+"/docassignment");
            if(response != "-2")
            {
                JObject jo = JObject.Parse(response);
                foreach (doctor d in jo["DocAssign"].ToObject<doctor[]>()) this.mc_doctor.Add(d);
            }
        }

        public void GetBooked()
        {
            string postData = JsonConvert.SerializeObject(new { token = this.token });
            string response = webapi.Post(postData, pathApi+"/getbooked");
            if (response != "-2")
            {
                JObject jo = JObject.Parse(response);
                this.Complete_booked = jo["complete"].ToObject<List<booking>>();
                this.Incomplete_booked = jo["incomplete"].ToObject<List<booking>>();
            }
        }

        public string NewDoctor(doctor d)
        {
            string postData = JsonConvert.SerializeObject(new { token = this.token, name = d.name, surname = d.surname, CF = d.CF, phone = d.phone, mail = d.mail, days = d.days });
            string response = webapi.Post(postData, pathApi + "/insertdoc");
            return response;

        }
        public string UpdateDoctor(doctor d)
        {
            string postData = JsonConvert.SerializeObject(new { token = this.token, name = d.name, surname = d.surname, CF = d.CF, phone = d.phone, mail = d.mail });
            string response = webapi.Post(postData, pathApi+"/updatedoc");
            if (response == "0")
            {
                this.mc_doctor.Find(mc => mc.CF == d.CF).ModifyDoctor(d);
            }
            return response;
        }

        public string DeleteDoctor(doctor d)
        {
            string json_data = JsonConvert.SerializeObject(new { token = this.token, CF = d.CF });
            string response = webapi.Post(json_data, pathApi + "/dismissdoc");
            if (response == "0")
            {
                this.mc_doctor.RemoveAll(doc => doc.CF == d.CF);
            }
            return response;
        }

        public string SetExec(int id, string time_exec, string result)
        {
            string json_data = JsonConvert.SerializeObject(new { id = id, time = time_exec, result = result, token = this.token});
            string response = webapi.Post(json_data, pathApi + "/insertexec");
            if (response != "-6" && response != "-5" && response != "-4" && response != "-3" && response != "-2" && response != "-1")
            {
                JObject jo = JObject.Parse(response);
                booking pp = jo.ToObject<booking>();
                this.Incomplete_booked.RemoveAll(pr => pr.practical_num == pp.practical_num);
                this.Complete_booked.Add(pp);
                return "0";
            }
            return response;
        }

    }
}
