using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using MySql.Data.MySqlClient;
using System.Data;


namespace AIRTEL
{
    public partial class CLIENT1 : System.Web.UI.Page
    {
        MySql.Data.MySqlClient.MySqlConnection conn;
        MySql.Data.MySqlClient.MySqlCommand cmd;
        String queryStr;
        MySqlConnection conn2 = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=airtel;User Id=root;Password=''");

        protected void cmdsave_Click(object sender, EventArgs e)
        {
            String ConnString = System.Configuration.ConfigurationManager.ConnectionStrings["AIRTELAppConnString"].ToString();
            conn = new MySql.Data.MySqlClient.MySqlConnection(ConnString);
            conn.Open();
            queryStr = "";
            queryStr = "INSERT INTO airtel.client(CLIENT_NO,CLIENT_NA,CLIENT_CO,CLIENT_AD,CLIENT_SE,CLIENT_AM)" +
                            "VALUES('" + a.Text + "','" + b.Text + "','" + c.Text + "','" + d.Text + "','" + ee.Text + "','" + f.Text + "')";
            cmd = new MySql.Data.MySqlClient.MySqlCommand(queryStr, conn);
            cmd.ExecuteReader();
            conn.Close();
            Response.Write("Your Data has been saved successfully !");
            clr();
        }
        private void clr()
        {
            a.Text = "";
            b.Text = "";
            c.Text = "";
            d.Text = "";
            ee.Text = "";
            f.Text = "";
        }
        protected void cmdclr_Click(object sender, EventArgs e)
        {
            clr();
        }
        protected void cmddelete_Click(object sender, EventArgs e)
        {
            conn2.Open();
            MySqlCommand cmd2 = conn2.CreateCommand();
            cmd2.CommandType = CommandType.Text;
            cmd2.CommandText = "delete from CLIENT where CLIENT_NO='" + a.Text + "'";
            cmd2.ExecuteNonQuery();
            conn2.Close();
            Response.Write("Your Data has been Delete Permanently !");
            clr();
        }
        protected void cmdupdate_Click(object sender, EventArgs e)
        {
            conn2.Open();
            MySqlCommand cmd2 = conn2.CreateCommand();
            cmd2.CommandType = CommandType.Text;
            cmd2.CommandText = "update CLIENT set CLIENT_NO='" + a.Text + "',CLIENT_NA='" + b.Text + "' where CLIENT_NO='" + a.Text + "'";
            cmd2.ExecuteNonQuery();
            conn2.Close();
            Response.Write("Your Data has been Updated Successfully !");
            clr();
        }
        protected void cmdupdate0_Click(object sender, EventArgs e)
        {
            displaydata();
        }
        private void displaydata()
        {

            String ConnString = System.Configuration.ConfigurationManager.ConnectionStrings["AIRTELAppConnString"].ToString();
            conn = new MySqlConnection(ConnString);
            conn.Open();
            queryStr = "";
            queryStr = "select * from client";
            cmd = new MySqlCommand(queryStr, conn);
            cmd.ExecuteNonQuery();
            DataTable dt = new DataTable();
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(dt);
            GridView1.DataSource = dt;
            GridView1.DataBind();
            conn.Close();
        }

        protected void Page_Load(object sender, EventArgs e)
        {
            // a.Enabled = true;
            //a.Enabled = false;
            //a.Visible = false;

        }


        protected void searchBtn_Click(object sender, EventArgs e)
        {
            searchbtn444();
        }
        private void searchbtn444()
        {

            MySqlConnection conn2 = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=Airtel;User Id=root;Password=''");


            string find = "select * from client where(Client_No like '" + aa.Text + "' or   Client_na like '" + aa.Text + "' or   Client_co like '" + aa.Text + "')";

            MySqlCommand cmd2 = new MySql.Data.MySqlClient.MySqlCommand(find, conn2);
            cmd2.Parameters.Add("@Client_No", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@Client_Na", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@Client_Co", SqlDbType.VarChar).Value = aa.Text;

            conn2.Open();
             cmd2.ExecuteNonQuery();

            DataTable dt = new DataTable();
            MySqlDataAdapter da = new MySqlDataAdapter();
            da.SelectCommand = cmd2;
            DataSet ds = new DataSet();
            da.Fill(ds, "Client_No");
            da.Fill(ds, "Client_Na");
            da.Fill(ds, "Client_Co");
            GridView1.DataSource = ds;
            GridView1.DataBind();
            conn2.Close();

        }

        protected void SEARCH_Click(object sender, EventArgs e)
        {
            MySqlConnection conn = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=airtel;User Id=root;Password=''");
            conn2.Open();
            if (aa.Text != "")
            {
                MySqlCommand cmd = new MySqlCommand("SELECT Client_no, client_na, Client_co, client_ad,client_se,client_am from client WHERE client_no =@id", conn2);
                cmd.Parameters.AddWithValue("@id", aa.Text);
                MySqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    a.Text = dr.GetValue(0).ToString();
                    b.Text = dr.GetValue(1).ToString();
                    c.Text = dr.GetValue(2).ToString();
                    d.Text = dr.GetValue(3).ToString();
                    ee.Text = dr.GetValue(4).ToString();
                    f.Text = dr.GetValue(5).ToString();
                }
            }
        }
    }
}