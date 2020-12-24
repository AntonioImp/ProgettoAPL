using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestioneTamponi.Class
{
    public class doctor
    {
        public string name { get; set; }
        public string surname { get; set; }
        private string cf;
        public string CF { get { return cf; } set { cf = value; } }
        public string mail { get; set; }
        public string phone { get; set; }
        public string avarage_time { get; set; }
        public List<string> days { get; set; }
       

        public doctor(string name, string surname, string CF, string phone, string mail, List<string> day = null )
        {
            this.name = name;
            this.surname = surname;
            this.mail = mail;
            this.CF = CF;
            this.phone = phone;
            this.days = day;
        }

        public void ModifyDoctor(doctor d)
        {
            this.name = d.name;
            this.surname = d.surname;
            this.mail = d.mail;
            this.phone = d.phone;
        }


        public string toString() {
            return JsonConvert.SerializeObject(this);
        }
    }
}
