using System;
using System.Net;
using System.IO;
using System.Text.RegularExpressions;

namespace C_
{
    class Program
    {
        static void Main(string[] args)
        {
            //C# WebRequest方法默认使用系统配置代理

            Console.WriteLine("Welcome to Monyhar Browser");
            Console.WriteLine("\u6839\u636e\u76f8\u5173\u6cd5\u5f8b\u6cd5\u89c4\u5bf9\u672a\u6210\u5e74\u4eba\u9632\u6b62\u6c89\u8ff7\u7684\u8981\u6c42\uff0c\u8bf7\u8f93\u5165\u60a8\u7684\u8eab\u4efd\u8bc1\u53f7\uff1a");
            string idnumber = Console.ReadLine();
            DateTime now = DateTime.Now;
            int nowDate = (now.Year-18)*10000+now.Month*100+now.Day;
            if((new Regex("\\d{18}")).IsMatch(idnumber)){
                if(int.Parse(idnumber.Substring(6,8))< nowDate){
                    Console.WriteLine("\u901a\u8fc7\u9a8c\u8bc1\uff01");
                }
                else{
                    Console.WriteLine("\u7cfb\u7edf\u68c0\u6d4b\u5230\u60a8\u662f\u672a\u6210\u5e74\u4eba\uff0c\u5c06\u9000\u51fa\u8f6f\u4ef6\u3002");
                    return;
                }
            }

            Console.Write("url:");
            string url = Console.ReadLine().Trim();
            string old_url = url;
            if (Regex.IsMatch(url,"^(http://|https://)[\\w\\W]*")) url = "http://" + url;
            Console.WriteLine("Auto inserted 'http://'.");

            Monyhar internet = new Monyhar(url);
            internet.surf_internet();
            
            if(internet.forMonyhar){
                Console.WriteLine("您好，您访问的页面已经适配了 Monyhar！");
                Console.WriteLine(internet.mstl);
                Console.WriteLine("您是否要查看该网页对西方内核的兼容版本？ [Y/n]");
                if(Console.ReadLine()=="Y")
                Console.WriteLine(internet.html);
            }
            else{
                Console.WriteLine(internet.html);
            }

            Console.WriteLine("Help-About?[Y/n]");
            if (Console.ReadLine() == "Y")
                Console.WriteLine(internet.about());
            Console.WriteLine("Do you want to download the page?[Y/n]");
            if (Console.ReadLine() == "Y")
                internet.save_html(old_url);
        }
    }
    class Monyhar
    {
        public string url { get; private set; }
        public string html { get; private set; }
        public string mstl { get; private set; }
        public bool forMonyhar {get; private set;} = false;
        public Monyhar(string url)
        {
            this.url = url;
        }
        public void surf_internet()
        {
            WebRequest wr = WebRequest.Create(url);
            WebResponse wres = wr.GetResponse();
            Stream stream = wres.GetResponseStream();
            StreamReader sr = new StreamReader(stream);
            this.html = sr.ReadToEnd();
            sr.Close();
            stream.Close();
            wres.Close();

            Regex Rmstl = new Regex("<!--harmony[\\s\\S]*-->");
            Regex RmstlHead = new Regex("^<!--harmony");
            Regex RmstlTail = new Regex("-->$");
            if(Rmstl.IsMatch(html)){
                forMonyhar = true;
                foreach(var mstl in Rmstl.Matches(html)){
                    this.mstl += RmstlTail.Replace(RmstlHead.Replace(mstl.ToString(),"").ToString(),"")+Environment.NewLine;
                }
            }
        }
        public string about()
        {
            return 
@"Monyhar Browser,made by Ranying.
©CopyRight 2021-2021 Ranying, All Rights Reserved.
This project use GPL-3.0 License";
        }
        public void save_html(string old_url)
        {
            using (StreamWriter sw = new StreamWriter($"{Environment.CurrentDirectory}\\{old_url.Replace('/', '_')}.html"))
            {
                sw.Write(html);
            }
        }
    }
}
