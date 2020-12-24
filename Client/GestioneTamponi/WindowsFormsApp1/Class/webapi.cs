using Newtonsoft.Json.Linq;
using System;
using System.IO;
using System.Net;
using System.Reflection;

namespace GestioneTamponi
{
    static  class  webapi
    {
        static string strurl;
        static WebRequest request;

        public static string Post(string postData, String url)
        {

            try
            {
                strurl = String.Format(url);
                request = WebRequest.Create(strurl);
                request.Method = "POST";
                request.ContentType = "application/json";

                using (var streamWriter = new StreamWriter(request.GetRequestStream()))
                {
                    streamWriter.Write(postData);
                    streamWriter.Flush();
                    streamWriter.Close();

                    var httpResponse = (HttpWebResponse)request.GetResponse();

                    using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
                    {
                        return streamReader.ReadToEnd();

                    }


                }
            }
            catch (WebException e)
            {

                if (e.Status == WebExceptionStatus.ConnectFailure)
                {
                    Console.WriteLine("Error Server");
                }
                else if (e.Status == WebExceptionStatus.ProtocolError)
                {
                    Console.WriteLine("Error request");
                }
            }
            catch (UriFormatException e1)
            {
                Console.WriteLine("Error URI");
            }
            return "False";
        }
        public static string Get(String url)
        {
            strurl = String.Format(url);
            request = WebRequest.Create(strurl);
            request.Method = "GET";
            request.ContentType = "application/json";
            try
            {
                var httpResponse = (HttpWebResponse)request.GetResponse();
                using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
                {
                    return streamReader.ReadToEnd();
                }
            }
            catch (WebException e)
            {

                if (e.Status == WebExceptionStatus.ConnectFailure)
                {
                    Console.WriteLine("Error Server");

                }
                else if (e.Status == WebExceptionStatus.ProtocolError)
                {
                    Console.WriteLine("ErrorRequest");
                }
            }
            return "";
}
}
}
