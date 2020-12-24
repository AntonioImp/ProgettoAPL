using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestioneTamponi.Class
{
    public class booking
    {
        public string practical_num { get; set; }
        public string CF{ get; set; }
        public string id{ get; set; }
        public string CF_M{ get; set; }
        public string time{ get; set; }
        public string date{ get; set; }
        public string state { get; set; }
        public string result { get; set; }
        public string time_taken { get; set; }

        public booking(string p_num, string cf_u, string id_m, string cf_m, string date, string time, string result, string state, string time_exe) {
            this.CF = cf_u;
            this.id = id_m;
            this.practical_num = p_num;
            this.CF_M = cf_m;
            this.date = date;
            this.time = time;
            this.result = result;
            this.state = state;
            this.time_taken = time_exe;
        }

        public string toString()
        {
            return JsonConvert.SerializeObject(this);
        }
    }
}
