using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;

namespace GestioneTamponi.Class
{
    public class user : ClientInterface<user>
    {
        public string surname { get; set; }
        public string name;
        public string cf;
        public string mail;
        public string phone;
        public string street;
        public string city;
        public string CAP;
        public int n_cv;
        public int age;

        public List<booking> Complete_booked;
        public List<booking> Incomplete_booked;


        public user() : base()
        {
            pathApi = "http://localhost:5000/user";
        }

        public user(string name, string surname, string CF, string street, string mail, string city, string phone, int age, int n_cv, string CAP, string token) : base()
        {
            pathApi = "http://localhost:5000/user";
            this.name = name;
            this.surname = surname;
            this.mail = mail;
            this.cf = CF;
            this.street = street;
            this.city = city;
            this.phone = phone;
            this.CAP = CAP;
            this.age = age;
            this.n_cv = n_cv;
            this.token = token;
            this.Complete_booked = new List<booking>();
            this.Incomplete_booked = new List<booking>();
        }

        public string GetMedical()
        {
            string json_data = JsonConvert.SerializeObject(new { token = this.token });
            return webapi.Post(json_data, pathApi + "/getmedical");
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

        public string InsertBooking(string id, string CF_M, string time)
        {
            string json_data = JsonConvert.SerializeObject(new { token = this.token, id = id, CF_M = CF_M, time = time });
            Console.WriteLine(json_data);
            string response = webapi.Post(json_data, pathApi + "/setbooking");
            if (response != "-6" && response != "-5" && response != "-4" && response != "-3" && response != "-2" && response != "-1")
            {
                JObject jo = JObject.Parse(response);
                booking p = jo.ToObject<booking>();
                this.Incomplete_booked.Add(p);
                Console.WriteLine(p);
                return "0";
            }
            return response;
        }
        public string DeleteBooked(string id)
        {
            string json_data = JsonConvert.SerializeObject(new { token = this.token, id = id  });
            string response = webapi.Post(json_data, pathApi+"/deletebooked");
            try
            {
                JObject jo = JObject.Parse(response);
                booking p = jo.ToObject<booking>();
                this.Incomplete_booked.RemoveAll(booked => booked.practical_num == p.practical_num);
                return "0";
            }
            catch (Exception)
            {
                return response;
            }
        }


    }
}
