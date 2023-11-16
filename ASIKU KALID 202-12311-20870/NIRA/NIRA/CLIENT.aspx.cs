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
    public partial class WebForm1 : System.Web.UI.Page
    {
        MySql.Data.MySqlClient.MySqlConnection conn;
        MySql.Data.MySqlClient.MySqlCommand cmd;
        String queryStr;
        MySqlConnection conn2 = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=NIRA;User Id=root;Password=''");
        protected void cmdsave_Click(object sender, EventArgs e)
        {
            String ConnString = System.Configuration.ConfigurationManager.ConnectionStrings["NIRAAppConnString"].ToString();
            conn = new MySql.Data.MySqlClient.MySqlConnection(ConnString);
            conn.Open();
            queryStr = "";
            queryStr = "INSERT INTO NIRA.BIRTH(BIRTH_NUMBER,NAME,GENDER,DISTRICT,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,PLACE_OF_RESIDENCE)" +
                            "VALUES('" + a.Text + "','" + b.Text + "','" + c.Text + "','" + d.Text + "','" + ee.Text + "','" + f.Text + "','" + g.Text + "','" + h.Text + "')";
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
            g.Text = "";
            h.Text = "";
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
            cmd2.CommandText = "delete from BIRTH where BIRTH_NUMBER='" + a.Text + "'";
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
            cmd2.CommandText = "update BIRTH set BIRTH_NUMBER='" + a.Text + "',NAME='" + b.Text + "',GENDER='" + c.Text + "',DISTRICT='" + d.Text + "',NATIONALITY='" + ee.Text + "',DATE_OF_BIRTH='" + f.Text + "',PLACE_OF_BIRTH='" + g.Text + "',PLACE_OF_RESIDENCE='" + h.Text + "' where BIRTH_NUMBER='" + a.Text + "'";
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

            String ConnString = System.Configuration.ConfigurationManager.ConnectionStrings["NIRAAppConnString"].ToString();
            conn = new MySqlConnection(ConnString);
            conn.Open();
            queryStr = "";
            queryStr = "select * from BIRTH";
            cmd = new MySqlCommand(queryStr, conn);
            cmd.ExecuteNonQuery();
            DataTable dt = new DataTable();
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(dt);
            GridView1.DataSource = dt;
            GridView1.DataBind();
            conn.Close();
        }

        protected void cmdsearch_Click(object sender, EventArgs e)
        {
            searchbtn444();
        }
        private void searchbtn444()
        {

            MySqlConnection conn2 = new MySqlConnection(@"Data Source=localhost;port=3306;Initial Catalog=Nira;User Id=root;Password=''");


            string find = "select * from Birth where(BIRTH_NUMBER like '" + aa.Text + "' or  NAME  like '" + aa.Text + "' or GENDER  like '" + aa.Text + "' or DISTRICT like '" + aa.Text + "' or NATIONALITY  like '" + aa.Text + "' or DATE_OF_BIRTH  like '" + aa.Text + "' or PLACE_OF_BIRTH like '" + aa.Text + "' or PLACE_OF_RESIDENCE like '" + aa.Text + "')";

            MySqlCommand cmd2 = new MySql.Data.MySqlClient.MySqlCommand(find, conn2);
            cmd2.Parameters.Add("@DBIRTH_NUMBER", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@NAME", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@GENDER", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@DISTRICT", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@NATIONALITY", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@DATE_OF_BIRTH", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@PLACE_OF_BIRTH", SqlDbType.VarChar).Value = aa.Text;
            cmd2.Parameters.Add("@PLACE_OF_RESIDENCE", SqlDbType.VarChar).Value = aa.Text;
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
            da.Fill(ds, "PLACE_OF_BIRTH");
            da.Fill(ds, "PLACE_OF_RESIDENCE");
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
                MySqlCommand cmd = new MySqlCommand("SELECT BIRTH_NUMBER,NAME,GENDER,DISTRICT,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,PLACE_OF_RESIDENCE from BIRTH WHERE BIRTH_NUMBER =@id", conn2);
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
                    g.Text = dr.GetValue(6).ToString();
                    h.Text = dr.GetValue(7).ToString();



                }
            }
        }


    }
 }