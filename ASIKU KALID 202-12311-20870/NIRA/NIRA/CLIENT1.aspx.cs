using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using MySql.Data.MySqlClient;
using System.Data;


namespace NIRA
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        MySql.Data.MySqlClient.MySqlConnection conn;
        MySql.Data.MySqlClient.MySqlCommand cmd;
        String queryStr;
        MySqlConnection conn2 = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=NIRA;User Id=root;Password=''");
        protected void cmdsave_Click1(object sender, EventArgs e)
        {
            String ConnString = System.Configuration.ConfigurationManager.ConnectionStrings["NIRAAppConnString"].ToString();
            conn = new MySql.Data.MySqlClient.MySqlConnection(ConnString);
            conn.Open();
            queryStr = "";
            queryStr = "INSERT INTO NIRA.DEATH(DEATH_NUMBER,NAME,GENDER,DISTRICT,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_DEATH,PLACE_OF_DEATH)" +
                            "VALUES('" + a.Text + "','" + b.Text + "','" + c.Text + "','" + d.Text + "','" + ee.Text + "','" + f.Text + "','" + g.Text + "','" + h.Text + "','" + j.Text + "')";
            cmd = new MySql.Data.MySqlClient.MySqlCommand(queryStr, conn);
            cmd.ExecuteReader();
            conn.Close();
            Response.Write("Your Data has been saved successfully !");
            clr();
        }
        protected void cmdclr_Click1(object sender, EventArgs e)
        {
            a.Text = "";
            b.Text = "";
            c.Text = "";
            d.Text = "";
            ee.Text = "";
            f.Text = "";
            g.Text = "";
            h.Text = "";
            j.Text = "";
        }
        protected void cmdclr_Click(object sender, EventArgs e)
        {
            clr();
        }

        protected void cmddel_Click(object sender, EventArgs e)
        {
            conn2.Open();
            MySqlCommand cmd2 = conn2.CreateCommand();
            cmd2.CommandType = CommandType.Text;
            cmd2.CommandText = "delete from DEATH where DEATH_NUMBER='" + a.Text + "'";
            cmd2.ExecuteNonQuery();
            conn2.Close();
            Response.Write("Your Data has been Delete Permanently !");
            clr();
        }
        protected void cmdupdate_Click1(object sender, EventArgs e)
        {
            conn2.Open();
            MySqlCommand cmd2 = conn2.CreateCommand();
            cmd2.CommandType = CommandType.Text;
            cmd2.CommandText = "update DEATH set DEATH_NUMBER='" + a.Text + "',NAME='" + b.Text + "',GENDER='" + c.Text + "',DISTRICT='" + d.Text + "',NATIONALITY='" + ee.Text + "',DATE_OF_BIRTH='" + f.Text + "',PLACE_OF_BIRTH='" + g.Text + "',DATE_OF_DEATH='" + h.Text + "',PLACE_OF_DEATH='" + j.Text + "'where DEATH_NUMBER='" + a.Text + "'";
            cmd2.ExecuteNonQuery();
            conn2.Close();
            Response.Write("Your Data has been Updated Successfully !");
            clr();
        }

        private void clr()
        {
            //throw new NotImplementedException();
        }
        protected void cmdupdate0_Click1(object sender, EventArgs e)
        {
            displaydata();
        }

        private void displaydata()
        {

            String ConnString = System.Configuration.ConfigurationManager.ConnectionStrings["NIRAAppConnString"].ToString();
            conn = new MySqlConnection(ConnString);
            conn.Open();
            queryStr = "";
            queryStr = "select * from DEATH";
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

        }
        protected void cmdsearch_Click(object sender, EventArgs e)
        {
            searchbtn444();
        }
        private void searchbtn444()
        {

            MySqlConnection conn2 = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=Nira;User Id=root;Password=''");


            string find = "select * from Death where(DEATH_NUMBER like '" + aa.Text + "' or  NAME  like '" + aa.Text + "' or GENDER  like '" + aa.Text + "' or DISTRICT like '" + aa.Text + "' or NATIONALITY  like '" + aa.Text + "' or DATE_OF_BIRTH  like '" + aa.Text + "' or PLACE_OF_BIRTH like '" + aa.Text + "' or DATE_OF_DEATH like'" + aa.Text + "' or PLACE_OF_BIRTH like '" + aa.Text + "')";

            MySqlCommand cmd2 = new MySql.Data.MySqlClient.MySqlCommand(find, conn2);
            cmd2.Parameters.Add("@DEATH_NUMBER", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@NAME", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@GENDER", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@DISTRICT", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@NATIONALITY", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@DATE_OF_BIRTH", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@PLACE_OF_BIRTH", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@DATE_OF_DEATHH", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@PLACE_OF_DEATH", SqlDbType.VarChar).Value = aa.Text;


            conn2.Open();
            cmd2.ExecuteNonQuery();

            DataTable dt = new DataTable();
            MySqlDataAdapter da = new MySqlDataAdapter();
            da.SelectCommand = cmd2;
            DataSet ds = new DataSet();
            da.Fill(ds, "DEATH_NUMBER");
            da.Fill(ds, "NAME");
            da.Fill(ds, "GENDER");
            da.Fill(ds, "DISTRICT");
            da.Fill(ds, "NATIONALITY");
            da.Fill(ds, "DATE_OF_BIRTH");
            da.Fill(ds, "PLACE_OF_BIRTH");
            da.Fill(ds, "DATE_OF_DEATH");
            da.Fill(ds, "PLACE_OF_DEATH");

            GridView1.DataSource = ds;
            GridView1.DataBind();
            conn2.Close();

        }

        protected void cmdsearch1_Click(object sender, EventArgs e)
        {
            MySqlConnection conn = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=Nira;User Id=root;Password=''");
            conn2.Open();
            if (aa.Text != "")
            {
                MySqlCommand cmd = new MySqlCommand("SELECT DEATH_NUMBER,NAME,GENDER,DISTRICT,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_DEATH,PLACE_OF_DEATH from Death WHERE DEATH_NUMBER =@id", conn2);
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
                    g.Text = dr.GetValue(5).ToString();
                    h.Text = dr.GetValue(5).ToString();
                    j.Text = dr.GetValue(5).ToString();


                }
            }

        }
    }
}