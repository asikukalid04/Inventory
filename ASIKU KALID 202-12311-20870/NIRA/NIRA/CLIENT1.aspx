<%@ Page Title="" Language="C#" MasterPageFile="~/CLIENT.Master" AutoEventWireup="true" CodeBehind="CLIENT1.aspx.cs" Inherits="NIRA.WebForm2" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <style type="text/css">
        .auto-style8 {
            color: #006600;
        background-color: #996633;
    }
        .auto-style12 {
        font-weight: bold;
        color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style13 {
            text-align: right;
        background-color: #996633;
    }
        .auto-style14 {
        height: 23px;
        text-align: center;
        background-color: #996633;
    }
        .auto-style15 {
            font-weight: bold;
            height: 45px;
            width: 693px;
        color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style16 {
            text-align: center;
            height: 45px;
        background-color: #996633;
    }
        .auto-style17 {
            font-weight: bold;
            text-align: center;
        color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style18 {
        width: 693px;
        font-weight: bold;
        height: 23px;
        color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style19 {
        text-align: center;
        background-color: #996633;
    }
    .auto-style20 {
        font-weight: bold;
        width: 693px;
        background-color: #996633;
    }
    .auto-style21 {
        color: #FFFFFF;
        background-color: #996633;
    }
    .auto-style22 {
        font-weight: bold;
        width: 693px;
        color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style23 {
            font-weight: bold;
            text-align: center;
            color: #FFFFFF;
            background-color: #996633;
            height: 23px;
        }
        .auto-style24 {
            font-weight: bold;
            text-align: center;
            color: #FFFFFF;
            background-color: #996633;
            height: 34px;
        }
    </style>
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="ContentPlaceHolder2" runat="server">
    <table class="auto-style1" style="color: #FFFFFF">
        <tr>
            <td class="auto-style8" colspan="2" style="text-align: center"><strong>DEATH RIGISTRATION</strong></td>
        </tr>
        <tr>
            <td class="auto-style20">DEATH_NUMBER</td>
            <td class="auto-style19">
                <strong>
                <asp:TextBox ID="a" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style20">NAME</td>
            <td class="auto-style19">
                <strong>
                <asp:TextBox ID="b" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style20">GENDER</td>
            <td class="auto-style19">
                <strong>
                <asp:TextBox ID="c" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">DISTRICT</td>
            <td class="auto-style14">
                <strong>
                <asp:TextBox ID="d" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style22">NATIONALITY</td>
            <td class="auto-style19">
                <strong>
                <asp:TextBox ID="ee" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">DATE_OF_BIRTH</td>
            <td class="auto-style14">
                <strong>
                <asp:TextBox ID="f" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style22">PLACE_OF_BIRTH</td>
            <td class="auto-style19">
                <strong>
                <asp:TextBox ID="g" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style22">DATE_OF_DEATH</td>
            <td class="auto-style19">
                <strong>
                <asp:TextBox ID="h" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style15">PLACE_OF_DEATH</td>
            <td class="auto-style16">
                <strong>
                <asp:TextBox ID="j" runat="server" Height="31px" Width="289px"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style17" colspan="2"><strong style="text-align: center">&nbsp;<asp:Button ID="cmdsave" runat="server" CssClass="auto-style12" Height="35px" OnClick="cmdsave_Click1" Text="SUBMIT" Width="99px" />
                <span class="auto-style21">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmdclr" runat="server" CssClass="auto-style12" Height="35px" OnClick="cmdclr_Click1" Text="CLEAR" Width="99px" />
                <span class="auto-style21">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmddel" runat="server" CssClass="auto-style12" Height="35px" OnClick="cmddel_Click" Text="DELETE" Width="99px" />
                <span class="auto-style21">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmdupdate" runat="server" CssClass="auto-style12" Height="35px" OnClick="cmdupdate_Click1" Text="UPDATE" Width="99px" />
                <span class="auto-style21">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmdupdate0" runat="server" CssClass="auto-style12" Height="35px" OnClick="cmdupdate0_Click1" Text="VIEW DATA!" Width="99px" />
                </strong></td>
        </tr>
        <tr>
            <td class="auto-style24" colspan="2">
                <asp:Button ID="cmdsearch" runat="server" Height="34px" OnClick="cmdsearch_Click" Text="SEARCH" Width="100px" />
                <strong style="text-align: center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </strong>
                <asp:TextBox ID="aa" runat="server" Height="29px"></asp:TextBox>
            </td>
        </tr>
        <tr>
            <td class="auto-style23" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <asp:Button ID="cmdsearch1" runat="server" Height="34px" OnClick="cmdsearch1_Click" Text="SEARCH" Width="100px" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td>
        </tr>
        <tr>
            <td class="auto-style20">
                <asp:GridView ID="GridView1" runat="server">
                </asp:GridView>
            </td>
            <td class="auto-style13">&nbsp;</td>
        </tr>
    </table>
</asp:Content>
