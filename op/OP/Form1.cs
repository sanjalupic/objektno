using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;


namespace OP
{
    public partial class Form1 : Form
    {
        String operationPerformed = "";
        TcpClient client;
        NetworkStream stream;
        string message = "";
        int byteCount;
        byte[] sendData;

        public Form1()
        {
            InitializeComponent();
        }


        private void num_btn_click(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            result_tb.Text = result_tb.Text + button.Text;
        }

        private void operator_btn_click(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            result_tb.Text = result_tb.Text + button.Text;
            operationPerformed = button.Text;
            
        }

        private void ce_btn_Click(object sender, EventArgs e)
        { 
            result_tb.Text = "";
        }


        private void equal_btn_Click(object sender, EventArgs e)
        {
            
            switch (operationPerformed)
            {
                
                case "+":
                    string[] adds = result_tb.Text.Split('+');
                    message = "Add " + adds[0] + " " + adds[1];
                    break;

                case "-":
                    string[] substracts = result_tb.Text.Split('-');
                    message = "Subtract " + substracts[0] + " " + substracts[1];
                    break;

                case "*":
                    string[] multiplys = result_tb.Text.Split('*');
                    message = "Multiply " + multiplys[0] + " " + multiplys[1];
                    break;

                case "/":
                    string[] divides = result_tb.Text.Split('/');
                    message = "Divide   " + divides[0] + " " + divides[1];
                    break;

                default:

                    break;
            }

            byteCount = Encoding.ASCII.GetByteCount(message);
            sendData = new byte[byteCount];
            sendData = Encoding.ASCII.GetBytes(message);
            stream.Write(sendData, 0, sendData.Length);

            result_tb.Text = "";

        }

        private void connect_btn_Click(object sender, EventArgs e)
        {
            client = new TcpClient(hostname_tb.Text.ToString(), Int32.Parse(port_tb.Text.ToString()));
            stream = client.GetStream();
        }

        private void endconnect_btn_Click(object sender, EventArgs e)
        {
            stream.Close();
            client.Close();
        }
    }
}
