using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestioneTamponi.Class
{

    public class ClientInterface<T>
    {
        public string pathApi;
        public string token;

        public ClientInterface()
        {
        }

        public T Login(string Username, string passaword)
        {

            string json_data = JsonConvert.SerializeObject(new { username = Username, pass = passaword });
            string response = webapi.Post(json_data, pathApi + "/login");
            if (response != "False") 
            { 
                JObject jo = JObject.Parse(response);
                return jo.ToObject<T>();
            }
            else {
                return default(T); 
            }

        }

        public string Logout()
        {

            if (this.token != null)
            {
                return webapi.Get(pathApi + "/logout?token=" + this.token);
            }
            return "False";

        }

        public string Delete(string password)
        {
            string json_data = JsonConvert.SerializeObject(new { token = this.token, pass = password });
            return webapi.Post(json_data, pathApi + "/delete");
        }

        public string Modify(T newItem)
        {
            Console.WriteLine(newItem.ToString());
            string response = webapi.Post(newItem.ToString(), pathApi + (typeof(T).Name == "user" ? "/userupdate" : "/medicalupdate"));
            return response;
        }

        public string ChangePassword(string password)
        {
            string json_data = JsonConvert.SerializeObject(new { token = this.token, pass = password });
            return webapi.Post(json_data, pathApi+"/passupdate");
        } 
        public string Signup(string newitem)
        {
            string response = webapi.Post(newitem, pathApi+"/signup");
            return response;
        }

        public override string ToString()
        {
            return JsonConvert.SerializeObject(this);
        }
    }
}
