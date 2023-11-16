<%@ Page Title="" Language="C#" MasterPageFile="~/CLIENT.Master" AutoEventWireup="true" CodeBehind="CLIENT.aspx.cs" Inherits="AIRTEL.CLIENT1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <style type="text/css">
    .auto-style4 {
        color: #006600;
        background-color: #999966;
    }
    .auto-style5 {        background-color: #999966;
    }
    .auto-style6 {
            width: 1018px;
            height: 42px;
            text-align: left;
            color: #FFFFFF;
            font-weight: bold;
            font-size: larger;
            background-color: #999999;
        }
    .auto-style7 {
        height: 42px;
        text-align: center;
        background-color: #999999;
    }
    .auto-style8 {
            width: 1018px;
            text-align: left;
            background-color: #999999;
            color: #FFFFFF;
            font-weight: bold;
        }
        .auto-style9 {
        text-align: right;
        background-color: #999999;
    }
    .auto-style10 {
        background-color: #999999;
    }
    .auto-style11 {
        color: #660033;
        background-color: #999999;
    }
    .auto-style12 {
        background-color: #993366;
    }
        .auto-style13 {
            text-align: right;
            background-color: #999999;
        }
        .auto-style14 {
            height: 42px;
            text-align: right;
            width: 100%;
            background-color: #999999;
        }
        .auto-style15 {
            background-color: #999999;
            width: 1018px;
        }
    </style>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <table class="auto-style1">
    <tr>
        <td class="auto-style4" colspan="2"><strong>CLIENT REGISTRATION FORM</strong></td>
    </tr>
    <tr>
        <td class="auto-style6">CLIENT_NO</td>
        <td class="auto-style14">
            <asp:TextBox ID="a" runat="server" Height="32px" Width="225px" CssClass="auto-style12"></asp:TextBox>
        </td>
    </tr>
    <tr>
        <td class="auto-style6">CLIENT_NA</td>
        <td class="auto-style14">
            <asp:TextBox ID="b" runat="server" Height="32px" Width="225px" CssClass="auto-style12"></asp:TextBox>
        </td>
    </tr>
    <tr>
        <td class="auto-style8">CLIENT_CO</td>
        <td class="auto-style13">
            <asp:TextBox ID="c" runat="server" Height="32px" Width="225px" CssClass="auto-style12"></asp:TextBox>
        </td>
    </tr>
    <tr>
        <td class="auto-style8">CLIENT_AD</td>
        <td class="auto-style13">
            <asp:TextBox ID="d" runat="server" Height="32px" Width="225px" CssClass="auto-style12"></asp:TextBox>
        </td>
    </tr>
    <tr>
        <td class="auto-style8">CLIENT_SE</td>
        <td class="auto-style13">
            <asp:TextBox ID="ee" runat="server" Height="32px" Width="225px" CssClass="auto-style12"></asp:TextBox>
        </td>
    </tr> 
    <tr>
        <td class="auto-style8">CLIENT_AM</td>
        <td class="auto-style9">
            <asp:TextBox ID="f" runat="server" Height="32px" Width="225px" CssClass="auto-style12"></asp:TextBox>
        </td>
    </tr>
    <tr>
        <td class="auto-style10" colspan="2">
            <asp:Button ID="cmdsave" runat="server" Height="37px" Text="SUBMIT" Width="100px" style="font-weight: 700" OnClick="cmdsave_Click" />
&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="cmdclr" runat="server" Height="37px" Text="CLEAR" Width="100px" style="font-weight: 700; color: #996600" OnClick="cmdclr_Click" />
&nbsp;&nbsp;&nbsp;
            <asp:Button ID="cmddelete" runat="server" Height="37px" Text="DELETE" Width="100px" style="font-weight: 700; color: #CC0000" OnClick="cmddelete_Click" />
&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="cmdupdate" runat="server" Height="37px" Text="UPDATE" Width="100px" style="font-weight: 700; color: #006600" OnClick="cmdupdate_Click" />
&nbsp;&nbsp;&nbsp;
            <asp:Button ID="cmdupdate0" runat="server" Height="37px" Text="VIEW DATA!" Width="100px" style="font-weight: 700; color: #000099" OnClick="cmdupdate0_Click" />
        </td>
    </tr>
    <tr>
        <td class="auto-style10" colspan="2">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="searchbtn" runat="server" Height="39px" OnClick="searchBtn_Click" style="font-weight: 700" Text="SEARCH" Width="121px" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<asp:TextBox ID="aa" runat="server" Height="35px"></asp:TextBox>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </td>
    </tr>
    <tr>
        <td class="auto-style10" colspan="2">
            <asp:Button ID="SEARCH" runat="server" Height="38px" OnClick="SEARCH_Click" style="font-weight: 700" Text="SEARCH" Width="121px" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td>
    </tr>
    <tr>
        <td class="auto-style15">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:GridView ID="GridView1" runat="server" Width="277px" style="color: #FFFFFF">
            </asp:GridView>
        </td>
        <td class="auto-style11">
            &nbsp;</td>
    </tr>
</table>
</asp:Content>
