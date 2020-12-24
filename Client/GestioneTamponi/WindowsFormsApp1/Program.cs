using System;
using System.Windows.Forms;

namespace GestioneTamponi
{
    static class Program
    {

        /// Punto di ingresso principale dell'applicazione.

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Login mainForm = new Login();
            Application.Run(mainForm);
        }
    }
}
